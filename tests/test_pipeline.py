import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.encoding.use_lite_encoder import LiteEncoder
from src.summary_generator.template_classifier import TemplateClassifier
from src.summary_generator.slot_filler import SlotFiller


profile = {
    "name": "Rahul Sharma",
    "position": "Backend Engineer",
    "years_experience": 3,
    "skills": "Python, Django, APIs"
}

text = "Rahul Sharma is a Backend Engineer with 3 years experience in Python and Django."

encoder = LiteEncoder()
classifier = TemplateClassifier()
filler = SlotFiller()

embedding = encoder.encode(text)

template_index = classifier.predict(embedding)

summary = filler.fill(template_index, profile)

print("Generated Summary:")
print(summary)