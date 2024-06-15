def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2) + fibonacci(n-3)
    
x = int(input('Número: '))
print('Fibonacci: ', fibonacci(x))