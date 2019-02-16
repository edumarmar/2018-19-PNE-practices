from Seq import Seq

seq1= Seq('AGTACACTGGT')
seq2= Seq('CGTAAC')
seq3= seq1.complement()
seq4= seq2.reverse()
seqs= [seq1, seq2, seq3, seq4]

for index in range(len(seqs)):
    print('\n')
    print('Sequence {}: {}'.format(index+1, seqs[index].strbases))
    print('Length: {}'.format(seqs[index].len()))
    print('Bases count: A:{}, T:{}, C:{}¨, G:{}'.format(seqs[index].count('A'),seqs[index].count('T'),seqs[index].count('C'),seqs[index].count('G')))
    print('Bases percentage: A:{}%, T:{}%, C:{}%¨, G:{}%'.format(seqs[index].perc('A'),seqs[index].perc('T'),seqs[index].perc('C'),seqs[index].perc('G')))