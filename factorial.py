def factorial(n):
    resultado = 1

    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

n = 20
pas = factorial(n)