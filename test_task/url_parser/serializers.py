from rest_framework import serializers
from .models import Ticket, Result
import requests

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'url']

    def validate(self, attrs):
        # if attrs.get('url'):
        #     response = requests.head(attrs.get('url'))
        #     code = response.status_code
        #     if code != requests.codes.ok:
        #         raise serializers.ValidationError({"error": f"URL returned {code} status code."})
        return attrs

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['ticket_id', 'result']