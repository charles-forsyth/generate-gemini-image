# generate-gemini-image Project Context

## Project Overview

**generate-gemini-image** is a modernized CLI tool designed for generating and editing images using Google's **Gemini 3 Pro** (Nano Banana Pro) models. It leverages the `google-genai` SDK to provide a robust interface for image synthesis, styling, and variation.

### Key Features
*   **Core Generation:** Text-to-image generation using `gemini-3-pro-image-preview`.
*   **Image Editing:** Inpainting and modification using reference images.
*   **Styling & Variations:** Built-in support for artistic styles (e.g., Cyberpunk, Oil Painting) and visual variations (e.g., Cinematic Lighting).
*   **Nano Banana Mode:** Strict adherence to image counts (one request per image iteration).
*   **Dual Authentication:** Supports both Google AI Studio API Keys and Google Cloud Vertex AI.
*   **Secure Config:** Uses `pydantic-settings` and restricted `.env` files for credentials.

## Architecture & Tech Stack

*   **Language:** Python 3.12+
*   **Package Manager:** `uv` (recommended)
*   **CLI Framework:** `typer`
*   **AI SDK:** `google-genai`
*   **Configuration:** `pydantic-settings`, `python-dotenv`
*   **Output:** `rich` for terminal output.

### Key Files
*   `src/generate_gemini_image/cli.py`: The main entry point using `typer`. Handles argument parsing and initialization.
*   `src/generate_gemini_image/core.py`: Contains the `ImageGenerator` class, which interacts with the `google-genai` client.
*   `src/generate_gemini_image/config.py`: Manages settings loading from environment variables and `.env` files.
*   `run_tests.sh`: A shell script for running functional CLI tests.

## Building and Running

### Installation
The project is designed to be installed as a tool using `uv`:

```bash
uv tool install .
```

To update:
```bash
uv tool update generate-gemini-image
```

### Configuration
Run the init command to generate the configuration file at `~/.config/generate-gemini-image/.env`:

```bash
generate-gemini-image init
```

### Usage
Run the CLI using the `generate-gemini-image` command:

```bash
# Basic generation
generate-gemini-image -p "A futuristic city"

# With styles and count
generate-gemini-image -p "A cat" --style "Watercolor" --count 2

# Image editing
generate-gemini-image -p "Add sunglasses" -i input.png
```

## Development & Testing

### Dependency Management
This project uses `uv` for dependency management.

```bash
# Install dependencies
uv sync

# Add a dependency
uv add package-name
```

### Running Tests
The project includes both unit tests (via `pytest`) and functional CLI tests.

**Unit Tests:**
```bash
uv run pytest
```

**Functional Tests:**
Execute the provided shell script to run a series of CLI commands:
```bash
./run_tests.sh
```

### Code Style & Linting
`ruff` is used for linting and formatting, configured in `pyproject.toml`.

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .
```

## Contribution Guidelines

*   **Strict Count:** When adding features, ensure the `--count` parameter is strictly respected (Nano Banana principle).
*   **Error Handling:** Use `typer.Exit(code=1)` for CLI errors and ensure logs are informative.
*   **Safety:** Default safety filters should be set to `BLOCK_ONLY_HIGH` unless configured otherwise.
