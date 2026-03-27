import tensorflow_hub as hub
from config import USE_MODEL_URL


class LiteEncoder:

    def __init__(self):
        self.model = hub.load(USE_MODEL_URL)

    def encode(self, text):

        embedding = self.model([text])[0].numpy()

        return embedding