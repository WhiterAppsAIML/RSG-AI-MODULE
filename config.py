from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
LABELED_DATA_DIR = DATA_DIR / "labeled"

MODEL_DIR = BASE_DIR / "model"
SUMMARY_MODEL_DIR = MODEL_DIR / "summary_model"
TFLITE_DIR = MODEL_DIR / "tflite"

SRC_DIR = BASE_DIR / "src"
RUBRICS_DIR = BASE_DIR / "rubrics"

TEMPLATES_FILE = RUBRICS_DIR / "summary_templates.json"

USE_MODEL_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"