def contador(palavra):
    return len(palavra)

def main():
    entrada = str(input("Digite a palavra:"))
    caracteres = (contador(entrada))
    print(f"\nA quantidade de letras da sua palavra é {caracteres} caracteres!")
if __name__ == '__main__':
    main()

    

