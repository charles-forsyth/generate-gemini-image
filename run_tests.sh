#!/bin/bash
set -e

echo "=== Gemini CLI Test Suite ==="
echo "Updating tool..."
uv tool update generate-gemini-image

echo -e "\n\n--- Test 1: Basic Generation ---"
generate-gemini-image -p "A futuristic brave new world, highly detailed"

echo -e "\n\n--- Test 2: Advanced Parameters (16:9, 2K, Count 2) ---"
generate-gemini-image -p "A cinematic shot of a space station" \
    --aspect-ratio "16:9" \
    --image-size "2K" \
    --count 2

echo -e "\n\n--- Test 3: Piping from Stdin ---"
echo "A cyberpunk street vendor selling tacos, neon lights" | generate-gemini-image

echo -e "\n\n--- Test 4: Styling & Negative Prompts ---"
generate-gemini-image -p "A portrait of a wizard" \
    --style "oil painting" \
    --variation "moody lighting" \
    --negative-prompt "hats, wands"

echo -e "\n\n--- Test 5: Image Editing Workflow ---"
echo "Generating base image..."
# Use explicit filename for predictable testing
generate-gemini-image -p "A simple white cube on a wooden table" --filename "base_cube.png"

# Path is output_dir/filename (default output dir is ~/Pictures/Gemini_Generated)
BASE_IMG=~/Pictures/Gemini_Generated/base_cube.png
echo "Base image created: $BASE_IMG"

echo "Editing image..."
generate-gemini-image -p "Turn the cube into a block of melting ice" -i "$BASE_IMG"

echo -e "\n\n--- Test 6: Help Command (-h) ---"
generate-gemini-image -h

echo -e "\n\n=== All Tests Completed Successfully! ==="
