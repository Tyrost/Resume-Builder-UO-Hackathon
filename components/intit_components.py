import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from PIL import Image, ImageTk
from components.TextEditor import TextEditor
from components.Button import Button
 
# _______ Element Creation _______ #

def create_image(frame: tk.Frame, file_name, width = 300, height = 400):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    image_path = os.path.join(project_root, "components", "images", f"{file_name}")

    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    image = ImageTk.PhotoImage(resized_image)

    image_label = tk.Label(frame, image=image)
    image_label.pack()

    frame.image = image
    return image, image_label

def create_label(frame, text = "", font = ('Lexend', 15)):
    label = tk.Label(frame, text=text, font=font)
    label.pack()
    
    return label

def create_button(frame, label, width = 10, height=3, command=None):
    btn = Button(frame, label=label, width=width, height=height)
    btn.pack()
    
    return btn
    
def create_textbox(window, placeholder_text='Job description:', width='50', height='20', font = ("Arial", 14)):
    editor = TextEditor(window, placeholder_text, width, height, font) # MISSING FONT
    editor.pack()
    return editor

def create_elements(window, frame, file_name):
    null, img_label = create_image(frame, file_name)
    editor = create_textbox(window)
    
    return img_label, editor