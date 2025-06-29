from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
import os

load_dotenv()

# Load documents
#loader = TextLoader("data/faqs/faq1.txt")
#documents = loader.load()

folder_path = "data/faqs"
files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".txt", ".md"))]

documents = []
for file in files:
    loader = TextLoader(file)
    documents.extend(loader.load())

# Split text
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Use local embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Save to vectorstore
vectorstore = FAISS.from_documents(texts, embeddings)
vectorstore.save_local("vectorstore")



