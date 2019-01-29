


def lendna():
    with open('dna.csv', 'r') as f:
        for row in f:
            sequence = row

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

        f.close()

    return



lendna()