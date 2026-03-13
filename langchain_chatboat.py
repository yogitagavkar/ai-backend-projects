from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory
)

print(conversation.predict(input="My name is Yogita"))
print(conversation.predict(input="What is my name?"))