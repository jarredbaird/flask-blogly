from unittest import TestCase
from app import app
from flask import session

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BloglyTestCases(TestCase):
    """Examples of integration tests: testing Flask app."""

    def test_blogly_html(self):
        with app.test_client() as client:
            # can now make requests to flask via `client`
            response = client.get('/users')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<div class="container mt-5">', html)

    def test_user_new(self):
        with app.test_client() as client:
            response = client.get('/users/new')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)

    def test_edit_user(self):
        with app.test_client() as client:
            response = client.get('/users/edit/1')

            self.assertEqual(response.status_code, 200)

    def test_view_user(self):
        with app.test_client() as client:
            response = client.get('/users/1')

            self.assertEqual(response.status_code, 200)