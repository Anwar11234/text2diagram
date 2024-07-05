import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from examples import examples
from system_message import sys_msg

# Load environment variables from .env file
load_dotenv()

# Get the Groq API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set")

# FastAPI app initialization
app = FastAPI()

# Define the input data model
class PromptRequest(BaseModel):
    input: str
    model: str = "llama"  # Default model is LLaMA

def get_final_prompt():
    example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}")
            ]
        )

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples
    )

    # Final prompt template
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", sys_msg),
            few_shot_prompt,
            ("human", "{input}")
        ]
    )

    return final_prompt

def get_model_response(model , input_text):
    models = {
        "mixtral": "mixtral-8x7b-32768",
        "llama": "llama3-70b-8192"
    }

    final_prompt = get_final_prompt()
    chat = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=models[model], temperature=0.2)
    output_parser = StrOutputParser()
    chain = final_prompt | chat | output_parser
    return chain.invoke({"input": input_text})

def format_response(response: str) -> str:
    # Replace '\n\n' with two new lines to keep paragraph breaks
    formatted_response = response.replace('\\n\\n', '\n\n')
    
    # Replace '\\n' with a single new line to maintain line breaks
    formatted_response = formatted_response.replace('\\n', '\n')
    
    return formatted_response

@app.post("/generate-response/")
async def generate_response(request: PromptRequest):
    input_text = request.input
    model_choice = request.model.lower()

    response = get_model_response(model_choice , input_text)
    return {"response": format_response(response)}

# To run the FastAPI app, use:
# uvicorn main:app --reload