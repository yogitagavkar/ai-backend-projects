from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
import helper
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing")

client = OpenAI(api_key=api_key)


@app.get("/")
def root():
    return {
        "status": "AI Resume Analyzer API is running 🚀"
    }


@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        resume_text = await helper.extract_resume_txt(file)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Unable to extract text from resume"
            )

        prompt = f"""
Analyze this resume and provide:

1. Key Skills
2. Missing Skills
3. Suggested Job Roles
4. Resume Improvements

Resume:
{resume_text}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        analysis = response.choices[0].message.content

        return {
            "status": "success",
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )