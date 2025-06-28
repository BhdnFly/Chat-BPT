"""
Tourism classes for Chat-BPT demonstrating polymorphism
"""

class TourismType:
    """Base class for all tourism types"""

    def __init__(self, name):
        self.name = name
        self.subtypes = []

    def get_name(self):
        return self.name

    def get_subtypes(self):
        return self.subtypes

    def get_description(self):
        """Get a description of this tourism type"""
        return f"General tourism activities in Poland"

    def recommend_attraction(self, city):
        """Recommend an attraction based on the city"""
        return f"A popular {self.name} attraction in {city}"


class MountainTourism(TourismType):
    """Mountain tourism type"""

    def __init__(self):
        super().__init__("mountain")
        self.subtypes = ["hiking", "climbing", "skiing"]

    def get_description(self):
        """Override the base description"""
        return "Explore the beautiful mountains of Poland"

    def recommend_attraction(self, city):
        """Override with specific mountain recommendations"""
        attractions = {
            "Warsaw": "Day trip to Kampinos National Park",
            "Krakow": "Excursion to Tatra Mountains",
            "Gdansk": "Trip to Kashubian Switzerland",
            "Lodz": "Day trip to Góry Świętokrzyskie (Holy Cross Mountains)"
        }
        return attractions.get(city, f"Mountain trip from {city}")


class SeaTourism(TourismType):
    """Sea tourism type"""

    def __init__(self):
        super().__init__("sea")
        self.subtypes = ["beaches", "sailing", "diving"]

    def get_description(self):
        """Override the base description"""
        return "Enjoy Poland's beautiful Baltic coastline"

    def recommend_attraction(self, city):
        """Override with specific sea recommendations"""
        attractions = {
            "Warsaw": "Weekend trip to the Baltic coast",
            "Krakow": "Visit to Mazurian Lakes",
            "Gdansk": "Relaxing day at Sopot Beach",
            "Lodz": "Visit to Arturówek Lake complex with beaches and water activities"
        }
        return attractions.get(city, f"Water activities near {city}")


class CulturalTourism(TourismType):
    """Cultural tourism type"""

    def __init__(self):
        super().__init__("cultural")
        self.subtypes = ["museums", "historical sites", "theaters"]

    def get_description(self):
        """Override the base description"""
        return "Discover Poland's rich cultural heritage"

    def recommend_attraction(self, city):
        """Override with specific cultural recommendations"""
        attractions = {
            "Warsaw": "The Royal Castle and Old Town",
            "Krakow": "Wawel Castle and Historic Center",
            "Gdansk": "Main Town Hall and Neptune's Fountain",
            "Lodz": "Piotrkowska Street and Manufaktura - former factory complex turned cultural center"
        }
        return attractions.get(city, f"Cultural sites in {city}")


def create_tourism_type(type_name):
    """Factory function to create tourism types"""
    tourism_types = {
        "mountain": MountainTourism,
        "sea": SeaTourism,
        "cultural": CulturalTourism
    }

    tourism_class = tourism_types.get(type_name, TourismType)
    if tourism_class == TourismType:
        return TourismType(type_name)
    return tourism_class()
