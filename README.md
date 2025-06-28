# Chat-BPT: Chat Bot of Polish Tourism

A simple Python-based console chatbot for Polish tourism.

## Features

- Interactive console-based chatbot
- Information about tourism options in Poland
- City-based recommendations
- Different tourism types (mountain, sea, cultural)
- Command system for easy navigation

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Running the Chatbot

1. Clone the repository:
   ```
   git clone https://github.com/BhdnFly/Chat-BPT.git
   cd Chat-BPT
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```
   make run
   ```

   Or directly with Python:
   ```
   python main.py
   ```

## Usage

### Available Cities

The chatbot currently supports the following cities:
- Warsaw
- Krakow
- Gdansk
- Lodz

Start by entering one of these cities to set your location.

### Tourism Types

After setting your city, you can explore these tourism types:
- mountain
- sea
- cultural

### Commands

The chatbot supports the following commands:

- `/help` - Display available commands
- `/city [name]` - Change your current city (e.g., `/city Lodz`)
- `/restart` - Reset the conversation
- `/info [attraction]` - Get detailed information about an attraction (e.g., `/info Manufaktura`)
- `/nearby [type]` - Find attractions of specific type near your current city (e.g., `/nearby cultural`)
- `/exit` or `/quit` - Exit the chatbot

### Example Interaction

```
> Warsaw
Great! I'll use Warsaw as your location. What type of tourism are you interested in? Options: mountain, sea, cultural

> cultural
Discover Poland's rich cultural heritage

For cultural tourism, we offer: museums, historical sites, theaters

Recommended for you: The Royal Castle and Old Town

> /nearby mountain
Nearby mountain attraction in Warsaw: Day trip to Kampinos National Park

> /info Royal Castle
The Royal Castle in Warsaw - former residence of Polish monarchs. Opening hours: 10:00-18:00, closed on Mondays. Located in the Old Town, Warsaw.

> /city Lodz
Your city has been changed to Lodz.

> /nearby cultural
Nearby cultural attraction in Lodz: Piotrkowska Street and Manufaktura - former factory complex turned cultural center
```

## Testing

Run the tests using the Makefile:

```
make test
```

Or use unittest directly:

```
python -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
