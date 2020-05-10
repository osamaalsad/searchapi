from django.db.models import Q
from django.views.generic import TemplateView, ListView
import numpy as np
from searchapi.models import Category, SearchingData, UnknownSearch
from spellchecker import SpellChecker
import re
from nltk.stem import PorterStemmer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

class Preprocess:
    # Fix the words length
    def reduce_lengthening(text):  # problem
        pattern = re.compile(r"(.)\1{2,}")
        text = pattern.sub(r"\1", text)
        return text

    # Clean the symbol form data
    def cleanSymbol(query):
        symbols = "!\"#$%&()*+-/:;<=>?@[\]^_`{|}~\n"
        for i in symbols:
            query = np.char.replace(query, i, '')
        return str(query)

    # Check the words spilling
    def spellChecker(query):
        spell = SpellChecker()
        newtext = str()
        size = len(query)
        misspelled = spell.unknown(query.split())
        for word in misspelled:
            newtext += spell.correction(word)
        if len(newtext) != 0:
            return newtext
        else:
            return query

    # Remove dot '.' and fix words
    def wildcard(query):
        file = open("../WordList.txt", 'r')
        wordlist = file.read().split('\n')
        List = query.split(' ')
        s = str()
        s2 = str()
        for i in List:
            for word in wordlist:
                if re.search(i, word):
                    if len(i) == len(word):
                        s += word
            if len(s) != 0:
                s2 += s + " "
                s = ""
            else:
                s2 += i + " "
        file.close()
        return s2

    # Return the word to its root
    def limitazation(query):
        porter = PorterStemmer()
        temp = query.split()
        s = str()
        for i in temp:
            s += " " + porter.stem(i)
        return s

    # Remove stop words
    def stopWord(query):
        text1 = word_tokenize(query)
        text2 = [word for word in text1 if not word in stopwords.words()]
        s = str()
        for i in text2:
            s += i + " "
        return s

    # If there is no result from the real string that entered by user this function will run to search word by word
    def ifNoResult(object_list1, newstring, oldstring):
        newstring = newstring.split(' ')
        oldstring = oldstring.split(' ')
        object_list = list()
        for i in newstring:
            for data in object_list1:
                if i in data.Name.lower() or i in data.Description:
                    object_list.append(data)
        for i in oldstring:
            for data in object_list1:
                if i in data.Name.lower() or i in data.Description:
                    object_list.append(data)
        return object_list