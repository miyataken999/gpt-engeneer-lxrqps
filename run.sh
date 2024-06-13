#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app/__main__.py

# Run the tests
python -m unittest discover -v tests
