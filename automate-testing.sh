#!/bin/bash

echo "AUTOMATED TESTING SCRIPT"

# activate the virtual environment
. ./venv/bin/activate

echo "VIRTUAL ENVIRONMENT ACTIVATED"

# execute test script and check if pytest was successful
pytest && exit 0 || exit 1