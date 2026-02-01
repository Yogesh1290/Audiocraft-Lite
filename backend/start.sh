#!/bin/bash

# Start script for AudioCraft Lite Backend

echo "Starting AudioCraft Lite Backend..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create outputs directory
mkdir -p outputs

# Start the server
echo "Starting FastAPI server..."
python main.py
