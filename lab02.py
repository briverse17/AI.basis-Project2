import numpy as np

class KB:

    def __init__(self, length = 0, sentences = None):
        self.length = length
        self.sentences = []
        if sentences:
            self.sentences.append(sentences)
    
def read_input(path):
    '''
    Read the input file and store the query alpha and knowledge base KB

    Parameters:
        path: directory to the input file
    '''
    file = open(path, 'r')
    
    if file.mode = 'r':
        alpha = file.readline()
        KB_len = int(file.readline())
        KB_sentences =  []
        while KB_len > 0:
            KB_sencences.append(file.readline())
            KB_len -= 1

def write_output(file, buffer):
    #buffer contains results
    #write buffer to file