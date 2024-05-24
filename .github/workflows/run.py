from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

groq_api_token = os.getenv("GROQ_API_TOKEN")

@app.get("/status")
async def get_status():
    return {"status": "ok"}

@app.post("/chat")
async def chat(prompt: str):
    headers = {"Authorization": f"Bearer {groq_api_token}"}
    # Logique pour interagir avec l'API Groq en utilisant le jeton
    # par exemple, faire une requête à l'API Groq ici
    return {"response": "Réponse de l'API Groq"}
