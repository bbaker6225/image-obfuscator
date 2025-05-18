# Image Obfuscation Tool

A lightweight Python utility for protecting privacy in images through noise addition and blurring. This tool is designed for quick and easy obfuscation of sensitive information in images.

## 🌟 Features

- 🔒 **EXIF Data Removal** - Strip potentially sensitive metadata from images
- 🌫 **Noise Addition** - Add customizable random noise to obscure details
- 🖼️ **Batch Processing** - Process entire directories

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-obfuscator.git
   cd image-obfuscator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Commands

```bash
# Add noise to images
python obfuscate_images.py input/ output/ --noise --noise_strength 30

# Apply blur
python obfuscate_images.py input/ output/ --blur --blur_radius 3

# Combine both effects
python obfuscate_images.py input/ output/ --noise --blur
```

### Parameters

- `input`: Path to input file or directory
- `output`: Output directory
- `--noise`: Add random noise
- `--blur`: Apply Gaussian blur
- `--noise_strength`: Intensity of noise (default: 20)
- `--blur_radius`: Blur radius (default: 2)

## Comparison with Other Tools

### vs Fawkes

| Feature | This Tool | Fawkes |
|---------|-----------|--------|
| Purpose | General image obfuscation | Face protection against facial recognition |
| Method | Noise, blur, EXIF removal | Neural network-based cloaking |
| Speed | Very fast | Slower (neural network processing) |
| Ease of Use | Simple CLI | Requires more setup |
| Protection | Visual obfuscation | AI-targeted protection |
| Best For | Quick privacy protection, batch processing | Strong protection against facial recognition |

### When to Use This Tool
- Quick obfuscation of sensitive information
- Batch processing multiple images
- When you need simple, explainable obfuscation

### When to Consider Fawkes
- Specifically protecting against facial recognition
- Need stronger AI-targeted protection
- Willing to trade speed for stronger protection

## Responsible Use

This tool is intended to help users protect their privacy and sensitive information in images. Please use it in accordance with all applicable laws and platform policies. The author does not condone or support malicious, unlawful, or deceptive uses of this software.
