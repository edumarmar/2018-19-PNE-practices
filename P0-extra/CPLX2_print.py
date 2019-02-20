# Program that prints the text from a text file

with open('CPLX2.txt', 'r') as f:
    for line in f:
        print(line)
f.close()