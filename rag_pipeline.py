from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def load_db(file, chain_type, k):
    loader = PyPDFLoader(file)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150
    )
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    db = DocArrayInMemorySearch.from_documents(docs, embeddings)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})

    memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer")

    qa = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0),
    chain_type=chain_type,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    return_generated_question=True,)

    return qa