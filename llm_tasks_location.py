# from HF "what can transformers do?""

from transformers import pipeline




# question_answerer = pipeline("question-answering",model="distilgpt2")
# r= question_answerer(
#     question="Work location?",
#     context="My name is Sylvain and I work at Hugging Face in Brooklyn",
# )
# print(r)

# ner = pipeline("ner", grouped_entities=True)
# r= ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
# print(r)

# read from rtf file


from striprtf.striprtf import rtf_to_text

with open('./data/washington-post/Factiva-20240324-2204.rtf') as infile:
    content = infile.read()
    text = rtf_to_text(content)
preview=text[:1000]
# print(preview)

summarizer = pipeline("summarization")
r=summarizer(preview)
print(r)

