# Crie uma função recursiva que some todos os números de 1 até n.

def soma (n):
    if n == 0:
        return 0
    return n + soma(n - 1)
    
print(soma(5))

#4+3+2+1+0 = 10
#Primeira etapa: Soma n(4) mais (4-1) 3. Ele continua executando.