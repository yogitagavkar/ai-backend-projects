from openai import OpenAI
from db import run_sql
import json

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "run_sql",
            "description": "Execute SQL query on sales database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

def process_query(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": 
             """You are a data analyst. Table: sales(product, amount, month).IMPORTANT RULES:
            - If user does NOT specify month → Then show error as no sales data available for this month
            - Do NOT only assume latest month
            - Use SUM(amount) correctly
            - Return accurate SQL only"""},
            {"role": "user", "content": question}
        ],
        tools=tools
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        tool_call_id = tool_call.id
        args = json.loads(tool_call.function.arguments)
        result = run_sql(args["query"])

        final = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question},
                {"role": "assistant", "tool_calls": msg.tool_calls},
                {"role": "tool", "tool_call_id": tool_call_id,"content": str(result)}
            ]
        )

        return final.choices[0].message.content

    return msg.content