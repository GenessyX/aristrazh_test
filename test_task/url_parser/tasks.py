import requests
from rest_framework.serializers import Serializer
from url_parser.utils import parse_response

from url_parser.models import Ticket, Result
from url_parser.serializers import TicketSerializer, ResultSerializer

from celery import shared_task

@shared_task
def get_tickets():
    return Ticket.objects.count()

@shared_task
def handle_ticket(ticket_id, url):
    print(ticket_id, url)
    result = Result.objects.get(ticket_id=ticket_id)
    # try:
        # response = requests.get(url)
    # except requests.exceptions.ConnectionError:
        # result.result

    result_json = parse_response(url)
    result = Result.objects.get(ticket_id=ticket_id)
    result.result = result_json
    result.save()