# Program for summing the terms from 1 to n
# of the fibonacci series

n = int(input('inster the n parameter: '))

# function for generating the n numbers of the fibonacci series
def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    fibonacci=[]

    while count < n:
        fibonacci.append(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return fibonacci

# function that sums the terms fo the list generated previously
def fibonacci_sum(list):
    sum_fibo=0
    for i in list:
        sum_fibo+=i
    return sum_fibo

sum=fibonacci_sum(fibonacci(n))
print(sum)