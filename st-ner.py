import streamlit as st
import spacy
from spacy import displacy
import html

# Load your trained model
nlp = spacy.load("/home/veena/Desktop/info_extra/job_description/trained_model1")

st.title("Skill and Information Extraction")
st.write("Enter text below to extract named entities:")

# Text input
user_input = st.text_area("Text Input", "Type some text here...")

if st.button("Analyze"):
    if user_input:
        # Process the text with the loaded NER model
        doc = nlp(user_input)
        
        # Generate HTML visualization
        html = displacy.render(doc, style="ent", page=False)
        
        # Display the annotated text
        st.write(html, unsafe_allow_html=True)
        
        # Optionally, still list the entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            st.write("Entities found:")
            for entity in entities:
                st.write(f"Text: {entity[0]}, Label: {entity[1]}")
        else:
            st.write("No entities found.")
    else:
        st.write("Please enter some text for analysis.")
