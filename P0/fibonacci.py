n = int(input('inster the n parameter: '))

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

print(fibonacci(n))
