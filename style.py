# style.py
import reflex as rx

# Common styles for questions and answers.
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="17px",
    margin_y="0.5em",
    max_width="42em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
)

# Styles for the action bar.
input_style = dict(
    border_width="1px",
    border_radius="20px",
    width="700px",
    height="45px",
)
button_style = dict(
    background_color="#288C9D",
    border_radius="20px",
    height="45px",
    width="55px",
)
