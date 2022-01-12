from django.test import TestCase
from url_parser.models import Ticket, Result
from django.utils import timezone


class TicketTest(TestCase):
    def setUp(self):
        Ticket.objects.create(
            url="https://www.django-rest-framework.org/api-guide/testing/")
        Ticket.objects.create(
            url="https://github.com/axnsan12/drf-yasg"
        )

    def test_ticket_created_at(self):
        now = timezone.now()
        ticket = Ticket.objects.create(
            url="https://www.django-rest-framework.org/api-guide/testing/"
        )
        self.assertEqual(now.replace(microsecond=0), ticket.created_at.replace(microsecond=0))

    def test_ticket_post_save(self):
        ticket = Ticket.objects.create(
            url="https://www.django-rest-framework.org/api-guide/testing/"
        )
        result = Result.objects.get(ticket_id=ticket.uuid)
        self.assertEqual(result.result, "In queue")

    # def test_ticket