#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path

from html2image import Html2Image
from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture a full-page screenshot of an HTML file.")
    parser.add_argument(
        "--html",
        default="/Users/noahbaragar/Environmental friendly/index.html",
        help="Absolute path to the HTML file to capture.",
    )
    parser.add_argument(
        "--output-dir",
        default="/Users/noahbaragar/Desktop",
        help="Directory to save the screenshot.",
    )
    parser.add_argument(
        "--name",
        default="water-wise-full",
        help="Base filename for the output image (without extension).",
    )
    parser.add_argument("--width", type=int, default=1200, help="Viewport width in pixels.")
    parser.add_argument("--height", type=int, default=2600, help="Viewport height in pixels.")
    return parser.parse_args()


def capture_full_page(html_path: Path, output_dir: Path, base_name: str, width: int, height: int) -> Path:
    hti = Html2Image(output_path=str(output_dir), size=(width, height))
    png_name = f"{base_name}.png"
    hti.screenshot(html_file=str(html_path), save_as=png_name)

    png_path = output_dir / png_name
    jpg_path = output_dir / f"{base_name}.jpg"

    img = Image.open(png_path)
    rgb_img = img.convert("RGB")
    rgb_img.save(jpg_path, quality=95)

    os.remove(png_path)
    return jpg_path


def main() -> None:
    args = parse_args()
    html_path = Path(args.html).expanduser()
    output_dir = Path(args.output_dir).expanduser()

    output_dir.mkdir(parents=True, exist_ok=True)
    jpg_path = capture_full_page(html_path, output_dir, args.name, args.width, args.height)
    print(f"✓ Screenshot saved as {jpg_path}")


if __name__ == "__main__":
    main()
