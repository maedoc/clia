#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null
then
    echo "uv could not be found. Please install uv (e.g., pip install uv) to proceed."
    exit 1
fi

# Define the virtual environment directory
CLIA_DIR=$HOME/src/clia
VENV_DIR="$CLIA_DIR/.venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment with uv..."
    uv venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

source $VENV_DIR/bin/activate

# Activate the virtual environment and install requirements
uv pip install -r $CLIA_DIR/requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install requirements."
    exit 1
fi

# Run the agent_cli.py script
uv run python $CLIA_DIR/agent_cli.py --config-dir $CLIA_DIR "$@"
