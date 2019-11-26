import numpy as np

class KB:
    def __init__(self, length = 0, sentences = None):
        self.length = length
        self.sentences = []
        if sentences:
            self.sentences.append(sentences)
    
    def PL_Resolution(self, alpha):
        self.clauses = self.sentences + negates(alpha)
        new = set()

        while True:
            n = len(self.clauses)

            pairs = [(self.clauses[i], self.clauses[j])
                 for i in range(n) for j in range(i + 1, n)]

            for (ci, cj) in pairs:
                resolvents = PL_Resolve(ci, cj)
                if False in resolvents:
                    return True
                new = new.union(set(resolvents))
            
            if new.issubset(set(self.clauses)):
                return False
            
            for c in new:
                if c not in self.clauses:
                    self.clauses.append(c)
    

def negates(sentence):
    new = []
    if isPosLiteral(sentence):
        new.append("-" + sentence)
    elif isNegLiteral(sentence):
        new.append(sentence[1])
    else:
        new = deMorgan(sentence)
    
    return new

def isPosLiteral(sentence):
    return len(sentence) == 1 and sentence.isalpha()

def isNegLiteral(sentence):
    return len(sentence) == 2 and sentence[0] == "-" and sentence[1].isalpha()

def smallDeMorgan(sentence):
    #alpha = "(A OR B) AND C" ???
    
    #"A OR B" => ['A', 'OR', 'B']
    #check i = 'OR' => continue
    #res = negates(A) + negates(B)

    #"-A OR B OR C"
    '''
    Simple De Morgan rule for sentence like "A OR B" or "A OR B OR C"
    '''
    tokens = sentence.split()
    res = []
    for token in tokens:
        if token == "OR":
            continue
        res.append(negates(tokens))
    
    return res

def PL_Resolve(ci, cj):
    
    ci_tokens = ci.split(' OR ')
    cj_tokens = cj.split(' OR ')
    clauses = []
    for di in ci_tokens:
        for dj in cj_tokens:
            l1 = [di]
            l2 = [dj]
            if (l1 == negates(dj) or negates(di) == l2:
                newi = [n for n in ci_tokens if n != di]
                newj = [n for n in cj_tokens if n != dj]
                clauses.append(newi + newj)
    
    return clauses
 
def read_input(path):
    '''
    Read the input file and store the query alpha and knowledge base KB

    Parameters:
        path: directory to the input file
    '''
    file = open(path, 'r')
    
    if file.mode == 'r':
        alpha = file.readline()
        KB_len = int(file.readline())
        KB_sentences =  []
        for i in range(KB_len):
            KB_sencences.append(file.readline())
    
    return alpha, KB_sentences

def write_output(file, buffer):
    #buffer contains results
    #write buffer to file

