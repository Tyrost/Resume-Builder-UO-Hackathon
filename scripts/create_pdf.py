from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import fitz
from openai import OpenAI
import sys
import os

client = OpenAI(api_key="") # Add your API key here

class Resume:
    def __init__(self, path, page_size=letter):
        self.path = path  
        self.job_description = None
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

    def resume_analysis(self):
        self.text = self.__extract_text_from_pdf()
        headers_list = "job_description, skills, work_experience, education, certifications, awards, volunteer, title, name, contact_info, address, objective, linkedin, github, other_profiles, languages, hobbies, references, projects, publications, affiliations"
        
        # Prompt for ChatCompletion API
        prompt = f'''Based on the following headers: {headers_list}\n\nWhich headers do parts of the following text best fit under?\n\nText: {self.text}\n\nHeader:
        I also want the descrriptions for projets/jobs/experience/school etc..
        '''
        
    
        # Use the ChatCompletion endpoint
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with "gpt-4" for better quality
            messages=[
                {"role": "system", "content": "You are a helpful assistant that categorizes text based on predefined headers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000 
        )
        
        # Extract the response text
        answer = response.choices[0].message
        self.new_text = answer.content
        return 
    
    def score_resume(self, job):
        Resume.resume_analysis(self)


        prompt = f'''Score the following resume based on how good it is for a job application. The resume is as follows: {self.new_text}
        I also want it to take in {self.job_description}(only use this if it is not None) and score the resume based on how well it fits the job description.
        I want the score to be a number 1 - 100 with 100 being the best fit.

        return only one number
        '''

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with "gpt-4" for better quality
            messages=[
                {"role": "system", "content": "You are a helpful assistant that scores resumes based on how well they fit a job description."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1
        )
        answer = response.choices[0].message
        return answer.content

    def job_description(self, job_description):
        self.job_description = job_description
        


if __name__ == "__main__":
    resume1 = Resume(os.path.abspath("resumes/Resume1.pdf"))
    print(resume1.score_resume())
    
    
    

