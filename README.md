# Modernized Gemini Image Generation CLI

A robust, secure, and distribution-ready CLI tool for generating images using Google's Gemini 3 Pro (Nano Banana Pro) models.

## Features

*   **Gemini 3 Pro**: Uses the latest `gemini-3-pro-image-preview` model via `google-genai`.
*   **Dual Auth**: Support for both **API Key** (Google AI Studio) and **Vertex AI** (GCP).
*   **Nano Banana Enhancements**: Strict count adherence, style/variation prompt augmentation.
*   **Secure Configuration**: Uses `pydantic-settings` to load credentials from environment variables (`.env` support).
*   **Reproducible**: Managed with `uv` and `pyproject.toml`.

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

This will create `~/.config/generate-gemini-image/.env`. **Edit this file to set your authentication: **

**Option A: API Key (Simpler)**
Get a key from [Google AI Studio](https://aistudio.google.com/).
```env
API_KEY=your_api_key_here
```

**Option B: Vertex AI (Enterprise)**
Use your Google Cloud Project.
```env
PROJECT_ID=your_gcp_project_id
```

## Usage

```bash
# Basic Generation
generate-gemini-image generate "A futuristic city on Mars"

# With Nano Banana Styles & Variations
generate-gemini-image generate "A cat sitting on a fence" \
    --count 2 \
    --style "cyberpunk" --style "neon" \
    --variation "night time"

# Override Auth
generate-gemini-image generate "Test prompt" --api-key "AIzaSy..."
```

## License

Private / Internal Use.