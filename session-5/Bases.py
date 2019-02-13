def count_bases(seq):
    """Counting the number of As in the string """

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

