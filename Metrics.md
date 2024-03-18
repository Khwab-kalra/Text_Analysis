# Text Analysis

The objective of this document is to explain the methodology adopted to perform text analysis to drive sentimental opinion, sentiment scores, readability, passive words, personal pronouns, and more.

## Table of Contents

1. [Sentimental Analysis](#sentimental-analysis)
   - [Cleaning using Stop Words Lists](#cleaning-using-stop-words-lists)
   - [Creating a dictionary of Positive and Negative words](#creating-a-dictionary-of-positive-and-negative-words)
   - [Extracting Derived variables](#extracting-derived-variables)
2. [Analysis of Readability](#analysis-of-readability)
3. [Average Number of Words Per Sentence](#average-number-of-words-per-sentence)
4. [Complex Word Count](#complex-word-count)
5. [Word Count](#word-count)
6. [Syllable Count Per Word](#syllable-count-per-word)
7. [Personal Pronouns](#personal-pronouns)
8. [Average Word Length](#average-word-length)

## Sentimental Analysis

Sentiment analysis is the process of determining whether a piece of writing is positive, negative, or neutral. The below algorithm is designed for use in Financial Texts. It consists of the following steps:

### Cleaning using Stop Words Lists

The Stop Words Lists (found in the folder StopWords) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in the Stop Words List.

### Creating a dictionary of Positive and Negative words

The Master Dictionary (found in the folder MasterDictionary) is used for creating a dictionary of Positive and Negative words. We add only those words to the dictionary if they are not found in the Stop Words Lists.

### Extracting Derived variables

We convert the text into a list of tokens using the nltk tokenize module and use these tokens to calculate the 4 variables described below:

- **Positive Score:** This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
- **Negative Score:** This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
- **Polarity Score:** This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
    ```
    Polarity Score = (Positive Score – Negative Score) / ((Positive Score + Negative Score) + 0.000001)
    ```
    Range is from -1 to +1
- **Subjectivity Score:** This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
    ```
    Subjectivity Score = (Positive Score + Negative Score) / ((Total Words after cleaning) + 0.000001)
    ```
    Range is from 0 to +1

## Analysis of Readability

Analysis of Readability is calculated using the Gunning Fox index formula described below:

- **Average Sentence Length:** the number of words / the number of sentences
- **Percentage of Complex words:** the number of complex words / the number of words 
- **Fog Index:** 0.4 * (Average Sentence Length + Percentage of Complex words)

## Average Number of Words Per Sentence

The formula for calculating is: Sum of the total number of characters in each word / Total number of words

