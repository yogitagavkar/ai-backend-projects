import os
import openai
import sys
sys.path.append('../..')
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain_community.document_loaders import FileSystemBlobLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

loader = PyPDFLoader("sample_resume.pdf")
pages = loader.load()
page = pages[0]


url="https://www.youtube.com/watch?v=5i2Hn8OG94o&t=3441s"
save_dir="docs/youtube/"
os.makedirs(save_dir, exist_ok=True)

loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser()
)

docs = loader.load()

for doc in docs[:1]:
    print(doc.page_content[:500])
