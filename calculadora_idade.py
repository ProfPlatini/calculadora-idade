def calculadora_idade():
    ano_nasc = int(input("Digite o seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual:"))
    idade = ano_atual - ano_nasc
    print(f"\t\tA sua idade é:\n\t\t{idade} anos.")
    
def main():
    calculadora_idade()
    
if __name__ == '__main__':
    main()