import unittest
from app import app

class TelecomBotTestCases(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # =========================================
    # TEST 1 — CHECK BALANCE
    # =========================================
    def test_check_balance(self):

        payload = {
            "fulfillmentInfo": {
                "tag": "check-balance"
            },
            "sessionInfo": {
                "parameters": {
                    "mobile": "1234567890"
                }
            }
        }

        response = self.client.post(
            '/webhook',
            json=payload
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "Your current balance is",
            data["fulfillment_response"]["messages"][0]["text"]["text"][0]
        )

    # =========================================
    # TEST 2 — CREATE TICKET
    # =========================================
    def test_create_ticket(self):

        payload = {
            "fulfillmentInfo": {
                "tag": "create-ticket"
            },
            "sessionInfo": {
                "parameters": {
                    "mobile": "9876543210"
                }
            }
        }

        response = self.client.post(
            '/webhook',
            json=payload
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "Complaint created successfully",
            data["fulfillment_response"]["messages"][0]["text"]["text"][0]
        )

    # =========================================
    # TEST 3 — INVALID TAG
    # =========================================
    def test_invalid_tag(self):

        payload = {
            "fulfillmentInfo": {
                "tag": "unknown-tag"
            }
        }

        response = self.client.post(
            '/webhook',
            json=payload
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "Webhook reached but tag not matched",
            data["fulfillment_response"]["messages"][0]["text"]["text"][0]
        )

    # =========================================
    # TEST 4 — VERIFY OTP SUCCESS
    # =========================================
    def test_verify_otp_success(self):

        payload = {
            "fulfillmentInfo": {
                "tag": "verify-otp"
            },
            "sessionInfo": {
                "parameters": {
                    "mobile_number": "1234567890",
                    "otp_code": "123456"
                }
            }
        }

        response = self.client.post(
            '/webhook',
            json=payload
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        # OPTIONAL CHECK
        # Depending on your webhook implementation
        # update message accordingly

    # =========================================
    # TEST 5 — WEBHOOK HEALTH
    # =========================================
    def test_webhook_endpoint(self):

        response = self.client.post(
            '/webhook',
            json={}
        )

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()