from rest_framework import serializers
from .models import Ticket, Result
import requests

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['uuid', 'url']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['ticket', 'result']