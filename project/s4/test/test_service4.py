from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
import json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponseService4(TestBase):
    def test_correct_stadium_team(self):
        response = self.client.post(url_for('outcome'), json={'team':'Bayern Munich', 'stadium':'Allianz Arena'})
        self.assertIn(b'True', response.data)

    def test_incorrect_stadium_team(self):
        response = self.client.post(url_for('outcome'), json={'team':'Bayern Munich', 'stadium':'Volkswagen Arena'})
        self.assertIn(b'False', response.data)
    