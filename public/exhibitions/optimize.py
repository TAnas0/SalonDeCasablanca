#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image

# Configuration
MAX_DIM = 800
WEBP_QUALITY = 70  # aggressive but still good quality
MIN_WEBP_SIZE = 110 * 1024  # only process WebP files >5 KB
TARGET_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
ROOT_DIR = Path('.')  # current directory
OUTPUT_DIR = Path('./webp')  # where WebP images will be saved

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)

def process_image(path: Path):
    try:
        if path.suffix.lower() == '.webp' and path.stat().st_size < MIN_WEBP_SIZE:
            print(f"Skipping small WebP: {path}")
            return
        print(f"Processing: {path}")
        with Image.open(path) as img:
            # Resize if necessary
            img.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)

            # Determine output WebP path (keep relative folder structure)
            relative_path = path.relative_to(ROOT_DIR)
            webp_path = OUTPUT_DIR / relative_path.with_suffix('.webp')
            webp_path.parent.mkdir(parents=True, exist_ok=True)

            # Save as WebP
            img.save(webp_path, 'WEBP', quality=WEBP_QUALITY, method=6, optimize=True)
            print(f"Saved WebP: {webp_path} (original size: {path.stat().st_size} bytes, webp size: {webp_path.stat().st_size} bytes)")

    except Exception as e:
        print(f"Failed to process {path}: {e}")

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower().endswith(TARGET_EXTENSIONS):
                path = Path(root) / file
                process_image(path)

if __name__ == "__main__":
    main()
