from django import dispatch
from django.db import models
import uuid
import requests
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    url = models.URLField()

    def save(self, *args, **kwargs):
        # response = requests.get(self.url)
        # code = response.status_code
        # if code != requests.codes.ok:
        #     raise serializers.ValidationError({"error": f"URL returned {code} status code."})
        # result = Result.objects.create(
        #     ticket_id=self,
        #     result="In queue"
        # )

        # from url_parser.tasks import handle_ticket
        # result = handle_ticket.delay(self.id, self.url)
        # print(result.ready())
        super(Ticket, self).save(*args, **kwargs)

@receiver(post_save, sender=Ticket)
def init_result(sender, instance, **kwargs):
    result = Result.objects.create(
        ticket_id=instance.id,
        result="In queue"
    )
    from url_parser.tasks import handle_ticket

    handle_ticket.delay(instance.id, instance.url)

    # print(sender)
    # print(instance)
    # print(**kwargs)

class Result(models.Model):
    ticket_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    result = models.TextField()