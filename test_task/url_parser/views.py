from rest_framework import viewsets
from rest_framework import mixins
from url_parser.models import Ticket, Result
from url_parser.serializers import TicketSerializer, ResultSerializer


class TicketViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    Add a new ticket to the queue to parse html from
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ResultViewSet(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    Endpoint for getting results
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer