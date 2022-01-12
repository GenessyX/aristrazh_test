import os
from celery import Celery
import datetime
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task.settings')

app = Celery('test_task', backend='rpc://', broker='amqp://rabbitmq:rabbitmq@rabbit:5672')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5*60, delete_old_tickets.s())

@app.task
def delete_old_tickets():
    from url_parser.models import Ticket
    startdate = timezone.now() - datetime.timedelta(minutes=5)
    old_tickets = Ticket.objects.filter(created_at__lte=startdate).delete()