from Bases import count_bases

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

