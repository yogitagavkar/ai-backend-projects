from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_data=PyPDFLoader("sample.pdf")
documents = load_data.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap = 10)
docs_data = text_splitter.split_documents(documents)


embedding = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(docs_data,embedding)


retriever = vectorstore.as_retriever()

llm = ChatOpenAI(temperature=0)


qa = RetrievalQA.from_chain_type(llm=llm,retriever=retriever)


query = "What is this document about?"
print(qa.run(query))