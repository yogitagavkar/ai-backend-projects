from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template(
    "Explain {topic} simply"
)

chain = prompt | llm

result = chain.invoke({"topic": "LangChain"})

print(result.content)