#!/usr/bin/env python3
from html2image import Html2Image
from PIL import Image

# Initialize html2image
hti = Html2Image(output_path='/Users/noahbaragar/Desktop', size=(650, 900))

# Read the HTML file
with open('/Users/noahbaragar/Environmental friendly/wireframe.html', 'r') as f:
    html_content = f.read()

# Generate screenshot
hti.screenshot(html_str=html_content, save_as='water-wise-wireframe.png')

# Convert PNG to JPG
png_path = '/Users/noahbaragar/Desktop/water-wise-wireframe.png'
jpg_path = '/Users/noahbaragar/Desktop/water-wise-wireframe.jpg'

img = Image.open(png_path)
rgb_img = img.convert('RGB')
rgb_img.save(jpg_path, quality=95)

# Remove PNG
import os
os.remove(png_path)

print('✓ Wireframe saved as water-wise-wireframe.jpg on your Desktop!')
