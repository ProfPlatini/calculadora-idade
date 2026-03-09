from datetime import date
from dateutil.relativedelta import relativedelta  # precisa instalar a biblioteca: pip install python-dateutil

def calculadora():
    # Entrada de dados do usuário
    ano_nasc = int(input("Digite o seu ano de nascimento: "))
    mes_nasc = int(input("Digite o mês do seu nascimento: "))
    dia_nasc = int(input("Digite o dia do seu nascimento: "))

    # Data de nascimento e data atual
    nascimento = date(ano_nasc, mes_nasc, dia_nasc)
    hoje = date.today()

    # Calcula a diferença usando relativedelta
    diferenca = relativedelta(hoje, nascimento)

    years = diferenca.years
    months = diferenca.months
    days = diferenca.days

    print(f"\nVocê possui {years} anos, {months} meses e {days} dias.")

def main():
    calculadora()

if __name__ == "__main__":
    main()