import argparse

Literals = {'A': 1, '-A': 2, 'B': 3, '-B': 4, 'C': 5, '-C': 6, 'D': 7, '-D': 8, 'E': 9, '-E': 10, 'F': 11, '-F': 12,
            'G': 13, '-G': 14, 'H': 15, '-H': 16, 'I': 17, '-I': 18, 'J': 19, '-J': 20, 'K': 21, '-K': 22, 'L': 23, '-L': 24,
            'M': 25, '-M': 26, 'N': 27, '-N': 28, 'O': 29, '-O': 30, 'P': 31, '-P': 32 ,'Q': 33, '-Q': 34, 'R': 35, '-R': 36,
            'S': 37, '-S': 38, 'T': 39, '-T': 40, 'U': 41, '-U': 42, 'V': 43, '-V': 44, 'W': 45, '-W': 46, 'X': 47, '-X': 48,
            'Y': 49, '-Y': 50, 'Z': 51, '-Z': 52}
keys = list(Literals.keys())
values = list(Literals.values())

class KB:
    def __init__(self, sentences = None):
        self.sentences = []
        if sentences:
            self.sentences.extend(sentences)
        
        self.result = ""
    
    def PL_Resolution(self, alpha):
        '''
        Propositional Logic Resolution of KB.sentences and alpha
        '''
        self.clauses = self.sentences + negates(alpha[0])
        new = []
        while True:
            n = len(self.clauses)
            count = 0
            buf = ""

            pairs = [(self.clauses[i], self.clauses[j]) for i in range(0, n) for j in range(i + 1, n)]
            for (ci, cj) in pairs:
                resolvents = PL_Resolve(ci, cj)
                if resolvents != [] and not set(resolvents).issubset(set(self.clauses)) and not set(resolvents).issubset(set(new)) and False not in resolvents:
                    count += 1
                    buf += toCNF(resolvents)
                    new += resolvents
                if False in resolvents:
                    count += 1
                    buf += "{}\n"
            
            if set(new).issubset(set(self.clauses)):
                self.result += str(count) + '\n' + "NO\n"
                return False
            
            for c in new:
                if c not in self.clauses:
                    self.clauses.append(c)
            
            self.result += str(count) + '\n' + buf

            if "{}\n" in buf:
                self.result += "YES\n"
                return True
            
def toCNF(tuplelist):
    '''
    Convert tuples of literals to a string of the full proposition with keyword "OR"\n
    E.g.:
    \t('A', '-B', 'C') => "A OR -B OR C"
    '''
    res = ""
    if isLiteral(tuplelist[0]):
        res = tuplelist[0][0]
    else:
        for i in range(len(tuplelist)):
            for j in range(len(tuplelist[i]) - 1):
                res += tuplelist[i][j] + ' OR '
            res += tuplelist[i][len(tuplelist[i]) - 1]
    res += '\n'
    return res

def negates(proposition):
    '''
    Negates a proposition\n
    Commas of tuples represent operator OR\n
    Commas of lists represent operator AND\n
    E.g.:
    \t('A', 'B') => ['-A', '-B']\n
    \t('P') => ['-P']
    '''
    new = []
    if isLiteral(proposition):
        new.append(negatesLiteral(proposition))
    else:
        new = smallDeMorgan(proposition)
    
    return new

def negatesLiteral(literal):
    '''
    Negates a single literal\n
    E.g.:
    \t('A',) => ('-A',)\n
    \t('-O',) => ('O',)
    '''
    if isPosLiteral(literal[0]):
        return str("-" + literal[0]),
    else:
        return literal[0][1],

def isLiteral(proposition):
    '''
    Check if a proposition if a single literal\n
    '''
    if len(proposition) == 1:
        return True
    return False

def isPosLiteral(sentence):
    '''
    Check if a literal is positive
    '''
    return len(sentence) == 1 and sentence[0].isalpha()

def isNegLiteral(sentence):
    '''
    Check if a literal is negative
    '''
    return len(sentence) == 2 and sentence[0] == "-" and sentence[1].isalpha()

def smallDeMorgan(sentence):
    '''
    Simple De Morgan rule for sentence like "A OR B" or "A OR B OR C"
    '''
    res = []
    for i in sentence:
        neg_i = negatesLiteral((i,))
        res.append(neg_i)
    
    return res

def PL_Resolve(ci, cj):
    '''
    Main helper of KB.PL_Resolution()\n
    Given a pair of propostions (ci, cj), returns the "resolved" propostion from them\n
    E.g.:
    \t(('A', '-B', 'C'), ('-A',)) => [('-B', 'C')]\n
    \t(('-A', 'B'), ('A',)) => [('B',)]\n
    \t(('A', '-B', 'C'), ('B',)) => [('A', 'C')]\n
    \t(('A', '-B', 'C'), ('-C',)) => [('A', '-B')]\n
    '''
    clauses = []

    if ([ci] == negates(cj) or negates(ci) == [cj]):
        clauses.append(False)
        return clauses

    for di in ci:
        for dj in cj:
            #l1 = [di]
            #l2 = [dj]
            if ((di,) == negatesLiteral((dj,)) or negatesLiteral((di,)) == (dj,)):
                newi = [n for n in ci if n != di]
                newj = [n for n in cj if n != dj]
                new_propos = tuple(newi) + tuple(newj)
                if (isUseless(new_propos)):
                    continue
                new_propos = delDupLiteral(new_propos)
                clauses.append(sortProposition(new_propos))
    return clauses

def delDupLiteral(proposition):
    '''
    Delete duplicated literals in a proposition\n
    E.g.:
    \t('A', '-B', 'C', 'A') => ('A', '-B', 'C')
    '''
    pro = set(proposition)
    return tuple(pro)

def sortProposition(proposition):
    '''
    Sort the proposition alphabetically\n
    E.g.:
    \t('-A', 'B', 'A') => ('A', '-A', 'B')
    \t('-B', '-C', 'C') => ('-B', 'C', '-C')
    '''
    temp = []
    for i in proposition:
        temp.append(Literals[i])
    temp = sorted(temp)
    
    res = []
    for i in temp:
        res.append(keys[values.index(i)])

    res = tuple(res)

    return res

def isUseless(proposition):
    '''
    Check if a proposition is useless\n
    E.g.:
    \t('A', '-A', 'B') => True
    \t('X', 'Y', '-X') => True
    '''
    for i in range(len(proposition)):
        for j in range(i + 1, len(proposition)):
            if (proposition[i],) == negatesLiteral((proposition[j],)):
                return True
    return False

def makeTupleList(strList):
    '''
    Convert string of the full proposition to a tuple of literals\n
    E.g.:
    \t"A OR -B OR C" => ('A', '-B', 'C')
    '''
    res = []
    for i in strList:
        if isPosLiteral(i) or isNegLiteral(i):
            res.append((i,))
            continue
        tuple_i = tuple(i.split(' OR '))
        res.append(sortProposition(tuple_i))
    return res

def read_input(path):
    '''
    Read the input file and store the query alpha and knowledge base KB

    Parameters:
        path: directory to the input file
    '''
    file = open(path, 'r')
    
    if file.mode == 'r':
        alpha = makeTupleList([file.readline().replace('\n','')])
        KB_len = int(file.readline())
        KB_sentences =  []
        for i in range(KB_len):
            KB_sentences.append(file.readline().replace('\n', ''))
        
        KB_sentences = makeTupleList(KB_sentences)
    
    file.close()    
    return alpha, KB_sentences

def write_output(path, buffer):
    '''
    Print the resolution result to output file
    '''
    file = open(path, 'w')
    file.write(buffer)
    file.close()

def main(args):
    '''
    Driver function
    '''
    alpha, KB_sentences = read_input(args.input)

    agent = KB(sentences = KB_sentences)

    res = agent.PL_Resolution(alpha)

    print(agent.result)

    write_output(args.output, agent.result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Propositional Logic Resolution")
    parser.add_argument("input", type=None, help="The input file")
    parser.add_argument("output", type=None, help="The output file")
    args = parser.parse_args()

    main(args)