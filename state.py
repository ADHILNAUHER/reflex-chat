#state.py
import reflex as rx
import requests
from huggingface_hub import InferenceClient
import os
import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING"] = "true"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

client = InferenceClient(model=MODEL_ID, token=HUGGINGFACE_TOKEN)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are BuddyAI, a concise and helpful AI assistant. When answering questions, provide clear"
        "and complete responses that are medium in length — not too short or too long."
        "Avoid unnecessary explanations or extra details unless the user asks for more."),
        ("user", "Question: {question}")
    ]
)

parser = StrOutputParser()
chain = prompt | parser

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    @rx.event
    async def answer(self):
        self.chat_history.append((self.question, ""))
        question_copy = self.question
        self.question = ""
        yield

        formatted = prompt.invoke({"question": question_copy}).to_string()

        # Streaming response
        response_text = ""
        stream = await asyncio.to_thread(
            client.chat_completion,
            messages=[{"role": "user", "content": formatted}],
            stream=True,
            max_tokens=2400,
            model=MODEL_ID
        )
        for token in stream:
            fragment = token.choices[0].delta.content or ""
            response_text += fragment
            self.chat_history[-1] = (question_copy, response_text)
            yield
