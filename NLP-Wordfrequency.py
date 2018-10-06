from __future__ import division
from collections import Counter
import nltk, re, pprint,os
import re

indir = '//ds.strath.ac.uk/hdrive/21/kqb16121/cis/windows/Desktop/ICCRC/neutra'
outdir = '//ds.strath.ac.uk/hdrive/21/kqb16121/cis/windows/Desktop/output/frequency_neutra.txt'
output = ''
wordfound = []
noofwords = []
word_frequencies = []
for subdir, dirs, files in os.walk(indir): #loop sub directory in a folder
    for file in files: #loop files in a folder
         filepath = subdir + os.sep + file    
         content = open(filepath,'rU',encoding="utf-8")           #open a file read, Universal 
         print('===============================================================================================')
         for line in content:                    # loop throught the content of the file
            text1 = line.strip()                # get the string content of the file
            noofwords.extend( nltk.word_tokenize(text1.lower()) )    #convert content to list of words
            print(file)
frequentwords = Counter(noofwords).most_common(1000)
for  match in frequentwords:
     if(len(match[0]) >=3):
           output += "{}  {}".format(match[0] , match[1]) +"\n" 
#print(output)
text_file = open(outdir, "w+",encoding="utf-8")
text_file.write(output)
     #output = ''
                #print('{}'.format(match))
            #print('words found') 
            #for word in noofwords:                      #loop through the list of words to get frequently used words
            #   if word not in wordfound and len(word) >= 3:                   #if a word match frequently used word
            #       wordfound += [word]                  # create a list containing the frequencies from each files
            #print(wordfound)
