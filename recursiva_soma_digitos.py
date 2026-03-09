# Crie uma função recursiva que conte quantos dígitos existem em um número.
def digito (n):
    if n <= 0:
        return 0
    return n % 10 + digito(n//10)



print(digito(1234))
    
    

     
# print(n // 10) Remove o último dígito (No caso, 4)
# print(n % 10) Pega o último dígito (No caso ficaria 123)
#Sequência: 4 + digito(123), 3 + digito (12) + 2 + digito(1) + 1 + digito(0)
