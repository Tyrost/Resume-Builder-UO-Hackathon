import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk

from components.SystemOutputBox import SystemOutputBox
from components.main import create_window
from components.init_components import (
    create_label,
    create_elements
)

def placeholder_func():
    pass

def create_resume_window(parent: tk.Tk, on_back_to_main=None):
    """
    Create and return the Builder Frame (similar to the checker window).
    The layout, dimensions, and widget positions mirror the checker file.

    :param parent: The parent window or container (e.g. root Tk).
    :param on_back_to_main: Callback function to destroy this builder frame 
                            and re-create/show the main menu.
    """
    # Create the builder frame (same concept as the checker frame)
    builder_frame = create_window(parent)

    # Create an image + text editor inside builder_frame
    # (We pass builder_frame for both the parent of the image and text editor 
    # so that when builder_frame is destroyed, these widgets go away too.)
    text_editor = tk.Text(builder_frame, wrap="Job description:", width=80, height=5, font=("Arial", 12))

    # Create a "Main Menu" button that calls on_back_to_main
    back_to_main_btn = tk.Button(
        builder_frame,
        text="Main Menu",
        command=on_back_to_main,  # This callback will destroy builder frame, show main
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )

    chatbot_box = SystemOutputBox(
        builder_frame,
        initial_text="",
        width=85,
        height=25,
        font=("Arial", 12)
    )

    chatbot_box.place(x=300, y=50)
    
    # Place them similarly to your checker window approach
    back_to_main_btn.place(x=50, y=50)
    

    # If you want the image & text editor in the same spots as checker:
    text_editor.place(x=300, y=700)

    return builder_frame
