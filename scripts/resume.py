from reportlab.lib.pagesizes import letter
import fitz
from openai import OpenAI
from pprint import pprint
# Initialize OpenAI client with your API key
client = OpenAI(api_key="")

class Resume:

    def __init__(self, path, page_size=letter, question=None):
        self.path = path  
        self.page_size = page_size
        self.summary = self.__extract_text_from_pdf()
        self.new_text = "None"
        self.job_description = None
        self.question = None

    def __extract_text_from_pdf(self):
        """
        Extracts text from a PDF file using PyMuPDF (fitz).
        """
        pdf_document = fitz.open(self.path)
        pdf_text = ""
        
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pdf_text += page.get_text()

        return pdf_text

    def __resume_analysis(self): # Analyze resume
    
        headers_list = "job_description, skills, work_experience, education, certifications, awards, volunteer, title, name, contact_info, address, objective, linkedin, github, other_profiles, languages, hobbies, references, projects, publications, affiliations"

        prompt = f'''Based on the following headers: {headers_list}\n\nWhich headers do parts of the following text best fit under?\n\nText: {self.summary}\n\nHeader:
        I also want descriptions for projects/jobs/experience/school etc.
        '''

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that categorizes text based on predefined headers."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )
            # Correctly extract content
            self.new_text = response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error occurred during resume analysis: {e}")
            self.new_text = "None"
        
    
    def set_job_description(self, job_description): # Setter Function

        self.job_description = job_description

    # def __is_float(value):
    #     """
    #     Check if a string can be converted to a float.
    #     """
    #     try:
    #         float(value)
    #         return True
    #     except ValueError:
    #         return False
    
    def score_resume(self):
        
        if not self.new_text or self.new_text == "None":
            self.__resume_analysis()

        prompt = f"""
        Evaluate the following resume and score its quality for a job application:\n

        Resume: {self.new_text}
        Job Description: {self.job_description},
        Return only a number from 1 to 100, or 'None' if invalid inputs of Resume and Job Descriptions. Make sure 
        the answer has potential decimal places (up to two one) if you deem so.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that scores resumes based on job descriptions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )

            score_content = response.choices[0].message.content.strip()

            try:
                if score_content:
                    return float(score_content)
                else:
                    print(f"Invalid score received: {score_content}")
                    return None
            except ValueError:
                    print(f"Invalid score received: {score_content}")
                    return None

        except Exception as e:
            print(f"Error occurred while parsing the response: {e}")
            return None


    def interview_questions(self):
        
        prompt = f'''Generate interview questions based on the following resume: **{self.summary}**
                    Use this job description if provided: **{self.job_description}**.
                    Focus on gaps in the resume and relevance to the job description.
                    Return only 5 questions.

                    If neither of these are set or they don’t look resume-related, please simply say: "Resume and job description must be set!"
                '''

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates interview questions based on a resume."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400
            )
            
            pprint(vars(response))
            
            # Correctly extract content from response
            questions = response.choices[0].message.content
            print(questions)
    
            return questions

        except KeyError as e:
            print(f"KeyError while accessing response: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while generating interview questions: {e}")
            return None

