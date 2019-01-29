sequence= input('Insert a DNA sequence: ')

def dna_count(sequence):

    sequence= sequence.lower()
    num=len(sequence)

    a=sequence.count('a')
    c=sequence.count('c')
    t=sequence.count('t')
    g=sequence.count('g')

    print('Total length: ', num)
    print('A:', a)
    print('C:', c)
    print('T:', t)
    print('G:', g)

    return

dna_count(sequence)