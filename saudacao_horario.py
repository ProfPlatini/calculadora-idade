from datetime import datetime
print(datetime.now())
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().day)

current_hour = datetime.now().hour

def greetings ():
    if current_hour < 12:
        print("Olá, Luiz. Bom dia!")
    elif current_hour < 18:
        print("Olá Luiz. Boa tarde!")
    else:
        print("Olá Luiz. Boa noite!")
        
def main():
    greetings()
    
if __name__ == '__main__':
    main()