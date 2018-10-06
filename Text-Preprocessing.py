from __future__ import division
from collections import Counter
import re
import pprint
import os
import re
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
def processText(text):
    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word

    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words

    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    #stemming
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in words]
    return stemmed[:100]


indir = '//ds.strath.ac.uk/hdrive/21/kqb16121/cis/windows/Desktop/ICCRC'
outdir = '//ds.strath.ac.uk/hdrive/21/kqb16121/cis/windows/Desktop/output/'
output = ""
print('===============================================================================================')
print("Program Starting...............................................................................")
for subdir, dirs, files in os.walk(indir):  # loop sub directory in a folder
        for file in files:  # loop files in a folder

            filepath = subdir + os.sep + file  # get the file path

            content = open(filepath, 'rU', encoding="utf-8")  # open a file read, Universal
            print('Searching for word {}'.format(words))
            print(filepath)
            print('===============================================================================================')
            for line in content:  # loop through the content of the file
                text1 = line.strip()
                processText(text1)
            text_file = open(outdir + os.sep + file + ".txt", "a", encoding="utf-8")
            text_file.write(file + "-" + word + "\n")




