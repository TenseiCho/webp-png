import os
from PIL import Image

def convert_webp_to_png(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    converted_count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(input_folder, filename)
            image = Image.open(webp_path)

            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)
            image.save(png_path, "PNG")

            converted_count += 1

    return converted_count