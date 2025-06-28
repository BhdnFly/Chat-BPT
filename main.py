#!/usr/bin/env python3
"""
Chat-BPT - Chat Bot of Polish Tourism
"""
from tourism import create_tourism_type
from commands import CommandProcessor


class ChatBot:
    """Simple chatbot for Polish tourism"""
    def __init__(self):
        self.city = None
        self.valid_cities = ["Warsaw", "Krakow", "Gdansk", "Lodz"]
        self.tourism_types = ["mountain", "sea", "cultural"]
        self.current_tourism = None

    def get_greeting(self):
        return "Welcome to Chat-BPT! Please tell me which city in Poland you are in. \n" \
               "Example: > Lodz \n" \
               "\n" \
               "You can use the following commands: \n" \
               "/help - Display available commands \n" \
               "/city [name] - Change current city \n" \
               "/restart - Reset the conversation \n" \
               "/info [attraction] - Get detailed information about an attraction \n" \
               "/nearby [type] - Find attractions of specific type near current city \n" \
               "/exit or /quit - Exit the chatbot"

    def set_city(self, city_name):
        self.city = city_name

    def get_city(self):
        return self.city

    def validate_city(self, city_name):
        return city_name in self.valid_cities

    def get_tourism_types(self):
        return self.tourism_types

    def get_tourism_subtypes(self, tourism_type):
        tourism_obj = create_tourism_type(tourism_type)
        return tourism_obj.get_subtypes()

    def create_tourism_type(self, type_name):
        """Create a tourism type object using the factory function"""
        return create_tourism_type(type_name)

    def process_input(self, user_input):
        if user_input in self.valid_cities:
            self.set_city(user_input)
            return f"Great! I'll use {user_input} as your location. What type of tourism are you interested in? Options: {', '.join(self.tourism_types)}"

        if user_input in self.tourism_types:
            self.current_tourism = self.create_tourism_type(user_input)
            description = self.current_tourism.get_description()
            subtypes = self.current_tourism.get_subtypes()

            response = f"{description}\n\nFor {user_input} tourism, we offer: {', '.join(subtypes)}"

            if self.city:
                recommendation = self.current_tourism.recommend_attraction(self.city)
                response += f"\n\nRecommended for you: {recommendation}"

            return response

        return "I'm not sure what you mean. Please enter a valid city or tourism type."


def main():
    """Run the chatbot"""
    chatbot = ChatBot()
    command_processor = CommandProcessor(chatbot)
    print(chatbot.get_greeting())

    while True:
        try:
            user_input = input("> ")
            if user_input.startswith('/'):
                response = command_processor.process_command(user_input)
                if response == "EXIT":
                    print("Goodbye. Enjoy your trip!")
                    break
            else:
                response = chatbot.process_input(user_input)

            print(response)

        except KeyboardInterrupt:
            print("\nGoodbye. Enjoy your trip!")
            break


if __name__ == "__main__":
    main()
