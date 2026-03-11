from fastapi import FastAPI
from pydantic import BaseModel
import chatboat

app = FastAPI()

class ChatRequest(BaseModel):
    message:str

@app.post("/chat")

def chat(request:ChatRequest):
    try : 
       result = chatboat.ask_ai(request.message)

       return {
           "User Message":request.message,
           "AI Response":result
       }
    except Exception as e:
        return e
    else:
        return "No Error"
    finally:
        print("Program Finished")