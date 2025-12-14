import datetime
import re
from pathlib import Path


def sanitize_filename(prompt: str, extension: str = "png") -> str:
    """Sanitizes a prompt to create a safe filename."""
    # Remove non-alphanumeric characters except spaces and hyphens
    sanitized = re.sub(r"[^\w\s-]", "", prompt).strip()
    # Replace spaces and hyphens with underscores
    sanitized = re.sub(r"[-\s]+", "_", sanitized)
    # Truncate
    sanitized = sanitized[:50]
    # Add timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{sanitized}_{timestamp}.{extension}"

def ensure_directory(path: Path):
    """Ensures a directory exists."""
    path.mkdir(parents=True, exist_ok=True)
