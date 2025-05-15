#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 -n <env_name>"
    exit 1
}

# Parse command-line arguments
while getopts "n:" opt; do
    case $opt in
        n)
            ENV_NAME=$OPTARG
            ;;
        *)
            usage
            ;;
    esac
done

# Check if ENV_NAME is set
if [ -z "$ENV_NAME" ]; then
    echo "Error: Environment name is required."
    usage
fi

# Create conda environment
echo "Creating conda environment: $ENV_NAME"
conda create -y -n "$ENV_NAME" python=3.10

# Activate environment
echo "Activating environment: $ENV_NAME"
# For bash, use conda's recommended activation command
eval "$(conda shell.bash hook)"
conda activate "$ENV_NAME"

# Install pytorch (cuda=12.4)
echo "Installing pytorch"
conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.4 -c pytorch -c nvidia -y

# Upgrade pip
echo "Upgrading pip"
pip install --upgrade pip

# Install Genesis from GitHub
echo "Installing Genesis from GitHub"
pip install git+https://github.com/Genesis-Embodied-AI/Genesis.git

# Install current directory in editable mode
echo "Installing current directory in editable mode"
pip install -e .

echo "Setup complete."

