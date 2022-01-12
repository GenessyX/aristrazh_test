# Техническое задание
Реализовать RESTful-сервис который позволит реализовать следующий сценарий:
1. Внешний пользователь вызывает endpoint в который передаёт произвольный URL адрес.
Его запросу присваивается некоторый уникальный идентификатор.
2. Пользователь может передавать этот идентификатор в endpoint получения результатов
обработки. Если обработка завершена, пользователь должен получить количество
уникальных тегов в документе, с количеством “вложенных” в него элементов. Например:
{“html”: {“count”:1, “nested”:100}, “body”:{“count”:1, “nested”:99}, “H1”: {“count”:2,”nested”:0}.
3. Входящие данные должны валидироваться, ошибки доступности URL, ответа внешних
серверов и т.д. обрабатываться.

# Локальный запуск приложения

```
docker-compose build
docker-compose run
```

### Получить доступ к оболочке контейнера
```
docker exec -it container_name bash
```