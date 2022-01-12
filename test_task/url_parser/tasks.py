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
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code != requests.codes.ok:
            result_json = {'error': f'URL returned {status_code}'}
        else:
            result_json = parse_response(response)
    except requests.exceptions.ConnectionError:
        result_json = {'error': 'Could not connect to server'}
    
    result = Result.objects.get(ticket_id=ticket_id)
    result.result = result_json
    result.save()