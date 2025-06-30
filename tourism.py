"""
Tourism classes for Chat-BPT demonstrating polymorphism
"""
from geopy.distance import geodesic

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
        self.attractions = [
        Attraction(
            name="Tatra National Park",
            coords=(49.2712, 19.9810),
            voivodeship="Lesser Poland",
            rating=4.9,
            description="і"
        )
    ]




class SeaTourism(TourismType):
    """Sea tourism type"""

    def __init__(self):
        super().__init__("sea")
        self.subtypes = ["beaches", "sailing", "diving"]
        self.attractions = [
            Attraction(
                name="Sopot Beach",
                coords=(54.4419, 18.5601),
                voivodeship="Pomeranian",
                rating=4.7,
                description="Beautiful sandy beach and Europe’s longest wooden pier."
            )
        ]


class CulturalTourism(TourismType):
    """Cultural tourism type"""

    def __init__(self):
        super().__init__("cultural")
        self.subtypes = ["museums", "historical sites", "theaters"]
        self.attractions = [
            Attraction(
                name="Wawel Royal Castle",
                coords=(50.0545, 19.9366),
                voivodeship="Lesser Poland",
                rating=4.8,
                description="Iconic royal castle and museum in Krakow."
            )
        ]

class EcoTourism(TourismType):
    """Ecological tourism type"""

    def __init__(self):
        super().__init__("eco")
        self.subtypes = ["farm", "kayaking", "nature"]
        self.attractions = [
            Attraction(
                name="Biebrza National Park",
                coords=(53.1861, 22.6240),
                voivodeship="Podlaskie",
                rating=4.6,
                description="Vast wetlands with kayaking and rare wildlife."
            )
        ]



def create_tourism_type(type_name):
    """Factory function to create tourism types"""
    tourism_types = {
        "mountain": MountainTourism,
        "sea": SeaTourism,
        "cultural": CulturalTourism,
        "eco": EcoTourism
    }

    tourism_class = tourism_types.get(type_name, TourismType)
    if tourism_class == TourismType:
        return TourismType(type_name)
    return tourism_class()

class Attraction:
    def __init__(self, name, coords, voivodeship, rating, description):
        self.name = name
        self.coords = coords
        self.voivodeship = voivodeship
        self.rating = rating
        self.description = description

    def distance_to(self, other_coords):
        return round(geodesic(self.coords, other_coords).kilometers, 1)

    def __str__(self):
        return f"{self.name} ({self.voivodeship}) - {self.description} [Rating: {self.rating}]"


class PolishCity:
    def __init__(self, name, coords, voivodeship):
        self.name = name
        self.coords = coords
        self.voivodeship = voivodeship

    def __str__(self):
        return f"{self.name} in {self.voivodeship}"

POLISH_CITIES = {
    "Warsaw": PolishCity("Warsaw", (52.2297, 21.0122), "Masovian"),
    "Krakow": PolishCity("Krakow", (50.0647, 19.9450), "Lesser Poland"),
    "Gdansk": PolishCity("Gdansk", (54.3520, 18.6466), "Pomeranian"),
    "Lodz": PolishCity("Lodz", (51.7592, 19.4550), "Lodz"),
    "Wroclaw": PolishCity("Wroclaw", (51.1079, 17.0385), "Lower Silesian"),
    "Poznan": PolishCity("Poznan", (52.4064, 16.9252), "Greater Poland"),
    "Lublin": PolishCity("Lublin", (51.2465, 22.5684), "Lublin"),
    "Bydgoszcz": PolishCity("Bydgoszcz", (53.1235, 18.0084), "Kuyavian-Pomeranian"),
    "Bialystok": PolishCity("Bialystok", (53.1325, 23.1688), "Podlaskie"),
    "Katowice": PolishCity("Katowice", (50.2649, 19.0238), "Silesian"),
    "Rzeszow": PolishCity("Rzeszow", (50.0413, 21.9990), "Subcarpathian"),
    "Olsztyn": PolishCity("Olsztyn", (53.7784, 20.4801), "Warmian-Masurian"),
    "Opole": PolishCity("Opole", (50.6751, 17.9213), "Opole"),
    "Zielona Gora": PolishCity("Zielona Gora", (51.9356, 15.5064), "Lubusz"),
    "Kielce": PolishCity("Kielce", (50.8661, 20.6286), "Swietokrzyskie")
}