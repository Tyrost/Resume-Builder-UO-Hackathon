import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
import os
import tkinter as tk
from tkinter import filedialog
from shutil import copy

from components.init_components import (
    create_label,
    create_elements
)
from components.main import create_window

def upload_pdf_file():
    """
    Opens a file dialog for the user to select a PDF file
    and copies the PDF to a local 'PDFs' folder.
    """
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        print(f"Selected file: {file_path}")
        
        target_directory = os.path.join(os.getcwd(), "PDFs")
        os.makedirs(target_directory, exist_ok=True)
        
        target_file_path = os.path.join(target_directory, os.path.basename(file_path))
        copy(file_path, target_file_path)
        
        print(f"File copied to: {target_file_path}")
    else:
        print("No file selected.")

def placeholder_func():
    pass

def create_checker_window(parent: tk.Tk, on_back_to_main=None):
    """
    Create and return the Checker Frame. 
    `on_back_to_main`: callback function to destroy this frame
                       and re-create the Main Menu.
    """
    # Create a frame inside the parent
    checker_frame = create_window(parent)
    # Just for visual debugging

    # Use checker_frame as the master for your widgets
    # so that destroying 'checker_frame' removes them too.
    img_label, text_editor = create_elements(checker_frame, "sample_resume1.png")

    upload_btn = tk.Button(
        checker_frame, 
        text="Upload",
        command=upload_pdf_file,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )
    
    check_btn = tk.Button(
        checker_frame, 
        text="Check Now!", 
        command=placeholder_func,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )
    
    # The critical part: a button that calls on_back_to_main
    back_to_main_btn = tk.Button(
        checker_frame, 
        text="Main Menu",
        command=on_back_to_main,  # <--- callback
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )
    
    upload_label = create_label(checker_frame, text='Upload your resume here!')
    description_label = create_label(checker_frame, text='Put your job description here!')

    # Place (or pack) them. Using place here for direct coordinate control:
    back_to_main_btn.place(x=50, y=50)
    upload_btn.place(x=50, y=200)
    check_btn.place(x=1000, y=200)

    img_label.place(x=580, y=150)
    text_editor.place(x=50, y=350)

    upload_label.place(x=50, y=150)
    description_label.place(x=50, y=300)
    
    return checker_frame