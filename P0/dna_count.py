# Program to count the bases of a DNA sequence

seq = input('Insert a DNA sequence: ')


def dna_count(seq):
    seq = seq.lower()
    num = len(seq)

    a = seq.count('a')
    c = seq.count('c')
    t = seq.count('t')
    g = seq.count('g')

    print('Total length: ', num)
    print('A:', a)
    print('C:', c)
    print('T:', t)
    print('G:', g)

    return


dna_count(seq)
