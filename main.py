from fastapi import FastAPI,UploadFile,File
from openai import OpenAI
import helper
import os

app = FastAPI()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
@app.post("/analyze-resume")

def analyze_resume(file:UploadFile=File(...)):
    try :
            resume_text = helper.extract_resume_txt(file)
            prompt = f""" Analazye below resume 
            extract
            1.key skills
            2.missing skills
            3.suggest job roles
            4.improvement in resume
            resume {resume_text}
            """
            response = client.responses.create(model="gpt-4.1-mini",input=prompt)
            return {
                "analysis":response.output_text
            }
    except ValueError as e:
        print("error",e)
    finally:
        print("Program finished")