# chatapp.py
import reflex as rx

from ai_chat import style
from ai_chat.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(question, style=style.question_style),
            align_self="flex-end",  # 👈 Aligns right
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            # align_self="flex-start",  # 👈 Aligns left
        ),
        width="69vw",
        spacing='1' 
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


# chatapp.py
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask Anything",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            rx.icon("send-horizontal"),
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
            spacing="5",
            # width="100vw",
            # min_height="100vh",
            padding="1em",
        ),
        width="100vw",
        min_height="100vh",
        bg="#121B1D",
    )


app = rx.App(theme=rx.theme(color_mode="dark", accent_color="mint"))
app.add_page(index)
