from openai import OpenAI
def get_completion(prompt,model="gpt-3.5-turbo"):
    client = OpenAI()
    response = client.responses.create(model=model,
        input=prompt,
        temperature=0)
    return response.output[0].content[0].text

def calculation(operation,num1,num2):
    
    match(operation):
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return "Invalid operation"   

