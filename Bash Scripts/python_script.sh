#!/bin/bash

# Define a variable for the Python file name
PYTHON_FILE_1="python_file1.py"
PYTHON_FILE_2="python_file2.py"
PROJECT_DIR="/path/of/project/dir"

# Add sleep to let machine connect to network properly
sleep 3

# Change working directory to the project directory
cd $PROJECT_DIR

# Activate the virtual environment
source venv/bin/activate

# Run Python Scripts
nohup python3 $PYTHON_FILE_1 >> nohup.out 2>&1 &

sleep 3

nohup python3 $PYTHON_FILE_2 >> nohup.out 2>&1 &

echo "Python File executed successfully"