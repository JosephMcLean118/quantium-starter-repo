#!/bin/bash

echo "AUTOMATED TESTING SCRIPT"

# activate the virtual environment
source venv/bin/activate

echo "VIRTUAL ENVIRONMENT ACTIVATED"


# execute test suite
pytest

# check if pytest was successful
pytest && exit 0 || exit 1