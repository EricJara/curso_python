#Función de recursividad de núimero factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

facto = 5
print(factorial(facto))


#Función de recursibidad de número Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 4
print(fibonacci(number))


#Función de recursividad para la suma de número naturales
def sumNatural(n):
    if n == 0:
        return 0
    else:
        return n + sumNatural(n-1)

num = 6
print(sumNatural(num))