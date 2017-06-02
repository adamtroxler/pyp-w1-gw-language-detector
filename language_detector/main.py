# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
from collections import defaultdict

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    count = defaultdict(int)
    # create empty dict with default count at 0
    
    text = text.lower().split()
    # lowercase and split strings
    
    for word in text:
        for language in languages:
        # for each language in the language list
            for item in language['common_words']:
            # for each word in the common_words list
                if item == word:
                    count[language['name']] += 1
                    # pass the language to the count dictionary and increment the count
                    
    maxWord = 0
    maxLanguage = 0
    for language, total in count.items():
        if total > maxWord:
            maxWord = total
            maxLanguage = language
    return maxLanguage
   
