#!/bin/bash

# Check if GOOGLE_API_KEY is set
if [ -z "$GOOGLE_API_KEY" ]; then
  echo "Error: The GOOGLE_API_KEY environment variable is not set."
  echo "Please set it before running the example:"
  echo "export GOOGLE_API_KEY='your_api_key_here'"
  exit 1
fi

# Define the image path and prompt
IMAGE_PATH="examples/sample_image.jpg"
PROMPT="Describe this image in detail."

# Check if the image file exists
if [ ! -f "$IMAGE_PATH" ]; then
  echo "Error: Sample image not found at $IMAGE_PATH"
  echo "Please make sure the image exists or run the image download command again."
  exit 1
fi

# Run the main application
echo "Running the Gemini Pro Vision application..."
python3 gemini_app/main.py "$IMAGE_PATH" "$PROMPT"

echo ""
echo "Example finished."
