import reflex as rx
import asyncio
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="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"
)


class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = "A way to build web apps in pure Python! Anything from a simple website to a complex web app!"
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.02)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield
