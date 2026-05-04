import helper
import panel as pn
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

pn.extension(
    sizing_mode="stretch_width",
    notifications=True
)

# Store conversation panels
panels = []

# Theme styling
CHAT_STYLES = {
    "border-radius": "12px",
    "padding": "12px 16px",
    "margin": "8px 0px",
    "max-width": "80%",
    "word-wrap": "break-word",
    "overflow-wrap": "break-word"
}

USER_STYLE = {
    **CHAT_STYLES,
    "background": "#DCF8C6",
    "align-self": "flex-end"
}

BOT_STYLE = {
    **CHAT_STYLES,
    "background": "#F6F6F6",
    "align-self": "flex-start"
}


def collect_messages(event):
    prompt = inp.value.strip()

    if not prompt:
        return chat_container

    inp.value = ""

    context.append({
        'role': 'user',
        'content': prompt
    })

    response = helper.get_completion_from_messages(context)

    context.append({
        'role': 'assistant',
        'content': response
    })

    # User bubble
    panels.append(
        pn.Row(
            pn.Spacer(),
            pn.pane.Markdown(
                f"**You**  \n{prompt}",
                styles=USER_STYLE,
                width_policy="max"
            )
        )
    )

    # Assistant bubble
    panels.append(
        pn.Row(
            pn.pane.Markdown(
                f"**OrderBot 🍕**  \n{response}",
                styles=BOT_STYLE,
                width_policy="max"
            ),
            pn.Spacer()
        )
    )

    chat_container.objects = panels
    return chat_container


context = [{
    'role': 'system',
    'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant.
You greet the customer, collect the order, ask for pickup/delivery,
summarize the order, ask for final additions, collect address if delivery,
and collect payment.
Be short, friendly, and conversational.
"""
}]

# Header
header = pn.pane.Markdown("""
# 🍕 Pizza OrderBot  
### Fast, friendly, and delicious ordering
""")

# Chat area
chat_container = pn.Column(
    sizing_mode="stretch_both",
    height=500,
    scroll=True,
    styles={
        "padding": "15px",
        "background": "#FAFAFA",
        "border-radius": "12px",
        "overflow-y": "auto"
    }
)

# Input area
inp = pn.widgets.TextInput(
    placeholder="Type your order here...",
    sizing_mode="stretch_width"
)

send_button = pn.widgets.Button(
    name="Send 🚀",
    button_type="primary",
    width=120
)

send_button.on_click(collect_messages)

input_row = pn.Row(
    inp,
    send_button,
    sizing_mode="stretch_width"
)

dashboard = pn.Column(
    header,
    chat_container,
    input_row,
    sizing_mode="stretch_both",
    styles={
        "max-width": "900px",
        "margin": "0 auto",
        "padding": "20px"
    }
)

dashboard.servable()