import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import logic
import os
import configparser

def select_input_folder():
    input_folder = filedialog.askdirectory(title="Select Input Folder", initialdir=input_folder_var.get())
    if input_folder:
        input_folder_var.set(input_folder)
        save_config()

def select_output_folder():
    output_folder = filedialog.askdirectory(title="Select Output Folder", initialdir=output_folder_var.get())
    if output_folder:
        output_folder_var.set(output_folder)
        save_config()

def convert_images():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    converted_count = logic.convert_webp_to_png(input_folder, output_folder)
    messagebox.showinfo("Conversion Complete", f"Converted {converted_count} images.")

def load_config():
    if os.path.exists("config.ini"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        input_folder = config.get("Folders", "InputFolder", fallback="")
        output_folder = config.get("Folders", "OutputFolder", fallback="")
        input_folder_var.set(input_folder)
        output_folder_var.set(output_folder)

def save_config():
    config = configparser.ConfigParser()
    config.add_section("Folders")
    config.set("Folders", "InputFolder", input_folder_var.get())
    config.set("Folders", "OutputFolder", output_folder_var.get())
    with open("config.ini", "w") as config_file:
        config.write(config_file)

def on_enter(e):
    e.widget['background'] = '#3a7d95'  # Lighter shade for hover

def on_leave(e):
    e.widget['background'] = '#215b71'  # Original color

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
input_folder_button.bind("<Enter>", on_enter)
input_folder_button.bind("<Leave>", on_leave)

# Create output folder selection button
output_folder_var = tk.StringVar()
output_folder_button = tk.Button(button_frame, text="Output Folder", command=select_output_folder, bg="#215b71", fg="white")
output_folder_button.pack(side=tk.LEFT, padx=10)
output_folder_button.bind("<Enter>", on_enter)
output_folder_button.bind("<Leave>", on_leave)

# Create convert button
convert_button = tk.Button(button_frame, text="Convert Images", command=convert_images, bg="#215b71", fg="white")
convert_button.pack(side=tk.LEFT, padx=10)
convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Load the saved configuration
load_config()

# Run the main event loop
window.mainloop()