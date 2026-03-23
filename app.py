import panel as pn
from chatbot import cbfs

pn.extension()

cb = cbfs()

inp = pn.widgets.TextInput(placeholder="Ask something...")
conversation = pn.bind(cb.convchain, inp)

dashboard = pn.Column(
    pn.pane.Markdown("# ChatWithYourData Bot"),
    inp,
    pn.panel(conversation, height=400),
)

dashboard.servable()