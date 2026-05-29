#!/bin/bash
mkdir -p /logs/verifier

# Run the python suite via pytest
python3 -m pip install -q pytest
python3 -m pytest /tests/test_security.py

if [ $? -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi
