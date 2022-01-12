from django import dispatch
from django.db import models
import uuid
import requests
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Ticket(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Ticket)
def init_result(sender, instance, **kwargs):
    result = Result.objects.create(
        ticket=instance,
        result="In queue"
    )
    from url_parser.tasks import handle_ticket

    handle_ticket.delay(instance.uuid, instance.url)

class Result(models.Model):
    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None
    )
    result = models.JSONField()