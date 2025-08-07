# style.py
import reflex as rx

# Common styles for questions and answers.
chat_margin = "0%"
message_style = dict(
    padding="0.9em",
    border_radius="19px",
    # margin_y="0.5em",
    # max_width="100em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    # margin_right=chat_margin,
    background_color="#1F2E30",
    max_width="39em",
)
answer_style = message_style | dict(
    # margin_right=chat_margin,
    max_width="100em"
)

# Styles for the action bar.
input_style = dict(
    background_color="#12315200",
    border_width="1px",
    border_radius="20px",
    width="845px",
    height="45px",
)
button_style = dict(
    # background_color="#288C9D",
    border_radius="20px",
    height="45px",
    width="55px",
)
