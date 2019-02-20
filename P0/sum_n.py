# Program that sums all the numbers from 1
# to the n parameter introduced by the user

n= int(input('Insert the n parameter '))

count=0

for i in range(n+1):
    count+=i

print('the result is: ', count)