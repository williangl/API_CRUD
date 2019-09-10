from json import loads
from unittest import TestCase

from api_crud import create_app
from flask import url_for


class TestFlaskBase(TestCase):
    """Base class for test flask application."""

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.app.db.creat_all()
        self.costumer = {
            'name': 'test',
            'password': '123',
            'email': 'test@test.com'
        }

    def tearDown(self):
        self.app.db.drop_all()

    def create_client(self):
        self.client.post(url_for('client.register'), json=self.costumer)

    def create_token(self):
        login = self.client.post(url_for('login.login'), json=self.costumer)
        return {
            'authorization':
            'Bearer' + loads(login.data.decode())['access_token']
        }
