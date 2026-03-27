import numpy as np
import tensorflow as tf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "model" / "tflite" / "rsg_model.tflite"


class TemplateClassifier:

    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path=str(MODEL_PATH))
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self, embedding):

        embedding = np.array([embedding], dtype=np.float32)

        self.interpreter.set_tensor(
            self.input_details[0]['index'],
            embedding
        )

        self.interpreter.invoke()

        output = self.interpreter.get_tensor(
            self.output_details[0]['index']
        )

        template_index = int(np.argmax(output))

        return template_index