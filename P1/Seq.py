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
        seq=list(seq)
        for index, base in enumerate(seq):
            if base == 'A':
                seq[index]='T'
            if base == 'T':
                seq[index]='A'
            if base == 'C':
                seq[index]='G'
            if base == 'G':
                seq[index]='C'

        seq=''.join(seq)
        return Seq(seq)


    def reverse(self):
        seq = self.strbases.upper()[::-1]
        return Seq(seq)

    def count(self, base):
        base=base.upper()
        return self.strbases.upper().count(base)

    def perc(self, base):
        seq = self.strbases.upper()
        base=base.upper()
        count= seq.count(base)
        length = len(seq)
        return round(100.0 * count/length, 1)

s= 'ACGTTGGGCCA'
print(Seq(s).complement())