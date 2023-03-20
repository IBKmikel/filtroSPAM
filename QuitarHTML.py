from html.parser import HTMLParser

class QuitarHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        # Atributo
        self.data = []

    def handle_data(self, data):
        self.data.append(data)