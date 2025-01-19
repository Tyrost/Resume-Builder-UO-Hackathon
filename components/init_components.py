import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from PIL import Image, ImageTk
from components.TextEditor import TextEditor
from components.Button import Button
 
# _______ Element Creation _______ #


def create_image(frame: tk.Frame, file_name, width=300, height=400):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    image_path = os.path.join(project_root, "components", "images", file_name)

    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    image = ImageTk.PhotoImage(resized_image)

    # Just create the Label; do NOT place/pack it here
    image_label = tk.Label(frame, image=image)
    # Keep a reference to avoid garbage-collection
    frame.image = image

    return image, image_label


def create_label(frame, text="", font=('Lexend', 15)):
    label = tk.Label(frame, text=text, font=font)
    return label


def create_button(frame, text, width=10, height=3, command=None):
    # Using your custom Button class (from components.Button).
    # Just create; do not pack/place here.
    btn = Button(frame, label=text, width=width, height=height, command=command)
    return btn


def create_textbox(parent, placeholder_text='Job description:',
                   width='50', height='20', font=("Arial", 14)):
    editor = TextEditor(parent, placeholder_text, width, height, font)
    return editor


def create_elements(parent, file_name, width = '50', height = '20'):
    # Example function that returns an image label + a textbox
    _, img_label = create_image(parent, file_name)
    editor = create_textbox(parent, width=width, height=height)
    return img_label, editor