from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import mixins
from url_parser.models import Ticket, Result
from url_parser.serializers import TicketSerializer, ResultSerializer


class TicketViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ResultViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer