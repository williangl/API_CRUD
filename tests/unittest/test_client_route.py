"""Test client route."""
from unittest import TestCase

from flask import url_for


class TestClientRoute(TestCase):
    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_should_create_user_on_database(self):
        user = {
            'name': 'test',
            'email': 'test@test.com'
        }

        esperado = {
            'id': '1',
            'name': 'test',
            'email': 'test@test.com'
        }

        response = self.client.post(url_for('client.register'), json=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], esperado['name'])
        self.assertEqual(response.json['email'], esperado['email'])
