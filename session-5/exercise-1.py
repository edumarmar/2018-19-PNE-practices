def count_nuc(seq):
    """Counting the number of As in the string"""

    a = 0
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


def percentages(seq)
    # Calculate the total length
    tl = len(s)
    a, c, t, g = count(seq)['A'], count(seq)['C'], count(seq)['T'], count(seq)['G']
    variables = [a, c, t, g]
    astats, cstats, tstats, gstats = 0, 0, 0, 0
    stats = [astats, cstats, tstats, gstats]
    for i, elem in zip(variables, len(variables)):
        stats[elem] = round(100.0 * i / tl, 1)
    return stats

    print("This sequence is {} bases in length".format(tl))

    if tl == 0:
        print("The percentages of As is: ", 0)
    else:
        print("The percentages of As is {}%".format(round(100.0 * na / tl, 1)))
# Main program

s= input('Enter the sequence: ')
s=s.upper()
na = count_a(s)
print("The are {} As in the sequence".format(na))

