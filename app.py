import streamlit as st

from src.encoding.use_lite_encoder import LiteEncoder
from src.summary_generator.template_classifier import TemplateClassifier
from src.summary_generator.slot_filler import SlotFiller


st.title("AI Resume Summary Generator")

name = st.text_input("Name")
position = st.text_input("Job Role / Position")
experience = st.number_input("Years of Experience", min_value=0, max_value=30, step=1)
skills = st.text_input("Skills (comma separated)")
skills_list = [s.strip() for s in skills.split(",") if s.strip()]

if len(skills_list) > 1:
    skills_text = ", ".join(skills_list[:-1]) + " and " + skills_list[-1]
else:
    skills_text = skills
institution = st.text_input("Institution / Company")

if st.button("Generate Summary"):
    
    if experience <= 1:
        level = "fresher"
    elif experience <= 4:
        level = "early"
    else:
        level = "experienced"
    
    profile = {
        "name": name,
        "position": position,
        "years_experience": experience,
        "skills": skills_text,
        "institution": institution,
        "domain_area": position,
        "experience_level": level
    }

    text = f"{name} is a {position} with {experience} years of experience in {skills}"

    encoder = LiteEncoder()
    classifier = TemplateClassifier()
    filler = SlotFiller()

    embedding = encoder.encode(text)

    template_index = classifier.predict(embedding)

    summary = filler.fill(template_index, profile)

    st.subheader("Generated Professional Summary")
    st.write(summary)