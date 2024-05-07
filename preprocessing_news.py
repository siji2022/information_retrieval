from transformers import pipeline
from striprtf.striprtf import rtf_to_text

# remove all files under data/news
import os
import shutil
folder = './data/news/'
shutil.rmtree(folder)
os.mkdir(folder)
        
        
        
all_files=['Factiva-20240324-2159.rtf', 'Factiva-20240324-2200.rtf','Factiva-20240324-2201.rtf',
           'Factiva-20240324-2202.rtf',
           'Factiva-20240324-2203.rtf',
           'Factiva-20240324-2204.rtf']

id=0
for file in all_files:
    print(f'Processing file {file}')
    with open(f'./data/washington-post/{file}') as infile:
        content = infile.read()
        text = rtf_to_text(content)
        # split the text into articles
        articles = text.split('http://www.washingtonpost.com')
        for article in articles:
            # find 'Metro' in the article, remove everything before it
            if 'Metro' in article:
                article=article[article.find('Metro'):]
                article=article.strip()
                if len(article)>10:
                    with open(f'./data/news/washington_post_{id}.txt', 'w+') as outfile:
                        outfile.write(article)
                id=id+1
    


