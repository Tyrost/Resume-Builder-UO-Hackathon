import os
import sys
import tkinter as tk
from tkinter import filedialog
from shutil import copy
import json
import threading
from PIL import Image, ImageTk
import fitz 

# Modifier
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.init_components import create_label
from components.main import create_window
from scripts.Resume import Resume

def upload_pdf_file(upload_status_label, img_label):
    """
    Opens a file dialog for the user to select a PDF file
    and programmatically renames and copies it to a local 'PDFs' folder.
    Updates the upload status label with the file name or success message.
    Refreshes the displayed image preview.
    """
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        directory_path = os.path.abspath('PDFs')
        os.makedirs(directory_path, exist_ok=True)  # Check directory exists
        
        target_file_path = os.path.join(directory_path, "file.pdf")
        if os.path.exists(target_file_path):
            os.remove(target_file_path)

        copy(file_path, target_file_path)

        upload_status_label.config(text=f"Uploaded: {os.path.basename(file_path)}")

        update_image_preview(img_label)
    else:
        upload_status_label.config(text="No file selected.")

def update_image_preview(img_label):
    """
    Updates the image preview displayed in the GUI.
    """
    pdf_path = os.path.abspath('PDFs/file.pdf')
    preview_image_path = os.path.abspath('components/images/preview.jpg')

    # Generate image preview if PDF exists
    if os.path.exists(pdf_path):
        try:
            pdf_document = fitz.open(pdf_path)
            page = pdf_document.load_page(0)  # Load the first page
            pix = page.get_pixmap()  # Render the page to an image
            pix.save(preview_image_path)  # Save as PNG
            pdf_document.close()
        except Exception as e:
            print(f"Failed to generate PDF preview: {e}")

    # Load the image
    img = Image.open(preview_image_path)
    img = img.resize((400, 500), Image.Resampling.LANCZOS)  # Resize for display
    img_tk = ImageTk.PhotoImage(img)

    # Update the image label
    img_label.config(image=img_tk)
    img_label.image = img_tk

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
    image_to_display = preview_image_path
    if os.path.exists(pdf_path):
        try:
            # Open the PDF and render the first page
            pdf_document = fitz.open(pdf_path)
            page = pdf_document.load_page(0)  # Load the first page
            pix = page.get_pixmap()  # Rendering page to an image
            pix.save(preview_image_path)  # Save as PNG
            pdf_document.close()
            image_to_display = preview_image_path 
        except Exception as e:
            print(f"Failed to generate PDF preview: {e}")

    img = Image.open(image_to_display)
    img = img.resize((400, 500), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    img_label = tk.Label(parent, image=img_tk)
    img_label.image = img_tk
    img_label.pack()

    text_editor = tk.Text(parent, wrap="word", width=width, height=height)
    text_editor.pack()

    return img_label, text_editor

def score_resume(json_file_path: str):
    """
    Calculates the score for a resume based on a job description read from a JSON file.

    :param json_file_path: Path to the JSON file containing the job description.
    :return: The calculated score for the resume.
    """
    # Read the job description from the JSON file
    if not os.path.exists(json_file_path):
        print(f"Error: JSON file '{json_file_path}' does not exist.")
        return None
    
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    job_description = data.get("job_description", "").strip()
    
    if not job_description:
        print("Error: No valid job description found in the JSON file.")
        return None

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    pdf_path = os.path.join(project_root, "PDFs", "file.pdf")
    
    if not os.path.exists(pdf_path):
        print(f"Error: Resume file '{pdf_path}' does not exist.")
        return None

    resume = Resume(pdf_path)
    resume.set_job_description(job_description) # Job description class setter
    score = resume.score_resume()
    return score

def create_checker_window(parent: tk.Tk, on_back_to_main=None):
    """
    Create and return the Checker Frame.
    :param parent: The parent Tkinter widget (e.g., root window).
    :param on_back_to_main: Callback to navigate back to the main menu.
    """
    
    # def refresh_checker_frame():
    #     """
    #     Refreshes the checker frame to update the preview dynamically.
    #     Clears all widgets and recreates them.
    #     """
    #     for widget in checker_frame.winfo_children():
    #         widget.destroy()
    #     create_elements(checker_frame)
    
    checker_frame = create_window(parent)

    img_label, text_editor = create_elements(checker_frame)

    # Add a label for status updates
    status_label = tk.Label(
        checker_frame, 
        text="", 
        font=("Arial", 28), 
        fg="White"
    )
    status_label.place(x=1000, y=300)  # postioned it below other elements

    upload_status_label = tk.Label(
        checker_frame, 
        text="No file uploaded yet.", 
        font=("Arial", 12), 
        fg="white"
    )
    upload_status_label.place(x=50, y=260)

    def save_job_description_to_json(job_description, json_file_path):

        data = {"job_description": job_description}
        
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f"Job description saved to {json_file_path}")

    def on_save_job_description(event=None):

        job_description = text_editor.get("1.0", tk.END).strip()
        json_file_path = os.path.abspath('components/job_description.json')
        save_job_description_to_json(job_description, json_file_path)
        
        text_editor.delete("1.0", tk.END)
        
        return 'break'

    def on_check_now():

        json_file_path = os.path.abspath('components/job_description.json')

        # Checks dependencies
        if os.path.exists(json_file_path):
            directory_path = os.path.abspath('PDFs')

            if len(os.listdir(directory_path)) != 0:
                # Set status to Loading...
                status_label.config(text="Loading...")

                def calculate_score():
                    """
                    Perform the scoring in a separate thread.
                    """
                    try:
                        score = score_resume(json_file_path)
                        if score is not None:
                            status_label.config(text=f"{score}/100")
                        else:
                            status_label.config(text="Invalid Input.")
                    except Exception as e:
                        status_label.config(text=f"Error: {e}")

                # Start the calculation on a separate thread
                threading.Thread(target=calculate_score, daemon=True).start()
            else:
                status_label.config(text="Please upload a resume before checking.")
        else:
            status_label.config(text="Please enter a job description and press Enter before checking.")

    # Bind the Enter key to save the job description
    text_editor.bind("<Return>", on_save_job_description)

    # __________________ Button Creation __________________ #
    
    upload_btn = tk.Button(
        checker_frame, 
        text="Upload",
        command=lambda: upload_pdf_file(upload_status_label, img_label),
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )

    check_btn = tk.Button(
        checker_frame, 
        text="Check Now!", 
        command=on_check_now,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )

    back_to_main_btn = tk.Button(
        checker_frame, 
        text="Main Menu",
        command=on_back_to_main,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )

    # __________________ Label Creation __________________ #
    
    upload_label = create_label(checker_frame, text="Upload your resume here!")
    description_label = create_label(checker_frame, text="Put your job description here!")

    # __________________ Widget Placement __________________ #
    
    back_to_main_btn.place(x=50, y=50)
    upload_btn.place(x=50, y=200)
    check_btn.place(x=1000, y=200)
    img_label.place(x=500, y=115)
    text_editor.place(x=50, y=350)
    upload_label.place(x=50, y=150)
    description_label.place(x=50, y=300)

    return checker_frame
