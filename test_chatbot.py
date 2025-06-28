"""
Tests for the simplified Chat-BPT chatbot
"""
import unittest
from main import ChatBot


class TestChatBot(unittest.TestCase):
    """Test cases for the ChatBot class"""

    def setUp(self):
        """Set up test fixtures"""
        self.chatbot = ChatBot()

    def test_initialization(self):
        """Test chatbot initialization"""
        self.assertIsNotNone(self.chatbot)
        self.assertIsNone(self.chatbot.get_city())
        self.assertIsInstance(self.chatbot.get_greeting(), str)

    def test_city_operations(self):
        """Test city operations"""
        # Test setting and getting city
        self.chatbot.set_city("Warsaw")
        self.assertEqual(self.chatbot.get_city(), "Warsaw")

        # Test city validation
        self.assertTrue(self.chatbot.validate_city("Warsaw"))
        self.assertTrue(self.chatbot.validate_city("Krakow"))
        self.assertFalse(self.chatbot.validate_city("InvalidCity"))

    def test_tourism_types(self):
        """Test tourism types functionality"""
        # Test getting tourism types
        types = self.chatbot.get_tourism_types()
        self.assertEqual(len(types), 3)
        self.assertIn("mountain", types)
        self.assertIn("sea", types)
        self.assertIn("cultural", types)

    def test_tourism_subtypes(self):
        """Test tourism subtypes functionality"""
        # Test getting subtypes for each tourism type
        for tourism_type in self.chatbot.get_tourism_types():
            subtypes = self.chatbot.get_tourism_subtypes(tourism_type)
            self.assertEqual(len(subtypes), 3)

        # Test invalid tourism type
        invalid_subtypes = self.chatbot.get_tourism_subtypes("invalid")
        self.assertEqual(len(invalid_subtypes), 0)

    def test_input_processing_city(self):
        """Test processing city input"""
        # Test city input
        response = self.chatbot.process_input("Warsaw")
        self.assertIn("Warsaw", response)
        self.assertEqual(self.chatbot.get_city(), "Warsaw")

    def test_input_processing_tourism(self):
        """Test processing tourism type input"""
        # Test tourism type input without city
        response = self.chatbot.process_input("mountain")
        self.assertIn("mountain", response)
        self.assertIn("Explore the beautiful mountains", response)

        # Test tourism type input with city
        self.chatbot.set_city("Warsaw")
        response = self.chatbot.process_input("mountain")
        self.assertIn("Recommended for you", response)
        self.assertIn("Kampinos National Park", response)

        # Test different tourism type with different city
        self.chatbot.set_city("Gdansk")
        response = self.chatbot.process_input("sea")
        self.assertIn("Sopot Beach", response)

    def test_polymorphic_recommendations(self):
        """Test polymorphic recommendations for different cities and tourism types"""
        city_tourism_pairs = [
            ("Warsaw", "mountain"),
            ("Warsaw", "sea"),
            ("Warsaw", "cultural"),
            ("Krakow", "mountain"),
            ("Gdansk", "sea")
        ]

        for city, tourism_type in city_tourism_pairs:
            self.chatbot.set_city(city)
            response = self.chatbot.process_input(tourism_type)
            self.assertIn(city, response)
            self.assertIn(tourism_type, response)

    def test_invalid_input(self):
        """Test invalid input"""
        response = self.chatbot.process_input("something random")
        self.assertIn("not sure what you mean", response)


if __name__ == '__main__':
    unittest.main()
