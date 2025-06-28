# Chat-BPT: Chat Bot of Polish Tourism

A simple Python-based console chatbot for Polish tourism.

## Features

- Interactive console-based chatbot
- Information about tourism options in Poland
- City-based recommendations
- Different tourism types (mountain, sea, cultural)

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Running the Chatbot

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Chat-BPT.git
   cd Chat-BPT
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```
   python main.py
   ```

## Usage

- Start by entering a Polish city
- Choose a tourism type you're interested in
- Use commands like `/help` to see available options
- Use `/city [name]` to change your current city
- Use `/exit` or `/quit` to exit the program

## Testing

Run the tests using the Makefile:

```
make test          # Run all tests
```

Or use unittest directly:

```
python -m unittest discover tests
```

## Running the Chatbot

You can run the chatbot using the Makefile:

```
make run
```

Or directly with Python:

```
python main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
