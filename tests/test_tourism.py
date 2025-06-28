# Tests for the tourism classes demonstrating polymorphism

import unittest, sys, os

# Add the parent directory to the path so we can import the tourism module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tourism import TourismType, MountainTourism, SeaTourism, CulturalTourism, create_tourism_type


class TestTourismPolymorphism(unittest.TestCase):
    """Test cases for tourism classes demonstrating polymorphism"""

    def test_base_tourism_type(self):
        """Test the base TourismType class"""
        tourism = TourismType("generic")
        self.assertEqual(tourism.get_name(), "generic")
        self.assertEqual(tourism.get_subtypes(), [])
        self.assertEqual(tourism.get_description(), "General tourism activities in Poland")
        self.assertEqual(tourism.recommend_attraction("Warsaw"), "A popular generic attraction in Warsaw")

    def test_mountain_tourism(self):
        """Test the MountainTourism class"""
        tourism = MountainTourism()
        self.assertEqual(tourism.get_name(), "mountain")
        self.assertEqual(tourism.get_subtypes(), ["hiking", "climbing", "skiing"])
        self.assertEqual(tourism.get_description(), "Explore the beautiful mountains of Poland")
        self.assertEqual(tourism.recommend_attraction("Warsaw"), "Day trip to Kampinos National Park")
        self.assertEqual(tourism.recommend_attraction("Unknown"), "Mountain trip from Unknown")

    def test_sea_tourism(self):
        """Test the SeaTourism class"""
        tourism = SeaTourism()
        self.assertEqual(tourism.get_name(), "sea")
        self.assertEqual(tourism.get_subtypes(), ["beaches", "sailing", "diving"])
        self.assertEqual(tourism.get_description(), "Enjoy Poland's beautiful Baltic coastline")
        self.assertEqual(tourism.recommend_attraction("Gdansk"), "Relaxing day at Sopot Beach")

    def test_cultural_tourism(self):
        """Test the CulturalTourism class"""
        tourism = CulturalTourism()
        self.assertEqual(tourism.get_name(), "cultural")
        self.assertEqual(tourism.get_subtypes(), ["museums", "historical sites", "theaters"])
        self.assertEqual(tourism.get_description(), "Discover Poland's rich cultural heritage")
        self.assertEqual(tourism.recommend_attraction("Krakow"), "Wawel Castle and Historic Center")

    def test_polymorphic_behavior(self):
        """Test polymorphic behavior with different tourism types"""
        # Create a list of different tourism types
        tourism_list = [
            TourismType("generic"),
            MountainTourism(),
            SeaTourism(),
            CulturalTourism()
        ]

        # Demonstrate polymorphism by calling the same methods on different objects
        descriptions = [tourism.get_description() for tourism in tourism_list]
        self.assertEqual(len(descriptions), 4)
        self.assertNotEqual(descriptions[0], descriptions[1])  # Base class vs Mountain

        # Test recommendations for Warsaw across different types
        recommendations = [tourism.recommend_attraction("Warsaw") for tourism in tourism_list]
        self.assertEqual(len(recommendations), 4)
        self.assertNotEqual(recommendations[1], recommendations[2])  # Mountain vs Sea

    def test_factory_function(self):
        """Test the factory function for creating tourism types"""
        mountain = create_tourism_type("mountain")
        sea = create_tourism_type("sea")
        cultural = create_tourism_type("cultural")
        generic = create_tourism_type("unknown")

        # Verify correct types are created
        self.assertIsInstance(mountain, MountainTourism)
        self.assertIsInstance(sea, SeaTourism)
        self.assertIsInstance(cultural, CulturalTourism)
        self.assertIsInstance(generic, TourismType)

        # Verify polymorphic behavior through the factory
        self.assertEqual(mountain.get_description(), "Explore the beautiful mountains of Poland")
        self.assertEqual(sea.get_description(), "Enjoy Poland's beautiful Baltic coastline")
        self.assertEqual(cultural.get_description(), "Discover Poland's rich cultural heritage")
        self.assertEqual(generic.get_name(), "unknown")


if __name__ == '__main__':
    unittest.main()
