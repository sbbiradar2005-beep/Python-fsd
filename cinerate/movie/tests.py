from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieDetailUrlTests(TestCase):
    def test_movie_details_url_resolves(self):
        self.assertEqual(reverse('movie_details', kwargs={'movie_id': 1}), '/movie/1/')

    def test_homepage_renders_movie_details_link(self):
        Movie.objects.create(
            title='Test Movie',
            description='',
            release_date=date(2026, 1, 1),
            genre='Drama',
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/movie/1/"')
