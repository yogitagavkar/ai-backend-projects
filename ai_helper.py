from openai import OpenAI
import os


client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def generate_insights(data_summary):

    prompt = f"""Analyze dataset summary below and generate useful insights
    {data_summary}

    Provide 3 clear insights.
    """

    response = client.chat.completions.create(model="gpt-4.1-mini",messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content