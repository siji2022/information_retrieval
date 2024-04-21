# from HF "what can transformers do?""

from transformers import pipeline
from striprtf.striprtf import rtf_to_text
import os
import pandas as pd
import torch
        


    

questions = [
             # when
             "Which day, month and year did the crime happen?", 
             "what time of the day did the crime happen?",
             "Did the crime happen in the morning, afternoon,  evening or night?",
             "Did the crime happend on a weekday, weekend or holidays?",
             # what
             "What type of crime?", 
             "What is the type of the crime?",
             "Is the crime violent or non-violent?", 
             "Use 5 key words to describe this crime.",
             "Map the crime to the crime type: theft, homicide, sex abuse, robbery, burglary",
            #  "choose the crime to the crime type: theft, homicide, sex abuse, robbery, burglary",
             # where
             "In what location did the crime happend?",
             "Give me the accurate location of the crime.",
             "Did the crime happen in a public or private place?",
             "Did the crime happen in a residential or commercial area?",
             "Did the crime happen indoors or outdoors?",
             ]




model='facebook/bart-large-cnn' # bad
# model='sshleifer/distilbart-cnn-12-6' # default
# model='google-t5/t5-base' # bad
# model='openai-community/gpt2' # not working
model='google/flan-t5-base' # ok
model='google/flan-t5-large' 
# model='tiiuae/falcon-7b' # not working
# model='starmpcc/Asclepius-Llama2-7B' # not working
# model='meta-llama/Llama-2-7b-hf' # can't access
pipe = pipeline("text2text-generation", device=1,  model=model, truncation=False,max_new_tokens=10)



id=0
# get all files under 'data/news'
folder = './data/news'
# total number of files
total_files=len(os.listdir(folder))
result={}
try:
    for idx in range(total_files):
        with open(f'{folder}/washington_post_{idx}.txt') as infile:
            article=infile.read()
            
        for question_id in range(len(questions)):
            prompt =f'''
            Answer the question using the context below. 
            Question: {questions[question_id]}
            Context:{article}'''

            r=pipe(prompt)
            title = article.split('\n')[1]
            # check if result has key id
            if id not in result:
                result[id]=[title, r[0]['generated_text']]
            else:
                result[id].append( r[0]['generated_text'])
            # clean the cuda memory
            torch.cuda.empty_cache()
        id=id+1
        # if id>10:
        #     break
except:
    pass
# save results as csv
df = pd.DataFrame(result).T
df.columns=['Title']+[f'Q:{questions[i]}' for i in range(len(questions))]
df.to_csv(f'./data/results_{model.split("/")[1]}.csv')