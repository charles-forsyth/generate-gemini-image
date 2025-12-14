# Modernized Gemini Image Generation CLI

A robust, secure, and distribution-ready CLI tool for generating images using Google's Vertex AI (Gemini/Imagen models), including support for "Nano Banana" specific enhancements.

## Features

*   **Modern CLI**: Built with `typer` and `rich` for a great user experience.
*   **Secure Configuration**: Uses `pydantic-settings` to load credentials from environment variables (`.env` support).
*   **Latest API Support**: Compatible with Vertex AI `ImageGenerationModel` (Imagen 3 / Gemini Image).
*   **Nano Banana Enhancements**: Strict count adherence, style/variation prompt augmentation.
*   **Reproducible**: Managed with `uv` and `pyproject.toml`.
*   **Quality**: Enforced by `ruff` and `pytest`.

## Installation

### Using `uv` (Recommended)

You can install this tool directly from the repository:

```bash
uv tool install git+https://github.com/charles-forsyth/generate-gemini-image.git
```

To update later:

```bash
uv tool update generate-gemini-image
```

### Initial Setup

After installation, run the initialization command to create your secure configuration file:

```bash
generate-gemini-image init
```

This will create `~/.config/generate-gemini-image/.env`. **You must edit this file to set your `PROJECT_ID`.**

### Development Setup

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:charles-forsyth/generate-gemini-image.git
    cd generate-gemini-image
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    ```

3.  **Run Tests:**
    ```bash
    uv run pytest
    ```

## Configuration

The application looks for configuration in the following order:
1.  Command-line arguments (e.g., `--project-id`).
2.  Environment variables (e.g., `PROJECT_ID`).
3.  `.env` file in the current directory.
4.  `.env` file in `~/.config/generate-gemini-image/.env`.
5.  Google Application Default Credentials (ADC) for Project ID.

### Environment Variables

*   `PROJECT_ID`: Google Cloud Project ID.
*   `LOCATION`: GCP Location (default: `us-central1`).
*   `MODEL_NAME`: Vertex AI Model Name (default: `gemini-2.5-flash-image` or `imagen-3.0-generate-001`).
*   `OUTPUT_DIR`: Default output directory.

## Usage

```bash
# Basic Generation
generate-gemini-image "A futuristic city on Mars"

# With Nano Banana Styles & Variations
generate-gemini-image "A cat sitting on a fence" \
    --count 2 \
    --style "cyberpunk" --style "neon" \
    --variation "night time"

# Specify Project and Model
generate-gemini-image "Test prompt" \
    --project-id "my-project-id" \
    --model-name "imagen-3.0-generate-001"
```

## "Nano Banana" Compliance

This tool adheres to the Nano Banana guidelines:
*   **Strict Count**: `--count=N` generates exactly N images.
*   **Styles/Variations**: Appended to the prompt to guide the model.

## License

Private / Internal Use.
