import reflex as rx
import os
import asyncio
from openai import AsyncOpenAI


class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    @rx.event
    async def answer(self):
        answer = "Unfortunately, I don't have a brain right now. add a llm library to get me a brain so you can chat with me. " \
        "Unfortunately, I don't have a brain right now. add a llm library to get me a brain so you can chat with me."
        self.chat_history.append((self.question, answer))
        self.question = ""
        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.03)
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i+1]
            )
            yield
