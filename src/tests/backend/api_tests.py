import json
import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from src.backend.api.models import User, Feedback
from src.backend.api.views import ModelResponseView

class APITests(APITestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='testuser', password='testpassword')
        Feedback.objects.create(comment='Test feedback', user=User.objects.get(username='testuser'))

    def test_user_schema(self):
        # Ensure UserSchema is correct and serializable
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(isinstance(user, User))

    def test_feedback_schema(self):
        # Ensure FeedbackSchema is correct and serializable
        feedback = Feedback.objects.get(comment='Test feedback')
        self.assertEqual(feedback.comment, 'Test feedback')
        self.assertTrue(isinstance(feedback, Feedback))

    def test_model_response_view(self):
        # Test the ModelResponseView to ensure it returns a valid response
        url = reverse('model-response')
        response = self.client.post(url, {'input_text': 'Hello, world!'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('response_text' in json.loads(response.content))

    def test_api_base_url(self):
        # Test if API_BASE_URL is reachable and responds correctly
        response = self.client.get(API_BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theme_settings_consistency(self):
        # Test if THEME_SETTINGS is consistent across responses
        response = self.client.get(reverse('theme-settings'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), THEME_SETTINGS)

    def test_name_consistency(self):
        # Check for any missed references to the old name in the codebase
        self.assertFalse(updateNameReferences('Smol-Developer'), 'Old name reference found')

    def test_ui_integration(self):
        # Test UI component integration
        response = self.client.get(reverse('ui-integration-status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['message'], UI_INTEGRATION_COMPLETE)

    def test_deployment_status(self):
        # Test deployment status updates
        response = self.client.get(reverse('deployment-status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['message'], DEPLOYMENT_STATUS)

if __name__ == '__main__':
    unittest.main()