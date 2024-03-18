from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import preprocessing
import os
import variables
import utilities
import numpy as np

os.chdir('D:\\speed track - PhD\\codebase\\BlackCoffer\\')
Input = pd.read_excel("Input.xlsx")

def Main():
    for Index in range(len(Input)):
        preprocessing.extract(Input,index=Index)
        file_path = Input.iloc[Index,0] +'.txt'
        print("Reading " + file_path + '.......')
        try:
            with open(file_path) as f:
                content = f.read()
        except FileNotFoundError:
            utilities.save([Input.iloc[Index,0], Input.iloc[Index,1], None, None, None, None, None, None, None, None, None, None, None, None, None])
            continue
        sentence_count = utilities.CountSentences(file_path)
        text = preprocessing.remove_stop_words(file_path)
        word_count = len(text)
        positive_score = variables.PositiveScore(text)
        negative_score = variables.NegativeScore(text)
        polarity_score = (positive_score-negative_score)/((positive_score+negative_score)+0.000001)
        subjectivity_score = (positive_score+negative_score)/((word_count)+0.000001)
        average_sentence_length = word_count/sentence_count
        complex_count_vec = np.vectorize(variables.CountComplex,otypes=[np.ndarray])
        multi_count = complex_count_vec(text)
        complex_count =  sum(count[0] for count in multi_count)
        char_count = sum(count[1] for count in multi_count)
        syllable_count = sum(count[2] for count in multi_count)
        per_complex_words = complex_count/word_count
        fog_index = 0.4*(average_sentence_length + per_complex_words)
        average_words_per_sentence = word_count/sentence_count
        average_word_length = char_count/word_count
        pronoun_count = variables.CountPronouns(text)
        utilities.save([Input.iloc[Index,0], Input.iloc[Index,1], positive_score, negative_score, polarity_score, subjectivity_score, average_sentence_length, per_complex_words, fog_index, average_words_per_sentence, complex_count, word_count, syllable_count, pronoun_count, average_word_length])


if __name__ == "__main__":  
    openpyxl.Workbook().save('output.xlsx')
    utilities.save(["URL ID", "URL", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE", "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX", "AVG NUMBER OF WORDS PER SENTENCE", 
                    "COMPLEX WORD COUNT", "WORD COUNT", "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"])

    Main()
    