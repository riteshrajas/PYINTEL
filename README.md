# Gemini Pro Vision Python Example

This project demonstrates how to use the Google Gemini Pro Vision model with Python to get descriptions for images based on text prompts.

## Project Description

The core application in `gemini_app/main.py` takes a path to an image file and a text prompt as input. It then uses the Gemini Pro Vision multimodal model to generate a textual description of the image, guided by the provided prompt.

## Features

-   Command-line interface.
-   Uses the `google-generativeai` SDK.
-   Loads Google API Key from the `GOOGLE_API_KEY` environment variable.
-   Provides error handling for common issues (API key, file loading).
-   Includes an example script and sample image.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    (Replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name)

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Make sure you have Python 3.7+ installed.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### 1. Set the GOOGLE_API_KEY

You need a Google API key with the Generative Language API (Gemini API) enabled.
Set it as an environment variable:

```bash
export GOOGLE_API_KEY='YOUR_API_KEY_HERE'
```
Replace `YOUR_API_KEY_HERE` with your actual API key.

**Important:** Keep your API key confidential. Do not commit it to your repository.

### 2. Using the Example Script

The easiest way to test the application is with the provided example script:

```bash
sh examples/run_example.sh
```
This script will use the `examples/sample_image.jpg` and a default prompt.

### 3. Running `main.py` Directly

You can also run the main application script directly with your own image and prompt:

```bash
python3 gemini_app/main.py "path/to/your/image.jpg" "Your descriptive prompt here"
```

For example:
```bash
python3 gemini_app/main.py examples/sample_image.jpg "What animal is in this picture?"
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the terms of the LICENSE file.
(Note: A LICENSE file was present but its content was not specified in this task. Assuming it's a standard one like MIT, Apache 2.0, etc.)