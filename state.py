#state.py
import reflex as rx
import os
import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.chat_models import ChatOllama
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide useful response to the user's queries"),
        ("user", "Question: {question}")
    ]
)

llm = OllamaLLM(model="llama3.2", streaming=True)
parser = StrOutputParser()
chain = prompt | llm | parser

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    @rx.event
    async def answer(self):
        self.chat_history.append((self.question, ""))
        question_copy = self.question
        self.question = ""
        yield

        async for chunk in chain.astream({"question": question_copy}):
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                self.chat_history[-1][1] + chunk
            )
            yield
