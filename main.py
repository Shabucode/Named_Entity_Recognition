import spacy
#python -m spacy download en_core_web_sm  # Download the English language model

# Load the English language model in SpaCy
nlp = spacy.load("en_core_web_sm")

# Sample text for NER
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976."

# Process the text with SpaCy NLP pipeline
doc = nlp(text)

# Print recognized entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)
