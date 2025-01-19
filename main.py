import tkinter as tk
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

    def go_back_to_main(self):
        """Destroy the CHECKER frame, recreate the MAIN menu."""
        print("Destroying CHECKER, going back to MAIN.")
        self.CHECKER_FRAME.destroy()

        # Now create a fresh MAIN menu again
        self.MAIN_FRAME = create_main_menu_frame(
            parent=self.MASTER_WINDOW,
            on_upload=self.go_to_checker,
            on_create=self.go_to_interview
        )
        self.MAIN_FRAME.pack(fill="both", expand=True)

    def go_to_interview(self):
        """Destroy the MAIN frame, create an interview frame (placeholder)."""
        print("Destroying MAIN, creating INTERVIEW.")
        self.MAIN_FRAME.destroy()
        
        self.INTERVIEW_FRAME = create_window(self.MASTER_WINDOW)
        self.INTERVIEW_FRAME.config(bg="green")
        
        # You can add some sample content
        lbl = tk.Label(self.INTERVIEW_FRAME, text="Interview Frame", bg="green", fg="white")
        lbl.pack(pady=50)

        self.INTERVIEW_FRAME.pack(fill="both", expand=True)

    def run(self):
        self.MASTER_WINDOW.mainloop()


if __name__ == "__main__":
    app = MAIN()
    app.run()


