import tkinter as tk
from interview.resume_app import create_resume_window
from checker.checker import create_checker_window
from components import create_window
from main_menu.menu import create_main_menu_frame
import os
import shutil

class MAIN:
    def __init__(self):
        self.MASTER_WINDOW = tk.Tk()
        self.MASTER_WINDOW.geometry("1200x800")
        self.MASTER_WINDOW.title("ResumAI - Main Window")

        # Create only the MAIN frame first
        self.MAIN_FRAME = create_main_menu_frame(
            parent=self.MASTER_WINDOW,
            on_upload=self.go_to_checker,   # from MAIN to CHECKER
            on_create=self.go_to_interview
        )
        self.MAIN_FRAME.pack(fill="both", expand=True)

############################################

    def go_to_checker(self):
        
        print("Destroying MAIN, creating CHECKER.")
        self.MAIN_FRAME.destroy()

        self.CHECKER_FRAME = create_checker_window(
            parent=self.MASTER_WINDOW,
            on_back_to_main=self.go_back_to_main
        )
        self.CHECKER_FRAME.pack(fill="both", expand=True)

    def go_to_interview(self):
        print("Destroying MAIN, creating INTERVIEW.")
        self.MAIN_FRAME.destroy()

        self.INTERVIEW_FRAME = create_resume_window(
            parent=self.MASTER_WINDOW,
            on_back_to_main=self.go_back_to_main
        )
        self.INTERVIEW_FRAME.pack(fill="both", expand=True)
    
    def go_back_to_main(self):
        print("Going back to MAIN...")

        if hasattr(self, "CHECKER_FRAME"):
            print("Destroying CHECKER.")
            self.CHECKER_FRAME.destroy()
            del self.CHECKER_FRAME

        if hasattr(self, "INTERVIEW_FRAME"):
            print("Destroying INTERVIEW.")
            self.INTERVIEW_FRAME.destroy()
            del self.INTERVIEW_FRAME

        self.MAIN_FRAME = create_main_menu_frame(
            parent=self.MASTER_WINDOW,
            on_upload=self.go_to_checker,
            on_create=self.go_to_interview
        )
        self.MAIN_FRAME.pack(fill="both", expand=True)

    def run(self):
        self.MASTER_WINDOW.mainloop()  # Run the main event loop

############################################

def cleanup_files():
    """
    Deletes specified files at the end of the program.
    """
    try:
        pdf = os.path.abspath('components/job_description.json')
        description = os.path.abspath('PDFs/file.pdf')

        # Delete the PDF file if it exists
        if os.path.exists(pdf):
            try:
                os.remove(pdf)
                print(f"Deleted: {pdf}")
            except PermissionError:
                print(f"PermissionError: Could not delete {pdf}. File may be in use.")
            except Exception as e:
                print(f"Error deleting {pdf}: {e}")
        else:
            print(f"File not found: {pdf}")

        # Delete the ``description`` directory if it exists
        if os.path.exists(description):
            try:
                os.remove(description)
                print(f"Deleted: {description}")
            except PermissionError:
                print(f"PermissionError: Could not delete {description}. Directory may be in use.")
            except Exception as e:
                print(f"Error deleting {description}: {e}")
        else:
            print(f"File not found: {description}")
    except Exception as e:
        print(f"General error during cleanup: {e}")

if __name__ == "__main__":
    app = MAIN()
    try:
        app.run()
    finally:
        cleanup_files()
