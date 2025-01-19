import tkinter as tk
from interview.resume_app import create_resume_window
from checker.checker import create_checker_window
from components import create_window
from main_menu.menu import create_main_menu_frame

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
        """Destroy the MAIN frame, create the CHECKER frame."""
        print("Destroying MAIN, creating CHECKER.")
        self.MAIN_FRAME.destroy()

        # Provide a callback so the checker can go back to main
        self.CHECKER_FRAME = create_checker_window(
            parent=self.MASTER_WINDOW,
            on_back_to_main=self.go_back_to_main
        )
        self.CHECKER_FRAME.pack(fill="both", expand=True)

    def go_to_interview(self):
        """Destroy the Main frame, then create the Interview frame."""
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
            del self.CHECKER_FRAME  # Optional cleanup

        # If the interview frame exists, destroy it
        if hasattr(self, "INTERVIEW_FRAME"):
            print("Destroying INTERVIEW.")
            self.INTERVIEW_FRAME.destroy()
            del self.INTERVIEW_FRAME

        # Now recreate the MAIN menu
        self.MAIN_FRAME = create_main_menu_frame(
            parent=self.MASTER_WINDOW,
            on_upload=self.go_to_checker,
            on_create=self.go_to_interview
        )
        self.MAIN_FRAME.pack(fill="both", expand=True)
        
    def run(self):
        self.MASTER_WINDOW.mainloop()
        
############################################


if __name__ == "__main__":
    app = MAIN()
    app.run()


