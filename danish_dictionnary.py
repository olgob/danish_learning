import json
import numpy as np

class dictionnary():

    def __init__(self):
        self.dictionnary = {}

    def add_word(self, word, translation):
        '''Add a word in danish and its tranlation in French'''
        if word in self.dictionnary.keys():
            return -1
        else:
            self.dictionnary[word] = translation
            return 0

    def save(self, filename):
        '''Save the dictionnary to a textfile'''
        with open(filename, 'w') as file:
            file.write(json.dumps(self.dictionnary))  # use `json.loads` to do the reverse

    def load(self, filename):
        '''Load a dictionnary from a textfile'''
        self.dictionnary = json.load(open(filename))

    def get_danish_word(self):
        '''Get a random word in danish from the dictionnary'''
        n = np.random.randint(0, len(self.dictionnary))
        keys = list(self.dictionnary.keys())  # in python 3, you'll need `list(i.keys())`
        return keys[n]

    def get_french_word(self):
        n = np.random.randint(0, len(self.dictionnary))
        values = list(self.dictionnary.values())
        return values[n]

    def check_words(self, danishWord, frenchWord):
            if frenchWord == self.dictionnary[danishWord]:
                print(True)
            else:
                print(False)

# my_dictionnary = dictionnary()
# my_dictionnary.add_word('lille', 'petit')
# my_dictionnary.add_word('stor', 'grand')
# my_dictionnary.add_word('lille', 'petit')
# my_dictionnary.save('file.txt')