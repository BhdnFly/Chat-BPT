# Command processor for Chat-BPT

class CommandProcessor:
    """
    Processes commands for the chatbot
    """
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.commands = {
            '/help': self._help_command,
            '/city': self._city_command,
            '/restart': self._restart_command,
            '/info': self._info_command,
            '/nearby': self._nearby_command,
            '/exit': self._exit_command,
            '/quit': self._exit_command
        }

    def process_command(self, command_text):
        """
        Process a command and return a response

        Args:
            command_text (str): The command text including arguments

        Returns:
            str: The response to the command
        """
        # Split the command into the command name and arguments
        parts = command_text.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        # Check if the command exists
        if command in self.commands:
            return self.commands[command](args)

        return f"Unknown command: {command}. Type /help for available commands."

    def _help_command(self, args):
        """Handle the help command"""
        return "You can use the following commands: \n" \
               "/help - Display available commands \n" \
               "/city [name] - Change current city \n" \
               "/restart - Reset the conversation \n" \
               "/info [attraction] - Get detailed information about an attraction \n" \
               "/nearby [type] - Find attractions of specific type near current city \n" \
               "/exit or /quit - Exit the chatbot"

    def _city_command(self, args):
        """Handle the city command"""
        if not args:
            return "Please provide a city name. Usage: /city [name]"

        city_name = args.strip()
        if self.chatbot.validate_city(city_name):
            self.chatbot.set_city(city_name)
            return f"Your city has been changed to {city_name}."
        else:
            return f"Sorry, {city_name} is not a recognized city in our database."

    def _restart_command(self, args):
        """Handle the restart command"""
        self.chatbot.city = None
        self.chatbot.current_tourism = None
        return self.chatbot.get_greeting()

    def _info_command(self, args):
        """Handle the info command"""
        if not args:
            return "Please provide an attraction name. Usage: /info [attraction]"

        attraction_name = args.strip()

        # In a real implementation, this would look up the attraction in a database
        # For now, we'll provide some hardcoded information for a few attractions
        attractions = {
            "royal castle": "The Royal Castle in Warsaw - former residence of Polish monarchs. "
                           "Opening hours: 10:00-18:00, closed on Mondays. "
                           "Located in the Old Town, Warsaw.",
            "wawel castle": "Wawel Castle in Krakow - historic castle residency. "
                           "Opening hours: 9:00-17:00, open daily April-October. "
                           "Located on Wawel Hill in Krakow.",
            "sopot beach": "Sopot Beach - famous Baltic Sea beach with Europe's longest wooden pier. "
                          "Open 24/7, best visited during summer months. "
                          "Located in Sopot, near Gdansk.",
            "piotrkowska street": "Piotrkowska Street - the main street of Lodz and one of the longest commercial streets in Europe. "
                                 "Famous for its restaurants, bars, and beautiful architecture. "
                                 "Located in the center of Lodz.",
            "manufaktura": "Manufaktura - former factory complex turned into a shopping and entertainment center. "
                          "Opening hours: 10:00-22:00 daily. "
                          "Located in the heart of Lodz."
        }

        # Try to find the attraction by name (case insensitive)
        for name, info in attractions.items():
            if attraction_name.lower() in name:
                return info

        return f"Sorry, I don't have information about '{attraction_name}'. Please try another attraction."

    def _nearby_command(self, args):
        """Handle the nearby command"""
        if not args:
            return "Please provide a tourism type. Usage: /nearby [type]"

        if not self.chatbot.get_city():
            return "Please set your city first using /city [name] command."

        tourism_type = args.strip().lower()

        if tourism_type not in self.chatbot.get_tourism_types():
            return f"Unknown tourism type: {tourism_type}. Available types: {', '.join(self.chatbot.get_tourism_types())}"

        # Create tourism type object
        tourism_obj = self.chatbot.create_tourism_type(tourism_type)

        # Get recommendation using polymorphism
        recommendation = tourism_obj.recommend_attraction(self.chatbot.get_city())

        return f"Nearby {tourism_type} attraction in {self.chatbot.get_city()}: {recommendation}"

    def _exit_command(self, args):
        """Handle the exit command"""
        return "EXIT"
