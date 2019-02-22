# Class that contains different functions such as finding
# the length of a seq, the complement, reverse, number of
# the different bases or the appearence of itself in percentages.

# The class is also placed in this folder so it is easier to import
#it to the client file.

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # this method is called every time a new object is created

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


    def complement(self):
        seq = self.strbases
        seq = seq.upper()
        for index, elem in enumerate(seq):
            if elem == 'A':
                seq = seq[:index] + seq[index:].replace('A', 'T')
            if elem == 'T':
                seq = seq[:index] + seq[index:].replace('T', 'A')
            if elem == 'C':
                seq = seq[:index] + seq[index:].replace('C', 'G')
            if elem == 'G':
                seq = seq[:index] + seq[index:].replace('G', 'C')
        return seq


    def reverse(self):
        seq = self.strbases.upper()[::-1]
        return seq

    def count(self, base):
        base=base.upper()
        return self.strbases.upper().count(base)

    def perc(self, base):
        seq = self.strbases.upper()
        base=base.upper()
        counter= seq.count(base)
        tl = len(seq)
        return round(100.0 * counter/tl, 1)






def operations(seq, operation):
    i = Seq(seq)
    operations = {'len': i.len(),
                  'complement': i.complement(),
                  'reverse': i.reverse(),
                  'countA': i.count('a'),
                  'countT': i.count('t'),
                  'countG': i.count('g'),
                  'countC': i.count('c'),
                  'percA': i.perc('a'),
                  'percC': i.perc('c'),
                  'percT': i.perc('t'),
                  'percG': i.perc('g')}

    return operations[operation]



seq= 'ACGT'
operation='countA'

i=operations(seq, operation)
print(i)