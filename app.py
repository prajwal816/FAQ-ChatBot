import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("IBM_PROJECT_ID")
REGION = os.getenv("IBM_REGION")
MODEL_ID = os.getenv("IBM_MODEL_ID")

def ask_ibm(prompt):
    url = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_ibm_token()}",
    }
    data = {
        "model_id": MODEL_ID,
        "input": prompt,
        "project_id": PROJECT_ID
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["results"][0]["generated_text"]

def get_ibm_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": API_KEY
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return response.json()["access_token"]
