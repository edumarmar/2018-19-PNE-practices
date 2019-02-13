def count_bases(seq):
    """Counting the number of As in the string"""

    a=0
    c=0
    g=0
    t=0

    for i in seq:
        if i == 'A':
            a+= 1
        if i == 'C':
            c+= 1
        if i == 'T':
            t += 1
        if i == 'G':
            g += 1

    count= {'A': a,
                  'C': c,
                  'T': t,
                  'G': g}

    return count


def percentages(seq):
    # Calculate the total length
    tl = len(seq)
    a, c, g, t = seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')
    variables = [a, c, g, t]
    astats, cstats, gstats, tstats = 0, 0, 0, 0
    stats = [astats, cstats, gstats, tstats]
    for i, elem in zip(variables, range(4)):
        stats[elem] = round(100.0 * i / tl, 1)
    return stats

# Main program
def main(list):
    for seq in list:
        count= count_bases(seq)
        stats= percentages(seq)
        print('Base A')
        print('Counter: ', count['A'])
        print('Percentage: ', stats[0])

        print('Base C')
        print('Counter: ', count['C'])
        print('Percentage: ', stats[1])

        print('Base G')
        print('Counter: ', count['G'])
        print('Percentage: ', stats[2])

        print('Base T')
        print('Counter: ', count['T'])
        print('Percentage: ', stats[3])


s1= input('Enter the first sequence: ')
s2= input('Enter the second sequence: ')
seqs=(s1, s2)
main(seqs)

