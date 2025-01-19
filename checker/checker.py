import os
import sys
import tkinter as tk
from tkinter import filedialog
from shutil import copy
import json
import threading

# Ensure imports work correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import necessary components
from components.init_components import create_label, create_elements
from components.main import create_window
from scripts.Resume import Resume
from components.TextEditor import CustomText

# Helper function to handle PDF uploads
def upload_pdf_file():
    """
    Opens a file dialog for the user to select a PDF file
    and programmatically renames and copies it to a local 'PDFs' folder.
    """
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        directory_path = os.path.abspath('PDFs')
        os.makedirs(directory_path, exist_ok=True)  # Ensure the directory exists
        print(os.path.exists(directory_path))  # Debug print to confirm the directory exists
        
        # Check if 'file.pdf' exists in the directory and remove it
        target_file_path = os.path.join(directory_path, "file.pdf")
        if os.path.exists(target_file_path):
            os.remove(target_file_path)
            print(f"Removed existing file: {target_file_path}")

        # Copy the new file and rename it to 'file.pdf'
        copy(file_path, target_file_path)
        print(f"File copied and renamed to: {target_file_path}")
    else:
        print("No file selected.")
        
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

    # Set up the path to the PDF file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    pdf_path = os.path.join(project_root, "PDFs", "file.pdf")
    
    # Ensure the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: Resume file '{pdf_path}' does not exist.")
        return None

    # Initialize the Resume object and calculate the score
    resume = Resume(pdf_path)
    resume.set_job_description(job_description)  # Set the job description
    score = resume.score_resume()
    return score


def create_checker_window(parent: tk.Tk, on_back_to_main=None):
    """
    Create and return the Checker Frame.
    :param parent: The parent Tkinter widget (e.g., root window).
    :param on_back_to_main: Callback to navigate back to the main menu.
    """
    
    def refresh_checker_frame():
        """
        Refreshes the checker frame to update the preview dynamically.
        Clears all widgets and recreates them.
        """
        for widget in checker_frame.winfo_children():
            widget.destroy()  # Remove all existing widgets
        create_elements(checker_frame)
    
    def upload_and_refresh():
        """
        Handles PDF upload and refreshes the checker frame to display the updated preview.
        """
        upload_pdf_file()  # Function to handle PDF uploads
        refresh_checker_frame()
    
    checker_frame = create_window(parent)

    img_label, text_editor = create_elements(checker_frame)
    # text_editor = CustomText(parent, wrap="word", width=60, height=20)

    # Add a label for status updates
    status_label = tk.Label(
        checker_frame, 
        text="", 
        font=("Arial", 28), 
        fg="White"
    )
    status_label.place(x=1000, y=300)  # Position it below other elements

    def save_job_description_to_json(job_description, json_file_path):
        """
        Saves the job description to a JSON file. 
        Creates the file if it doesn't exist and overwrites any existing data.

        :param job_description: The job description to save.
        :param json_file_path: The path to the JSON file where the data will be stored.
        """
        data = {"job_description": job_description}
        
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f"Job description saved to {json_file_path}")

    def on_save_job_description(event=None):
        """
        Saves the job description from the text editor to a JSON file.
        Triggered by pressing Enter in the text editor.
        """
        job_description = text_editor.get("1.0", tk.END).strip()
        json_file_path = os.path.abspath('components/job_description.json')
        save_job_description_to_json(job_description, json_file_path)
        
        text_editor.delete("1.0", tk.END)
        
        return 'break'

    def on_check_now():
        """
        Retrieves job description from text editor and scores the resume.
        """
        json_file_path = os.path.abspath('components/job_description.json')

        # Ensure the JSON file exists before proceeding
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

                # Start the calculation in a separate thread
                threading.Thread(target=calculate_score, daemon=True).start()
            else:
                status_label.config(text="Please upload a resume before checking.")
        else:
            status_label.config(text="Please enter a job description and press Enter before checking.")

    # Bind the Enter key to save the job description
    text_editor.bind("<Return>", on_save_job_description)

    # Create buttons
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

    # Create Labels
    upload_label = create_label(checker_frame, text="Upload your resume here!")
    description_label = create_label(checker_frame, text="Put your job description here!")

    # Placement
    back_to_main_btn.place(x=50, y=50)
    upload_btn.place(x=50, y=200)
    check_btn.place(x=1000, y=200)
    img_label.place(x=500, y=115)
    text_editor.place(x=50, y=350)
    upload_label.place(x=50, y=150)
    description_label.place(x=50, y=300)

    return checker_frame
