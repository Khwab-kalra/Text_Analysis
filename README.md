# Web Scraping and Basic Data Analysis Project

This project focuses on web scraping data from websites and performing basic data analysis using Python libraries such as NLTK, Pandas, NumPy, and Beautiful Soup.

## Overview

The main objective of this project is to scrape data from various websites and perform basic text analysis. Key parameters like positivity score, negativity score, and complex words are calculated using NLTK for text processing. Beautiful Soup is used for web scraping tasks.

## Challenges Faced

During the development of this project, several challenges were encountered:

- Variations in HTML structure across different web pages.
- Issues with links not working or containing text in different div classes.
- Difficulty in reading files containing special characters not supported by Python.
- Lack of a robust structure to handle different scenarios universally.

## Approach

The project primarily utilizes Beautiful Soup for web scraping and NLTK for word tokenization and text processing. Although the code has been made to work for the provided set of URLs, creating a globally applicable and fail-safe structure remains a challenge.

## Execution Steps

1. Install the required libraries listed in `requirements.txt`.
2. Change the base directory to the folder containing all the code and input files.
3. Run the `main.py` file.
4. The output will be stored in a file named `output.xlsx`. Ensure that there is no pre-existing file with the same name, as data is appended in a loop and the file is not replaced.
