import logging as log
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.main import create_window
import tkinter as tk
from PIL import Image, ImageTk
from components.Button import Button


WINDOW = tk.Tk()
frame = create_window(WINDOW, "ResumAI", 800, 1200)

def create_label(frame, text, font, row, column, padx=20, pady=10, sticky="w", wraplength=None):
    """
    Creates a label widget and places it on the specified frame with the given grid parameters.

    Parameters:
        frame (tk.Frame): The Tkinter frame where the label will be placed.
        text (str): The text to display on the label.
        font (tuple): The font of the label (e.g., ("Times New Roman", 14)).
        row (int): The row in the grid where the label should be placed.
        column (int): The column in the grid where the label should be placed.
        padx (int): Horizontal padding around the label. Default is 20.
        pady (int): Vertical padding around the label. Default is 10.
        sticky (str): The alignment of the label within the grid cell. Default is "w" (west/left).
        wraplength (int or None): The maximum line width for wrapping text (in pixels). Default is None (no wrapping).
    """
    label = tk.Label(frame, text=text, font=font, wraplength=wraplength)
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return label

description= (
    "Welcome to ResumAI - Your AI - Powered Resume Assistant!\n\n"
    "At ResumAI, we leverage the power of AI to help you craft or update your resume with ease.\n\n"
    "Whether you're starting from scratch or looking to revise an existing document, our intelligent\n\n"
    "assistant guides you every step of the way. With tailored suggestions, industry-specific templates,\n\n "
    "expert formatting tips, you can create a professional resume that stands out. Let our AI help you\n\n "
    "highlight your skills, experience, and accomplishments, ensuring that your resume is polished and ready\n\n"
    "for your next career opportunity.\n\n"
)

create_label(frame, "ResumAI", ("Times New Roman", 60), 0, 0, pady=0, sticky="w")
create_label(frame, description, ("Times New Roman", 14), 1, 1, padx=100, pady=0, sticky="e", wraplength=700)
create_label(frame, "Upload Your Resume For Revision", ("Times New Roman", 22), 1, 0, pady=0, sticky="w")
create_label(frame, "Build Your Resume Here", ("Times New Roman", 22), 3, 0, pady=0, sticky="w")

def create_image(frame: tk.Frame, row, column, width=300, height=400, padx=20, pady=10, sticky="w"):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    image_path = os.path.join(project_root, "components", "images", "PDF.png")

    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    image = ImageTk.PhotoImage(resized_image)

    image_label = tk.Label(frame, image=image)
    image_label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

    frame.image = image
    return image, image_label

create_image(frame, row=3, column=1, width=200, height=300, padx=300, pady=0, sticky="e")

upload_button = Button(
        frame,
        label="Upload",
        height=50,
        width=20,
        defcolor="green",
        optcolor="lightgreen"
    )
upload_button.grid(row=2, column=0, pady=0, padx=120, sticky="w")

create_button = Button(
        frame,
        label="Create",
        height=50,
        width=20,
        defcolor="green",
        optcolor="lightgreen")

create_button.grid(row=4, column=0, pady=0, padx=120, sticky="w")

WINDOW.mainloop()