FROM python:3.8.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir --default-timeout 100 -r requirements.txt

COPY . /app/

# CMD ["python", "manage.py", "migrate"]