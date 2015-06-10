__author__ = 'esevre'

import matplotlib.pyplot as plt
from nltk.book import *


def get_title(text):
    start_char = '['
    end_char = ']'
    # check title[0] = '['
    if text[0] != start_char:
        return ['unknown']
    i = 1
    title = []
    while text[i] != end_char:
        title.append(text[i])
        i += 1
    return title

def get_title_string(text):
    title = get_title(text)
    title_string = ""
    for word in title:
        title_string += word + " "
    return title_string


text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
lex_div_list = []
length_list = []

for text in text_list:
    length_list.append(len(set(text)))
    lex_div_list.append(len(set(text))/len(text))
    #lex_div_ratio = len(set(text))/len(text)
    #print(get_title_string(text) + ": " + str(lex_div_ratio))

plt.figure("Length vs Lexical Diversity")
plt.plot(length_list, lex_div_list, 'ob')
plt.show()


'''
myword = "whale"
width = 7
for i, word in enumerate(text1):
    length = len(text1)
    if word == myword:
        if i < width & length - i < width:
            print(text1)
        if i < width:
            print(text1[0:i+width])
        if length - i < width:
            print(text1[i-width:-1])
        if i > width:
            print(text1[i-width:i+width])

'''




