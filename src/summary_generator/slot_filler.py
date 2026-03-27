import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
TEMPLATE_FILE = BASE_DIR / "rubrics" / "summary_templates.json"


class SafeDict(dict):
    def __missing__(self, key):
        return ""


class SlotFiller:

    def __init__(self):
        with open(TEMPLATE_FILE, "r") as f:
            data = json.load(f)

        self.templates = data["templates"]

    def fill(self, template_index, profile):
        template_index = (template_index + random.randint(0,3)) % len(self.templates)

        template = self.templates[template_index]["text"]

        summary = template.format_map(SafeDict(profile))

        extra_lines = [
            "Known for strong problem-solving ability and attention to detail.",
            "Passionate about building scalable and efficient solutions.",
            "Demonstrates strong collaboration, communication, and analytical skills.",
            "Focused on continuous learning and professional growth.",
            "Committed to delivering impactful technology solutions.",
            "Recognized for adaptability and ability to learn new technologies quickly."
        ]

        summary = summary + " " + random.choice(extra_lines)

        return summary