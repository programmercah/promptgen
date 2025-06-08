from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class ScriptInput(BaseModel):
    script: str

@app.post("/generate")
async def generate_prompts(data: ScriptInput):
    prompt = f"Extract all characters and generate descriptions based on this script:\\n\\n{data.script}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who extracts characters and describes them based on a script."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return {"result": response['choices'][0]['message']['content']}
