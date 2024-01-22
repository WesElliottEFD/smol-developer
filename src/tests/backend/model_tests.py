import unittest
from src.backend.api.models import AIModel
from src.utils.documentation_updater import updateNameReferences

class TestAIModel(unittest.TestCase):
    def setUp(self):
        # Initialize the AIModel with GPT-4 Turbo
        self.model = AIModel(model_name='GPT-4 Turbo')

    def test_model_name(self):
        # Test if the model name is correctly set to GPT-4 Turbo
        self.assertEqual(self.model.model_name, 'GPT-4 Turbo')

    def test_context_length(self):
        # Test if the context length is adjusted for GPT-4 Turbo's capabilities
        self.assertTrue(self.model.context_length > 2048)

    def test_model_response_schema(self):
        # Test if the model response follows the defined schema
        response = self.model.generate_response('Hello, world!')
        self.assertIn('text', response)
        self.assertIsInstance(response['text'], str)

    def test_update_name_references(self):
        # Test if the name references in the documentation are updated
        updated_content = updateNameReferences('Smol-Developer is now DevFusion.')
        self.assertNotIn('Smol-Developer', updated_content)
        self.assertIn('DevFusion', updated_content)

    def test_model_performance(self):
        # Test the performance of the model with a longer context
        long_context = ' ' * 4096  # Simulate a long context
        response = self.model.generate_response(long_context)
        self.assertIsNotNone(response)
        self.assertIn('text', response)

if __name__ == '__main__':
    unittest.main()