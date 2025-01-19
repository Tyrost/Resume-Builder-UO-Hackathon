from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import fitz

class PDF:
    def __init__(self, path, page_size=letter):
        self.path = path    
        self.file_name = None
        self.job_description = None
        self.skills = None
        self.work_experience = None
        self.education = None
        self.certifications = None
        self.awards = None
        self.volunteer = None
        self.title = None
        self.name = None
        self.contact_info = None
        self.address = None
        self.objective = None
        self.linkedin = None
        self.github = None
        self.other_profiles = None
        self.languages = None
        self.hobbies = None
        self.references = None
        self.projects = None
        self.publications = None
        self.affiliations = None


        self.page_size = page_size
        self.canvas = canvas.Canvas(pagesize=page_size)

    def add_text(self, text, x, y):
        self.canvas.drawString(x, y, text)

    def add_image(self, image_path, x, y, width, height):
        self.canvas.drawImage(image_path, x, y, width, height)

    def add_rectangle(self, x, y, width, height):
        self.canvas.rect(x, y, width, height)

    def save(self):
        self.canvas.save()

    def extract_text_from_pdf(self, file_path):
        pdf_document = fitz.open(file_path)
        pdf_text = ""
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pdf_text += page.get_text()

        return pdf_text

    def populate_from_text(self, text):
        # Placeholder parsing logic; you'll need to customize this
        if "John Doe" in text:  # Dummy check, replace with actual logic
            self.name = "John Doe"
        if "john.doe@example.com" in text:  # Dummy check, replace with actual logic
            self.contact_info = "john.doe@example.com"
        # Add more parsing logic for other fields...


    def extract(self, file_name):
        self.file_name = file_name
        # Extract text from the file and assign to the corresponding attributes




import fitz  # PyMuPDF

class ResumeExtractor:
    def __init__(self):
        self.file_name = None
        self.name = None
        self.contact_info = None
        self.address = None
        self.job_description = None
        self.skills = None
        self.work_experience = None
        self.education = None
        self.certifications = None
        self.awards = None
        self.volunteer = None
        self.objective = None
        self.linkedin = None
        self.github = None
        self.other_profiles = None
        self.languages = None
        self.hobbies = None
        self.references = None
        self.projects = None
        self.publications = None
        self.affiliations = None

    def extract_text_from_pdf(self, file_path):
        pdf_document = fitz.open(file_path)
        pdf_text = ""
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pdf_text += page.get_text()

        return pdf_text

    def populate_from_text(self, text):
        # Placeholder parsing logic; you'll need to customize this
        if "John Doe" in text:  # Dummy check, replace with actual logic
            self.name = "John Doe"
        if "john.doe@example.com" in text:  # Dummy check, replace with actual logic
            self.contact_info = "john.doe@example.com"
        # Add more parsing logic for other fields...

# Usage example
file_path = "example_resume.pdf"

# Create an instance of the class and extract text from the PDF
resume = ResumeExtractor()
pdf_text = resume.extract_text_from_pdf(file_path)

# Populate class variables using the extracted text
resume.populate_from_text(pdf_text)

# Print the extracted details (for demonstration)
print(f"Name: {resume.name}")
print(f"Contact Info: {resume.contact_info}")
# Add print statements for other fields as needed...

