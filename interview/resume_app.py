import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
import json

from scripts.Resume import Resume
from components.SystemOutputBox import SystemOutputBox
from components.main import create_window
from components.init_components import create_label, create_elements


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

    job_description = event.widget.get("1.0", tk.END).strip()
    json_file_path = os.path.abspath('components/job_description.json')
    save_job_description_to_json(job_description, json_file_path)

    event.widget.delete("1.0", tk.END)  # Clear the text editor on confirm
    return 'break'

def create_resume_window(parent: tk.Tk, on_back_to_main=None):

    builder_frame = create_window(parent)

    text_editor = tk.Text(builder_frame, wrap="word", width=80, height=5, font=("Arial", 12))
    text_editor.bind("<Return>", on_save_job_description)

    resume_status_label = tk.Label(
    builder_frame,
    text="",  # Placeholder text
    font=("Arial", 12),
    fg="black"
    )
    description_status_label = tk.Label(
    builder_frame,
    text="",
    font=("Arial", 12),
    fg="black"
    )
    
    def update_status_labels():

        resume_path = os.path.abspath('PDFs/file.pdf')
        description_path = os.path.abspath('components/job_description.json')

        if os.path.exists(resume_path):
            resume_status_label.config(text="Resume file found.", fg="green")
        else:
            resume_status_label.config(text="Resume file not found!", fg="red")

        if os.path.exists(description_path):
            description_status_label.config(text="Job description file found.", fg="green")
        else:
            description_status_label.config(text="Job description file not found!", fg="red")

    update_status_labels() # Running Function
    
    def ask_question():

        resume_path = os.path.abspath('PDFs/file.pdf')
        description_path = os.path.abspath('components/job_description.json')
        
        if not os.path.exists(resume_path):
            chatbot_box.set_text("Please upload a resume before generating questions.")
            return

        if not os.path.exists(description_path):
            chatbot_box.set_text("Please provide a job description before generating questions.")
            return

        with open(description_path, 'r') as json_file:
            data = json.load(json_file)
        
        try:
            print('executing...\n')
            resume = Resume(resume_path)
            print('instance set')
            resume.set_job_description(data["job_description"])
            questions = resume.interview_questions()
            print(questions)
            chatbot_box.set_text(str(questions))
        except Exception as e:
            chatbot_box.set_text(f"Error generating questions: {e}")

    back_to_main_btn = tk.Button(
        builder_frame,
        text="Main Menu",
        command=on_back_to_main,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )
    
    generate_btn = tk.Button(
        builder_frame,
        text='Generate',
        command=ask_question,
        width=10,
        height=3,
        fg="black",
        font=("Arial", 12)
    )

    chatbot_box = SystemOutputBox(
        builder_frame,
        initial_text="Chatbot:",
        width=85,
        height=25,
        font=("Arial", 12)
    )

    chatbot_box.place(x=300, y=50)
    generate_btn.place(x=1050, y=50)
    back_to_main_btn.place(x=50, y=50)
    text_editor.place(x=300, y=700)
    
    resume_status_label.place(x = 50, y = 630)
    description_status_label.place(x = 50, y = 600)
    
    return builder_frame