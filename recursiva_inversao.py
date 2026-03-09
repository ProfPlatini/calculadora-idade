# # Faça uma função recursiva que inverta um número.

# # Exemplo:

# # entrada: 1234
# # saida: 4321

# inverter(1234) = "4" + inverter(123)
# inverter(123)  = "3" + inverter(12)
# inverter(12)   = "2" + inverter(1)
# inverter(1)    = "1" + inverter(0)
# inverter(0)    = ""  # caso base


def inverter(n):
    if n == 0:
        return ""
    return str (n%10) + inverter(n//10)

print(inverter(1234))