import os
import argparse
import cv2
import numpy as np
import piexif
from PIL import Image, ImageFilter
from tqdm import tqdm
from typing import List


DEFAULT_NOISE_STRENGTH = 20
DEFAULT_BLUR_RADIUS = 2


def remove_exif(image_path: str) -> None:
    try:
        piexif.remove(image_path)
    except Exception as e:
        print(f"Failed to remove EXIF from {image_path}: {e}")


def add_noise(image_path: str, output_path: str, strength: int = DEFAULT_NOISE_STRENGTH) -> None:
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read {image_path}")
        return
    noise = np.random.randint(-strength, strength, image.shape, dtype='int16')
    noisy_image = np.clip(image.astype('int16') + noise, 0, 255).astype('uint8')
    cv2.imwrite(output_path, noisy_image)


def blur_image(image_path: str, output_path: str, radius: int = DEFAULT_BLUR_RADIUS) -> None:
    img = Image.open(image_path)
    img = img.filter(ImageFilter.GaussianBlur(radius=radius))
    img.save(output_path)


def process_images(
    input_paths: List[str],
    output_dir: str,
    noise: bool,
    blur: bool,
    noise_strength: int = DEFAULT_NOISE_STRENGTH,
    blur_radius: int = DEFAULT_BLUR_RADIUS
) -> None:
    os.makedirs(output_dir, exist_ok=True)
    for img_path in tqdm(input_paths, desc="Processing images"):
        basename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, basename)

        # If both are selected, do noise then blur
        temp_path = output_path + ".temp.jpg"

        if noise and blur:
            add_noise(img_path, temp_path, strength=noise_strength)
            blur_image(temp_path, output_path, radius=blur_radius)
            os.remove(temp_path)
            remove_exif(output_path)
        elif noise:
            add_noise(img_path, output_path, strength=noise_strength)
            remove_exif(output_path)
        elif blur:
            blur_image(img_path, output_path, radius=blur_radius)
            remove_exif(output_path)


def get_image_paths(input_path: str) -> List[str]:
    # Single file or directory
    if os.path.isfile(input_path):
        return [input_path]
    elif os.path.isdir(input_path):
        supported = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
        return [os.path.join(input_path, f) for f in os.listdir(input_path)
                if f.lower().endswith(supported)]
    else:
        raise ValueError("Input path must be an image file or directory")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch obfuscate images with noise and/or blur.")
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("output", help="Output directory")
    parser.add_argument("--noise", action="store_true", help="Add random noise")
    parser.add_argument("--blur", action="store_true", help="Apply Gaussian blur")
    parser.add_argument("--noise_strength", type=int, default=DEFAULT_NOISE_STRENGTH, help="Strength of random noise")
    parser.add_argument("--blur_radius", type=int, default=DEFAULT_BLUR_RADIUS, help="Gaussian blur radius")
    args = parser.parse_args()

    if not (args.noise or args.blur):
        parser.error("You must specify at least --noise or --blur.")

    image_paths = get_image_paths(args.input)
    if not image_paths:
        print("No images found to process.")
    else:
        process_images(
            image_paths,
            args.output,
            noise=args.noise,
            blur=args.blur,
            noise_strength=args.noise_strength,
            blur_radius=args.blur_radius
        )
        print(f"Processed {len(image_paths)} image(s). Output saved to: {args.output}")
