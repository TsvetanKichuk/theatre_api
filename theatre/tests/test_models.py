from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from theatre.models import (
    Genre,
    Actor,
    TheatreHall,
    Play,
    Performance,
    Reservation,
    Ticket,
)

User = get_user_model()


class ModelsTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.play = Play.objects.create(
            title="Hamlet", description="A Shakespearean tragedy"
        )
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=datetime.now() + timedelta(days=1),
        )
        self.user = User.objects.create_user(email="test_email", password="testpass")
        self.reservation = Reservation.objects.create(user=self.user)

    def test_genre_str(self):
        self.assertEqual(str(self.genre), "Drama")

    def test_actor_str_and_full_name(self):
        self.assertEqual(str(self.actor), "John Doe")
        self.assertEqual(self.actor.full_name, "John Doe")

    def test_theatre_hall_str_and_capacity(self):
        self.assertEqual(str(self.theatre_hall), "Main Hall")
        self.assertEqual(self.theatre_hall.capacity, 150)

    def test_play_str(self):
        self.assertEqual(str(self.play), "Hamlet")

    def test_performance_str(self):
        self.assertEqual(str(self.performance), f"Hamlet {self.performance.show_time}")

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation), str(self.reservation.created_at))

    def test_ticket_creation_valid(self):
        ticket = Ticket(
            performance=self.performance, reservation=self.reservation, row=5, seat=10
        )
        try:
            ticket.full_clean()
            ticket.save()
            self.assertIsNotNone(ticket.id)
        except ValidationError:
            self.fail("Ticket creation failed with valid row and seat numbers")

    def test_ticket_string_representation(self):
        ticket = Ticket(
            performance=self.performance, reservation=self.reservation, row=5, seat=10
        )
        ticket.full_clean()
        ticket.save()
        self.assertEqual(
            str(ticket),
            f"{str(self.performance)} (row: {ticket.row}, seat: {ticket.seat})",
        )

    def test_ticket_unique_together_constraint(self):
        Ticket.objects.create(
            performance=self.performance, reservation=self.reservation, row=5, seat=10
        )
        with self.assertRaises(ValidationError) as e:
            duplicate_ticket = Ticket(
                performance=self.performance,
                reservation=self.reservation,
                row=5,
                seat=10,
            )
            duplicate_ticket.full_clean()
        self.assertIn("__all__", e.exception.message_dict)
