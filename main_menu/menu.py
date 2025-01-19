import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from components.init_components import (
    create_label,
    create_button,
    create_image
)

from components.main import create_window

description = (
    "Welcome to ResumAI - Your AI-Powered Hiring Assistant!\n\n"
    "At ResumAI, we harness the power of AI to transform the hiring process by evaluating resumes with\n"
    "precision and ensuring candidates' qualifications are assessed accurately and efficiently.\n\n"
    "Our intelligent assistant goes beyond resume analysis by generating tailored interview questions\n"
    "to help employers conduct insightful and effective interviews that uncover top talent.\n\n"
    "By focusing on skills, experience, and potential, ResumAI helps you build a stronger team\n"
    "while streamlining your hiring process and empowering confident, informed decisions.\n"
)

def create_main_menu_frame(parent, on_upload=None, on_create=None):
    """
    Create and return the Main Menu frame.
    
    :param parent: The parent widget (root window or parent Frame).
    :param on_upload: Callback for the 'Upload' button click.
    :param on_create: Callback for the 'Create' button click.
    """
    main_menu_frame = create_window(parent)
    # Example: set a dark background so that white text is visible
    main_menu_frame.config(bg="gray20")

    # 1. Title at the top
    title_label = create_label(
        main_menu_frame, 
        text='ResumAI', 
        font=("Times New Roman", 60)
    )
    # style if needed (e.g. white text on dark background):
    title_label.config(bg="gray20", fg="white")
    title_label.pack(side="top", pady=15)

    # 2. Description just below the title
    description_label = create_label(
        main_menu_frame, 
        text=description, 
        font=("Times New Roman", 14)
    )
    description_label.config(bg="gray20", fg="white", justify="left")
    description_label.pack(side="top", padx=20, pady=10)

    # 3. A frame on the left for the “Upload” and “Create” controls
    left_frame = tk.Frame(main_menu_frame, bg="gray20")
    left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    upload_label = create_label(
        left_frame,
        text="Upload A Resume For Grading",
        font=("Times New Roman", 22)
    )
    upload_label.config(bg="gray20", fg="white")
    upload_label.pack(pady=10)

    upload_btn = create_button(
        left_frame,
        text="Score",
        width=12,
        height=4,
        command=on_upload
    )
    upload_btn.pack(pady=5)

    build_label = create_label(
        left_frame,
        text="Create Interview Questions For Applicant",
        font=("Times New Roman", 22)
    )
    build_label.config(bg="gray20", fg="white")
    build_label.pack(pady=10)

    create_btn = tk.Button(
        left_frame,

        text="Create",
        width=12,
        height=4,
        command=on_create
    )
    create_btn.pack(pady=5)

    # 4. A frame on the right for the image
    right_frame = tk.Frame(main_menu_frame, bg="gray20")
    right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    _, img_label = create_image(right_frame, "interview.png", width=400, height=400)
    img_label.config(bg="gray20")
    img_label.pack(anchor="center", pady=20)

    return main_menu_frame
