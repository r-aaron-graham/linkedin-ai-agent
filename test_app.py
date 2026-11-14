import unittest

from app import app


class ReviewerDemoTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_start_is_simulated(self):
        response = self.client.post("/start-agent")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "simulated"})

    def test_log_is_a_fixture(self):
        response = self.client.get("/log")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["log"], ["Sample log entry 1", "Sample log entry 2"])
