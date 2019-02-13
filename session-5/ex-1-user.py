def count_a(seq):
    """Counting the number of As in the string"""

    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    return result


# Main program

s= input('Enter the sequence: ')
s=s.upper()
na = count_a(s)
print("The are {} As in the sequence".format(na))

# Calculate the total length
tl = len(s)

print("This sequence is {} bases in length".format(tl))

if tl==0:
    print("The percentages of As is: ", 0)
else:
    print("The percentages of As is {}%".format(round(100.0 * na/tl, 1)))