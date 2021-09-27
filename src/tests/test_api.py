from fastapi.testclient import TestClient

from app.api import app
from app.settings import configs

import unittest


class TestPartners(unittest.TestCase):

    def setUp(self):
        url = '%s://%s:%d' % ('http', 'localhost', configs.APP_PORT)
        self.client = TestClient(app=app, base_url=url)

    def test_get_partners(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        body = response.json()
        print(str(body))
        self.assertTrue(len(body) > 0)

