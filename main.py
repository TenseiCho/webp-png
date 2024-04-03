import os
from PIL import Image

# Set the input and output folder paths
input_folder = "C:/Users/Carolina/Desktop/Images/Black Souls"
output_folder = "C:/Users/Carolina/Desktop/Images/Black Souls Completed"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        # Open the WebP image
        webp_path = os.path.join(input_folder, filename)
        image = Image.open(webp_path)

        # Convert the image to PNG format
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(output_folder, png_filename)
        image.save(png_path, "PNG")

        print(f"Converted {filename} to {png_filename}")

print("Conversion completed!")