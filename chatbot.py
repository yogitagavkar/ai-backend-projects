import panel as pn
import param
from rag_pipeline import load_db

class cbfs(param.Parameterized):
    chat_history = param.List([])
    answer = param.String("")
    db_query = param.String("")
    db_response = param.List([])

    def __init__(self, **params):
        super().__init__(**params)
        self.panels = []
        self.loaded_file = "sample.pdf"
        self.qa = load_db(self.loaded_file, "stuff", 4)

    def convchain(self, query):
        if not query:
            return pn.WidgetBox()

        result = self.qa.invoke({"question": query})

        self.chat_history.append((query, result["answer"]))
        self.answer = result["answer"]

        self.panels.extend([
            pn.Row('User:', pn.pane.Markdown(query, width=600)),
            pn.Row('Bot:', pn.pane.Markdown(self.answer, width=600))
        ])

        return pn.WidgetBox(*self.panels, scroll=True)

    def clr_history(self, event=None):
        self.chat_history = []