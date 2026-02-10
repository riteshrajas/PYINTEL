import google.generativeai as genai
import os
import argparse
from PIL import Image

def generate_description(image_path, prompt):
    """
    Generates a description of an image based on a text prompt using the Gemini Pro Vision model.

    Args:
        image_path: Path to the image file.
        prompt: Text prompt to guide the description.

    Returns:
        The generated description string, or None if an error occurs.
    """
    try:
        # Load API key from environment variable
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("Error: GOOGLE_API_KEY environment variable not set.")
            return None

        genai.configure(api_key=api_key)

        # Create the model
        model = genai.GenerativeModel('gemini-pro-vision')

        # Load the image
        img = Image.open(image_path)

        # Generate content
        response = model.generate_content([prompt, img])

        return response.text

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a description for an image using Gemini Pro Vision.")
    parser.add_argument("image_path", help="Path to the image file.")
    parser.add_argument("prompt", help="Text prompt to guide the description.")

    args = parser.parse_args()

    description = generate_description(args.image_path, args.prompt)

    if description:
        print("\nGenerated Description:")
        print(description)
