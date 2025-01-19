import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.intit_components import *
from components.main import create_window
import tkinter as tk
from tkinter import filedialog
from shutil import copy
# from PIL import Image, ImageTk
# from components.TextEditor import TextEditor
# from components.Button import Button

def upload_pdf_file():
    """
    Opens a file dialog for the user to select a PDF file.
    Prints the selected file's path.
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

def is_clicked_event(btn:Button, func):
    if btn.is_pressed:
        
        btn.click_btn(func)

# _______ Encapsulation _______ #

def placeholder_func():
    pass

def create_checker_window(WINDOW:tk.Tk):

    # Creation
    
    checker_frame = create_window(WINDOW, window_name='checker_frame')
    img_label, text_editor = create_elements(WINDOW, checker_frame, "sample_resume1.png")
    
    upload_btn = tk.Button(master=WINDOW, text="Upload", command=upload_pdf_file, width=10, height=3, fg="black", font=("Arial", 12))
    
    # PLACEHOLDER COMMANDS
    check_btn = tk.Button(master=WINDOW, text="Check Now!", command=placeholder_func, width=10, height=3, fg="black", font=("Arial", 12))
    back_to_main_btn = tk.Button(master=WINDOW, text="Main Menu", command=placeholder_func, width=10, height=3, fg="black", font=("Arial", 12))
    ######################
    
    upload_label = create_label(checker_frame, text='Upload your resume here!')
    description_label = create_label(checker_frame, text='Put your job description here!')
    
    # Placement
    
    back_to_main_btn.place(x = 50, y = 50)
    upload_btn.place(x=50, y=200)
    check_btn.place(x=1000, y = 200)
    
    img_label.place(x=580, y = 150)
    text_editor.place(x=50, y= 350)
    
    upload_label.place(x=50, y=150)
    description_label.place(x=50, y = 300)
    
    # # Start the main loop
    # WINDOW.mainloop()

create_checker_window()