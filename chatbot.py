import os
import requests
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_core.documents import Document
import requests
import json

# Load env variables
load_dotenv()
IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID")
IBM_REGION = os.getenv("IBM_REGION")
IBM_MODEL_ID = os.getenv("IBM_MODEL_ID")

# Load vectorstore
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


# Get IBM watsonx access token
def get_ibm_access_token(api_key):
    iam_url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "apikey": api_key,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    response = requests.post(iam_url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Failed to get IAM token: " + response.text)
    return response.json()["access_token"]

# Generate response using IBM watsonx
def ask_ibm(prompt: str) -> str:
    DEBUG = False  # Set to True to enable debug logs

    BASE_URL = "https://eu-de.ml.cloud.ibm.com"
    url = f"{BASE_URL}/ml/v1/text/generation?version=2024-05-01"

    access_token = get_ibm_access_token(IBM_API_KEY)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "model_id": "google/flan-ul2",
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200
        },
        "project_id": IBM_PROJECT_ID
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if DEBUG:
            print("[DEBUG] IBM response:", json.dumps(data, indent=2))

        return data["results"][0]["generated_text"].strip()

    except (KeyError, IndexError):
        if DEBUG:
            print("[ERROR] Unexpected IBM chat API response format.")
            print("[DEBUG] IBM API response:", data)
        return "Sorry, I couldn't generate a proper response."

    except requests.exceptions.RequestException as e:
        if DEBUG:
            print("[ERROR] IBM request failed:", str(e))
        return "Sorry, I couldn't connect to the AI service. Please try again later."



# QA Chat Function
def ask_question(query):
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"User asked: {query}\nAnswer based on the following context:\n{context}"

    return ask_ibm(prompt)

# CLI test (you can remove this in production)
if __name__ == "__main__":
    print("🤖 FAQ Chatbot ready. Ask a question (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ask_question(user_input)
        print("Bot:", response.strip())

