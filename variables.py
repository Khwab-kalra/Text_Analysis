from nltk import word_tokenize
import numpy as np
import re


def PositiveScore(text):
    positive_score = 0
    file_path = 'MasterDictionary\\positive-words.txt'
    with open(file_path) as file:
        tokens = word_tokenize(file.read())

    for word in text:
        if word in tokens:
            positive_score+=1    
    return positive_score

def NegativeScore(text):
    negative_score = 0
    file_path = 'MasterDictionary\\negative-words.txt'
    with open(file_path) as file:
        tokens = word_tokenize(file.read())

    for word in text:
        if word in tokens:
            negative_score+=1    
    return negative_score

def CountComplex(word):
    vowels = 'aeiou'
    count = [0,0,0]
    for char in word:
        count[1]+=1
        if char.lower() in vowels:
            count[2]+=1
    if 'ed' in word.lower() or 'es' in word.lower():
        count[2]-=1        
    if count[2] > 2:
        count[0] =1
    return count

def CountPronouns(text):
    pronouns = {"i", "we", "my", "ours", "us"}

    total_count = 0

    for word in text:
        if word.lower() in pronouns and word != 'US':
            total_count += 1

    return total_count
