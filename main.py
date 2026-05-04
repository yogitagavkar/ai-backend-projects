from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
import helper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# OpenAI Client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@app.get("/")
def root():
    return {
        "status": "AI Resume Analyzer API is running 🚀"
    }


@app.post("/analyze-resume")
def analyze_resume(file: UploadFile = File(...)):
    try:
        # Extract resume text
        resume_text = helper.extract_resume_txt(file)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Unable to extract text from resume"
            )

        prompt = f"""
        Analyze the below resume and provide:

        1. Key Skills
        2. Missing Skills
        3. Suggested Job Roles
        4. Improvements in Resume

        Resume:
        {resume_text}
        """

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return {
            "status": "success",
            "analysis": response.output_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        print("Program finished")