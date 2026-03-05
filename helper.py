from openai import OpenAI
def get_completion(prompt,model="gpt-3.5-turbo",temp= 0):
    client = OpenAI()
    response = client.responses.create(model=model,
        input=prompt,
        temperature=temp)
    return response.output[0].content[0].text