# Tests for the command processor

import unittest, sys, os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from commands import CommandProcessor
from main import ChatBot


class TestCommandProcessor(unittest.TestCase):
    """Test cases for the CommandProcessor class"""

    def setUp(self):
        """Set up test fixtures"""
        self.chatbot = ChatBot()
        self.command_processor = CommandProcessor(self.chatbot)

    def test_help_command(self):
        """Test the help command"""
        response = self.command_processor.process_command("/help")
        self.assertIn("Available commands", response)
        self.assertIn("/help", response)
        self.assertIn("/city", response)
        self.assertIn("/restart", response)
        self.assertIn("/info", response)
        self.assertIn("/nearby", response)

    def test_city_command(self):
        """Test the city command"""
        # Test with valid city
        response = self.command_processor.process_command("/city Warsaw")
        self.assertIn("Warsaw", response)
        self.assertEqual(self.chatbot.get_city(), "Warsaw")

        # Test with invalid city
        response = self.command_processor.process_command("/city InvalidCity")
        self.assertIn("not a recognized city", response)

        # Test without city name
        response = self.command_processor.process_command("/city")
        self.assertIn("Please provide a city name", response)

    def test_restart_command(self):
        """Test the restart command"""
        # Set a city first
        self.chatbot.set_city("Warsaw")
        self.assertEqual(self.chatbot.get_city(), "Warsaw")

        # Test restart
        response = self.command_processor.process_command("/restart")
        self.assertIsNone(self.chatbot.get_city())
        self.assertEqual(response, self.chatbot.get_greeting())

    def test_info_command(self):
        """Test the info command"""
        # Test with valid attraction
        response = self.command_processor.process_command("/info Royal Castle")
        self.assertIn("Royal Castle in Warsaw", response)
        self.assertIn("Opening hours", response)

        # Test with invalid attraction
        response = self.command_processor.process_command("/info NonExistentAttraction")
        self.assertIn("don't have information", response)

        # Test without attraction name
        response = self.command_processor.process_command("/info")
        self.assertIn("Please provide an attraction name", response)

    def test_nearby_command(self):
        """Test the nearby command"""
        # Test without city
        response = self.command_processor.process_command("/nearby mountain")
        self.assertIn("Please set your city", response)

        # Set city and test with valid tourism type
        self.chatbot.set_city("Warsaw")
        response = self.command_processor.process_command("/nearby mountain")
        self.assertIn("Nearby mountain attraction in Warsaw", response)

        # Test with invalid tourism type
        response = self.command_processor.process_command("/nearby invalid")
        self.assertIn("Unknown tourism type", response)

        # Test without tourism type
        response = self.command_processor.process_command("/nearby")
        self.assertIn("Please provide a tourism type", response)

    def test_exit_command(self):
        """Test the exit command"""
        response = self.command_processor.process_command("/exit")
        self.assertEqual(response, "EXIT")

        response = self.command_processor.process_command("/quit")
        self.assertEqual(response, "EXIT")

    def test_unknown_command(self):
        """Test an unknown command"""
        response = self.command_processor.process_command("/unknown")
        self.assertIn("Unknown command", response)
        self.assertIn("/help", response)


if __name__ == '__main__':
    unittest.main()
