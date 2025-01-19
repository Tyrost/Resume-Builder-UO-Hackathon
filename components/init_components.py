import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from PIL import Image, ImageTk
from components.TextEditor import TextEditor
from components.Button import Button
 
import fitz
 
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


def create_elements(parent, width='50', height='20'):
    """
    Creates and returns an image label and a text editor.
    If a resume PDF is uploaded, it generates a preview of the first page.
    Otherwise, it uses a default image.

    :param parent: The parent widget (e.g., frame or window).
    :param width: Width of the text editor.
    :param height: Height of the text editor.
    :return: (img_label, text_editor)
    """
    # Paths
    pdf_path = os.path.abspath('PDFs/file.pdf')  # Path to uploaded PDF
    preview_image_path = os.path.abspath('components/images/preview.jpg')  # Path to save preview image

    # Generate image preview if PDF exists
    image_to_display = preview_image_path  # Default to sample image
    if os.path.exists(pdf_path):
        try:
            # Open the PDF and render the first page
            pdf_document = fitz.open(pdf_path)
            page = pdf_document.load_page(0)  # Load the first page
            pix = page.get_pixmap()  # Render the page to an image
            pix.save(preview_image_path)  # Save as PNG
            pdf_document.close()
            image_to_display = preview_image_path  # Use the generated preview image
        except Exception as e:
            print(f"Failed to generate PDF preview: {e}")

    # Load the image to display
    img = Image.open(image_to_display)
    img = img.resize((400, 500), Image.Resampling.LANCZOS)  # Resize for display
    img_tk = ImageTk.PhotoImage(img)

    # Create image label
    img_label = tk.Label(parent, image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection
    img_label.pack()

    # Create a text editor
    text_editor = tk.Text(parent, wrap="word", width=width, height=height)
    text_editor.pack()

    return img_label, text_editor