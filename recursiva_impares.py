def soma_impar (n):
    if n <= 0:
        return 0 
    if n % 2 == 0:
        return soma_impar(n-1)
    if n % 2 != 0:
        return n + soma_impar(n-2)
    
print(soma_impar(10))


