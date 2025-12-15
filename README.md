# Modernized Gemini Image Generation CLI

A robust, secure, and distribution-ready CLI tool for generating and editing images using Google's **Gemini 3 Pro** (aka Nano Banana Pro) models.

## Features

*   **Gemini 3 Pro**: Uses the latest `gemini-3-pro-image-preview` model via `google-genai` SDK.
*   **Image Editing**: Modify existing images or create composites using reference images (`--image`).
*   **Dual Auth**: Support for both **API Key** (Google AI Studio) and **Vertex AI** (GCP).
*   **Flexible CLI**: Support for named arguments (`--prompt`), piping from stdin (`|`), and rich output.
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

This will create `~/.config/generate-gemini-image/.env`. **Edit this file to set your authentication:**

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

## Usage Examples

### 1. Basic Generation
Generate a single image with default settings.
```bash
generate-gemini-image -p "A futuristic city on Mars"
```

### 2. Image Editing & Inpainting
Modify an existing image by providing it as context.
```bash
generate-gemini-image -p "Add a red hat to the cat" -i cat.png
```

### 3. Multi-Image Composition
Combine elements from multiple images.
```bash
generate-gemini-image -p "Combine the style of image 1 with the subject of image 2" \
    -i style_ref.png -i subject_ref.png
```

### 4. Piping from Stdin
Great for chaining commands or reading from files.
```bash
echo "A cyberpunk street food vendor" | generate-gemini-image
```

### 5. High Resolution & Styles
Generate a 4K, 16:9 cinematic image with specific styles.
```bash
generate-gemini-image -p "Space battle fleet" \
    --aspect-ratio "16:9" \
    --image-size "4K" \
    --style "cinematic" --variation "dramatic"
```

## Configuration Reference (`.env`)

| Setting | Description | Default |
| :--- | :--- | :--- |
| `API_KEY` | Google AI Studio Key | None |
| `PROJECT_ID` | GCP Project ID | None |
| `MODEL_NAME` | Model ID | `gemini-3-pro-image-preview` |
| `OUTPUT_DIR` | Output folder | `~/Pictures/Gemini_Generated` |
| `ASPECT_RATIO` | Default shape | `1:1` |
| `IMAGE_SIZE` | Resolution (`1K`, `2K`, `4K`) | `1K` |
| `SAFETY_FILTER_LEVEL` | Content filtering (`BLOCK_NONE`, `BLOCK_ONLY_HIGH`) | `BLOCK_ONLY_HIGH` |

## License

Private / Internal Use.