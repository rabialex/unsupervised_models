import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)