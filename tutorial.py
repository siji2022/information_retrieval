# from HF "what can transformers do?""

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
r=classifier("I've been waiting for a HuggingFace course my whole life.")
print(r)

r=classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)
print(r)

classifier = pipeline("zero-shot-classification")
r=classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
print(r)


generator = pipeline("text-generation")
r=generator("In this course, we will teach you how to")
print(r)



generator = pipeline("text-generation", model="distilgpt2")
r= generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print (r)

unmasker = pipeline("fill-mask")
r=unmasker("This course will teach you all about <mask> models.", top_k=2)
print(r)

ner = pipeline("ner", grouped_entities=True)
r= ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(r)

question_answerer = pipeline("question-answering")
r= question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
print(r)


summarizer = pipeline("summarization")
r=summarizer(
    """
    America has changed dramatically during recent years. Not only has the number of 
    graduates in traditional engineering disciplines such as mechanical, civil, 
    electrical, chemical, and aeronautical engineering declined, but in most of 
    the premier American universities engineering curricula now concentrate on 
    and encourage largely the study of engineering science. As a result, there 
    are declining offerings in engineering subjects dealing with infrastructure, 
    the environment, and related issues, and greater concentration on high 
    technology subjects, largely supporting increasingly complex scientific 
    developments. While the latter is important, it should not be at the expense 
    of more traditional engineering.

    Rapidly developing economies such as China and India, as well as other 
    industrial countries in Europe and Asia, continue to encourage and advance 
    the teaching of engineering. Both China and India, respectively, graduate 
    six and eight times as many traditional engineers as does the United States. 
    Other industrial countries at minimum maintain their output, while America 
    suffers an increasingly serious decline in the number of engineering graduates 
    and a lack of well-educated engineers.
"""
)
print(r)

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
r=translator("Ce cours est produit par Hugging Face.")
print(r)