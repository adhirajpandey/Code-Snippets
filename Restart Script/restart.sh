#!/bin/bash

# Define a variable for the Python file name
PYTHON_FILE="<your_flask_app>.py"
PROJECT_DIR="<your_project_directory>"

# Add sleep to let machine connect to network properly
sleep 10

# Change working directory to the project directory
cd $PROJECT_DIR

# Activate the virtual environment
source venv/bin/activate


# Check if the Flask server process is running
if ps aux | grep -v grep | grep "python3 $PYTHON_FILE" >/dev/null; then
    # Flask server process is running, capture its PID
    pid=$(ps aux | grep -v grep | grep "python3 $PYTHON_FILE" | awk '{print $2}')

    echo "Flask Server already running, PID is: $pid"
    sudo kill -9 $pid

    echo "Process killed successfully."
else
    echo "No already running process found."
fi

# run flask app using nohup command to save terminal logs in nohup.out file
nohup python3 $PYTHON_FILE >> nohup.out 2>&1 &

echo "New Flask Server started successfully."