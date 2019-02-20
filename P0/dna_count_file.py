# program for counting the bases of sequences located on another file

def dna_count_file():

    # opening text file and convert all sequences into one

    with open('dna.csv', 'r') as f:
        sequence=[]
        for row in f:
            sequence.append(row)

        sequence=''.join(sequence)
        sequence=sequence.lower()
        sequence.replace('\n', '')

    # counting the bases
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

        f.close()
    return

dna_count_file()
