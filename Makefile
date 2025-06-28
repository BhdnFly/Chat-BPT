# Makefile for Chat-BPT project

.PHONY: run test clean help

# Python interpreter
PYTHON = python

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available commands:"
	@echo "  make run       - Run the chatbot"
	@echo "  make test      - Run all tests"
	@echo "  make clean     - Remove Python cache files"
	@echo "  make help      - Show this help message"

# Run the chatbot
run:
	$(PYTHON) main.py

# Run all tests
test:
	$(PYTHON) -m unittest discover tests

# Run chatbot tests only
test-chat:
	$(PYTHON) -m unittest tests.test_chatbot

# Run tourism tests only
test-tour:
	$(PYTHON) -m unittest tests.test_tourism

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
