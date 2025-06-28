# The entry point of the application Chat-BPT (Chat Bot of Polish Tourism)

from tourism import create_tourism_type


class ChatBot:
    """Simple chatbot for Polish tourism"""
    def __init__(self):
        self.city = None
        self.valid_cities = ["Warsaw", "Krakow", "Gdansk"]
        self.tourism_types = ["mountain", "sea", "cultural"]
        self.current_tourism = None

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
        # Use polymorphism to get subtypes
        tourism_obj = create_tourism_type(tourism_type)
        return tourism_obj.get_subtypes()

    def process_input(self, user_input):
        if user_input in self.valid_cities:
            self.set_city(user_input)
            return f"Great! I'll use {user_input} as your location. What type of tourism are you interested in? Options: {', '.join(self.tourism_types)}"

        if user_input in self.tourism_types:
            # Use polymorphism to create the appropriate tourism type
            self.current_tourism = create_tourism_type(user_input)

            # Get description and recommendation using polymorphic methods
            description = self.current_tourism.get_description()
            subtypes = self.current_tourism.get_subtypes()

            response = f"{description}\n\nFor {user_input} tourism, we offer: {', '.join(subtypes)}"

            # If city is set, add a recommendation
            if self.city:
                recommendation = self.current_tourism.recommend_attraction(self.city)
                response += f"\n\nRecommended for you: {recommendation}"

            return response

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
