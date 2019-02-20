# Program that opens a file text with a sequence
# and counts the bases in it

with open('CPLX2.txt', 'r') as f:
    a=0
    c=0
    t=0
    g=0
    for line in f:
        line=line.lower()
        if '>' in line:
            line=''
        a += line.count('a')
        c += line.count('c')
        t += line.count('t')
        g += line.count('g')
print('A: ', a, '\nC: ', c, '\nT: ', t,'\nG: ', g)