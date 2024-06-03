import tkinter as tk
from tkinter import filedialog, messagebox
import main

def select_input_folder():
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    input_folder_var.set(input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(output_folder)

def convert_images():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    converted_count = main.convert_webp_to_png(input_folder, output_folder)
    messagebox.showinfo("Conversion Complete", f"Converted {converted_count} images.")

# Create the main window
window = tk.Tk()
window.title("WebP to PNG Converter")

# Set the window size to 1000x800 pixels
window.geometry("800x600")

# Create input folder selection button
input_folder_var = tk.StringVar()
input_folder_button = tk.Button(window, text="Select Input Folder", command=select_input_folder)
input_folder_button.pack(pady=10)

# Create output folder selection button
output_folder_var = tk.StringVar()
output_folder_button = tk.Button(window, text="Select Output Folder", command=select_output_folder)
output_folder_button.pack(pady=10)

# Create convert button
convert_button = tk.Button(window, text="Convert Images", command=convert_images)
convert_button.pack(pady=10)

# Run the main event loop
window.mainloop()