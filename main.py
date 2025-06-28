#!/usr/bin/env python3
"""
Chat-BPT - Chat Bot of Polish Tourism
"""

class ChatBot:
    """Simple chatbot for Polish tourism"""
    def __init__(self):
        self.city = None
        self.valid_cities = ["Warsaw", "Krakow", "Gdansk"]
        self.tourism_types = ["mountain", "sea", "cultural"]

    def get_greeting(self):
        return "Welcome to Chat-BPT! Please tell me which city in Poland you are in."

    def set_city(self, city_name):
        self.city = city_name

    def get_city(self):
        return self.city

    def validate_city(self, city_name):
        return city_name in self.valid_cities

    def get_tourism_types(self):
        return self.tourism_types

    def get_tourism_subtypes(self, tourism_type):
        subtypes = {
            "mountain": ["hiking", "climbing", "skiing"],
            "sea": ["beaches", "sailing", "diving"],
            "cultural": ["museums", "historical sites", "theaters"]
        }
        return subtypes.get(tourism_type, [])

    def process_input(self, user_input):
        if user_input in self.valid_cities:
            self.set_city(user_input)
            return f"Great! I'll use {user_input} as your location. What type of tourism are you interested in? Options: {', '.join(self.tourism_types)}"

        if user_input in self.tourism_types:
            subtypes = self.get_tourism_subtypes(user_input)
            return f"For {user_input} tourism, we offer: {', '.join(subtypes)}"

        return "I'm not sure what you mean. Please enter a valid city or tourism type."


def main():
    """Run the chatbot"""
    chatbot = ChatBot()
    print(chatbot.get_greeting())

    while True:
        try:
            user_input = input("> ")

            if user_input.lower() in ['/exit', '/quit']:
                print("Goodbye!")
                break

            response = chatbot.process_input(user_input)
            print(response)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
