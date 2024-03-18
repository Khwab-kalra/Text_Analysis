import nltk
import os
import string
from openpyxl import load_workbook

def SWords():
    path = 'StopWords\\'
    files = os.listdir(path)
    swords = list()
    for f in files:
        file_path = path+f
        with open(file_path) as file:
            swords.append(nltk.word_tokenize(file.read()))
    return swords

def RemovePunctuation(text):
    t_clean = [t for t in text if t not in string.punctuation]
    return t_clean 

def CountSentences(file_path):
    with open(file_path) as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    return num_sentences

def save(data):
    file_path = "output.xlsx"
    wb = load_workbook(file_path)
    ws = wb["Sheet"] 
    row_data = data
    ws.append(row_data)
    wb.save(file_path)

    print("Row of data added successfully to the Excel file.")