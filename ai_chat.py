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
            rx.markdown(answer, style=style.answer_style, highlight=True),
            # align_self="flex-start",  # 👈 Aligns left
        ),
        width="69vw",
        spacing="1",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def chat_scroll_area() -> rx.Component:
    return rx.box(
        chat(),
        id="chat-scroll",
        # height="100vh",
        padding="1rem",
        padding_bottom="3.7rem",   # reserve space for the fixed action bar
        overflow_y="auto",
        # width="100%",
        overflow_x="hidden",     # prevent horizontal overflow
    )

# chatapp.py
def action_bar() -> rx.Component:
    return rx.box(
        rx.hstack(
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
            width="min(100%, 860px)",
            margin_x="auto",
            spacing="2",
        ),
        position="fixed",
        bottom="0",
        left="0",
        right="0",
        width="100%",
        padding="0.4rem",
        # padding_bottom="0.3rem",
        bg="#121B1D",
        border_top="0px solid #233136",
        z_index="10",
    )


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            chat_scroll_area(),
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
