from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import reportlab
import fitz
from openai import OpenAI
import sys
import os

client = OpenAI(api_key="asdbfiu") # Add your API key here

class PDF:
    def __init__(self, path, page_size=letter):
        self.path = path    
        self.file_name = None
        self.job_description = None
        self.skills = None
        self.work_experience = []
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

        self.job_description = {
            "Junior software engineer": "",
            "Software engineer": "",
        }


        self.page_size = page_size
        self.canvas = canvas.Canvas(filename=self.path, pagesize=page_size) ######

    def add_text(self, text, x, y):
        self.canvas.drawString(x, y, text)

    def add_image(self, image_path, x, y, width, height):
        self.canvas.drawImage(image_path, x, y, width, height)

    def add_rectangle(self, x, y, width, height):
        self.canvas.rect(x, y, width, height)

    def save(self):
        self.canvas.save()

    def __extract_text_from_pdf(self):
        pdf_document = fitz.open(self.path)
        pdf_text = ""
        
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            
            pdf_text += page.get_text()

        return pdf_text

    
    
    def populate_from_text(self):
        self.text = self.__extract_text_from_pdf()
        headers_list = "job_description, skills, work_experience, education, certifications, awards, volunteer, title, name, contact_info, address, objective, linkedin, github, other_profiles, languages, hobbies, references, projects, publications, affiliations"
        
        # Prompt for ChatCompletion API
        prompt = f'''Based on the following headers: {headers_list}\n\nWhich headers do parts of the following text best fit under?\n\nText: {self.text}\n\nHeader:
        I also want the descrriptions for projets/jobs/experience/school etc..
        '''
        
    
        # Use the ChatCompletion endpoint
        response = client.chat.completions.create(
            model="gpt-4o",  # Replace with "gpt-4" for better quality
            messages=[
                {"role": "system", "content": "You are a helpful assistant that categorizes text based on predefined headers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000 
        )
        
        # Extract the response text
        answer = response.choices[0].message
        self.text = answer.content
        return
        


if __name__ == "__main__":
    resume1 = PDF(os.path.abspath("pdfs/Resume1.pdf"))
    
    
    

