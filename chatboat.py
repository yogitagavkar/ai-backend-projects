from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def ask_ai(question):
    response = client.chat.completions.create(model="gpt-4.1-mini",
                                              messages=[{"role":"system","content":"You are a helpful assistant"}
                                                        ,{"role":"user","content":question}])
    return response.choices[0].message.content