from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from theatre.models import Play, TheatreHall, Genre, Actor
from theatre.serializers import (
    PlayListSerializer,
    PlayDetailSerializer,
    PlaySerializer,
)
from theatre.views import PlayViewSet

PlAY_URL = reverse("theatre:play-list")
MOVIE_SESSION_URL = reverse("theatre:performance-list")


def sample_play(**params):
    defaults = {
        "title": "Sample play",
        "description": "Sample description",
    }
    defaults.update(params)

    return Play.objects.create(**defaults)


def sample_genre(**params):
    defaults = {
        "name": "Drama",
    }
    defaults.update(params)

    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {"first_name": "John", "last_name": "Doe"}
    defaults.update(params)

    return Actor.objects.create(**defaults)


def sample_performance(**params):
    theatre_hall = TheatreHall.objects.create(name="Blue", rows=20, seats_in_row=20)

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "play": None,
        "theatre_hall": theatre_hall,
    }
    defaults.update(params)


class PlayViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.test", password="testpassword"
        )
        self.client.force_authenticate(self.user)
        self.genre = sample_genre()
        self.actor = sample_actor()
        self.play = sample_play()
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        self.play.save()

    def test_list_movies(self):
        url = PlAY_URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_movie(self):
        url = reverse("theatre:play-detail", args=[self.play.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_play_by_title(self):
        url = PlAY_URL + f"?title={self.play.title}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.play.title)
        self.assertIsNot(response.data[0]["title"], [])

    def test_filter_play_by_genre(self):
        url = (PlAY_URL + f"?genres={self.genre.id}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.play.title)
        self.assertIsNot(response.data[0]["genres"], [])

    def test_filter_play_by_actor(self):
        url = (PlAY_URL + f"?actors={self.actor.id}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.play.title)
        self.assertIsNot(response.data[0]["actors"], [])

    def test_get_serializer_class(self):
        view = PlayViewSet()
        view.action = "list"
        self.assertEqual(view.get_serializer_class(), PlayListSerializer)

        view.action = "retrieve"
        self.assertEqual(view.get_serializer_class(), PlayDetailSerializer)

        view.action = ""
        self.assertEqual(view.get_serializer_class(), PlaySerializer)
