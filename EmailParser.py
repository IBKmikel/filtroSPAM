import email
import re
import nltk
from QuitarHTML import QuitarHTML
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
from nltk.corpus import stopwords


class EmailParser():
    def __init__(self):
        pass

    def parser(self, email):
        # Obtenemos el cuerpo del email
        body_correo = " ".join(self.obtener_body(email))
        # Eliminar los tags html
        body_correo = self.quitar_tags(body_correo)
        # Eliminar las urls
        body_correo = self.remove_urls(body_correo)
        # Transformarlo en tokens
        body_correo = word_tokenize(body_correo)
        # Eliminar stopwords
        # Eliminar puntuacion
        # Hacemos stemming
        body_correo = self.clean_email(body_correo)
        return " ".join(body_correo)

    def obtener_body(self, correo):
        msg = email.message_from_string(correo)
        return self._parse_body(msg.get_payload())

    def _parse_body(self, payload):
        body = []
        if type(payload) is str:
            return [payload]
        elif type(payload) is list:
            for p in payload:
                body += self._parse_body(p.get_payload())
        return body

    def quitar_tags(self, email):
        html_parser = QuitarHTML()
        html_parser.feed(email)
        return ''.join(html_parser.data)

    def remove_urls(self, email):
        return re.sub(r"http\S+", "", email)

    def clean_email(self, email):
        body_correo = []
        stemmer = nltk.PorterStemmer()
        punct = list(punctuation) + ["\n", "\t"]
        for word in email:
            if word not in punct and word not in stopwords.words('english'):
                body_correo.append(stemmer.stem(word))
        return body_correo
