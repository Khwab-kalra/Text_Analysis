from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
from nltk import word_tokenize
import utilities
def extract(input, index):
    print("Extracting data........")
    url = input.iloc[index,1]
    file_name = input.iloc[index,0]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    div_text = soup.find('div', class_="td-post-content tagdiv-type")
    div_title = soup.find('h1')
    if(div_text == None):
        div_text = soup.find('div', class_="tdi_130")
        if(div_text == None):
            return
    pre_tag = div_text.find('pre', class_='wp-block-preformatted')
    if pre_tag:
        pre_tag.extract()
    if(div_title == None):
        extracted_title = ""    
    else:
        extracted_title = div_title.get_text(separator=' ', strip=True).split()
    if('' in div_text.get_text()):
        extracted_text = div_text.get_text(separator=' ', strip=True).replace('', ' ').split()
    elif('″' in div_text.get_text()):
        extracted_text = div_text.get_text(separator=' ', strip=True).replace('″', ' ').split()
    elif('₹' in div_text.get_text()):
        extracted_text = div_text.get_text(separator=' ', strip=True).replace('₹', ' ').split()
    else:
        extracted_text = div_text.get_text(separator=' ', strip=True).split()

    file_path = str(file_name)+'.txt'
    with open(file_path, 'w') as file:
        for text in extracted_title:
            file.write(text + '\n')
        for text in extracted_text:
            file.write(text + '\n')

def remove_stop_words(file_path):
    print("Removing stop words.........")
    with open(file_path, 'r') as file:
        tokens = word_tokenize(file.read())
    stop_words = utilities.SWords()
    tokens = utilities.RemovePunctuation(tokens)
    text = list()
    for token in tokens:
        if token.upper() in stop_words:
            pass
        else:
            text.append(token)
    return text
