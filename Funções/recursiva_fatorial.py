def fatorial(n):
    if n == 0: #Se n estiver em 0
        return 1 #A função para e retorna ela mesmo 
    return n * fatorial (n - 1) #Exemplo 3: Retorna 3*2 ... 

print(fatorial(3)) 