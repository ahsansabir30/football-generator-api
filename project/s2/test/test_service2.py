from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponseService2(TestBase):
    def test_page_response(self):
        response = self.client.get(url_for('getteams'))
        self.assert200(response)
        assert response.data.decode('utf-8') in ['Bayern Munich', 'Borussia Dortmund', 'VfL Wolfsburg', 'Leverkusen', 'Eintracht Frankfurt', 'Borussia Mönchengladbach']