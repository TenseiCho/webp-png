import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
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
window.geometry("800x600")
window.configure(bg="#efe3d7")

# Load the logo image
logo_image = Image.open("logo.png")
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo
logo_label = tk.Label(window, image=logo_photo, bg="#efe3d7")
logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="#efe3d7")
button_frame.pack(side=tk.BOTTOM, pady=20)

# Create input folder selection button
input_folder_var = tk.StringVar()
input_folder_button = tk.Button(button_frame, text="Input Folder", command=select_input_folder, bg="#215b71", fg="white")
input_folder_button.pack(side=tk.LEFT, padx=10)

# Create output folder selection button
output_folder_var = tk.StringVar()
output_folder_button = tk.Button(button_frame, text="Output Folder", command=select_output_folder, bg="#215b71", fg="white")
output_folder_button.pack(side=tk.LEFT, padx=10)

# Create convert button
convert_button = tk.Button(button_frame, text="Convert Images", command=convert_images, bg="#215b71", fg="white")
convert_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
window.mainloop()