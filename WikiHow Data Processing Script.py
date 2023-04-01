#!/usr/bin/env python
# coding: utf-8

'''
This code is used to create article and summary files from the csv file.
The output of the file will be a directory of text files representing separate articles and their summaries.
Each summary line starts with tag "@summary" and the article is followed by "@article".
'''
import pandas as pd
import os
import re
import csv

# read data from the csv file (from the location it is stored)
Data = pd.read_csv(r'wikihowSep.csv')
Data = Data.astype(str)
rows, columns = Data.shape

# create a file to record the file names. This can be later used to divide the dataset in train/dev/test sets
title_file = open('titles.txt', 'wb')

# The path where the articles are to be saved
path = "articles"
if not os.path.exists(path): os.makedirs(path)

# go over all the articles in the data file
for row in range(rows):
    abstract = Data.loc[row, 'headline']      # headline is the column representing the summary sentences
    article = Data.loc[row, 'text']           # text is the column representing the article

    # a threshold is used to remove short articles with long summaries as well as articles with no summary
    if len(abstract) < (0.75 * len(article)):
        # remove extra commas in abstracts
        abstract = abstract.replace(".,", ".")
        abstract = abstract.encode('utf-8')
        # remove extra commas in articles
        article = re.sub(r'[.]+[\n]+[,]', ".\n", article)
        article = article.encode('utf-8')

        # a temporary file is created to initially write the summary, it is later used to separate the sentences of the summary
        with open('temporaryFile.txt', 'wb') as t:
            t.write(abstract)

        # file names are created using the alphanumeric characters from the article titles.
        # they are stored in a separate text file.
        filename = Data.loc[row, 'title']
        filename = "".join(x for x in filename if x.isalnum())
        filename1 = filename + '.txt'
        filename = filename.encode('utf-8')
        title_file.write(filename + b'\n')

        with open(os.path.join(path, filename1), 'wb') as f:
            # summary sentences will first be written into the file in separate lines
            with open('temporaryFile.txt', 'r') as t:
                for line in t:
                    line = line.lower()
                    if line != "\n" and line != "\t" and line != " ":
                        f.write(b'@summary' + b'\n')
                        f.write(line.encode('utf-8'))
                        f.write(b'\n')

            # finally the article is written to the file
            f.write(b'@article' + b'\n')
            f.write(article)

title_file.close()

# Function to extract summary and article content from the text
def extract_content(text):
    summary_start = text.find('@summary') + len('@summary\n')
    summary_end = text.find('\n@article')
    summary = text[summary_start:summary_end].strip()

    article_start = text.find('@article') + len('@article\n')
    article = text[article_start:].strip()

    return summary, article

# Directory containing your .txt files
input_directory = 'articles'

# CSV file where you want to store the extracted data
output_csv = 'output2.csv'

with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Summary', 'Article'])

    for file in os.listdir(input_directory):
        if file.endswith('.txt'):
            with open(os.path.join(input_directory, file), 'r', encoding='utf-8') as txt_file:
                text = txt_file.read()
                summary, article = extract_content(text)
                csv_writer.writerow([summary, article])

