# Início: 24/05, às 17:52
# Término: 24/05, às 18:11

def main():
    n = int(input('Digite o limite inferior: '))
    m = int(input('Digite o limite superior: '))

    numero = n + 1  

    while numero < m:
        divisor = 2
        eh_primo = True  

        while divisor < numero:
            if numero % divisor == 0:
                eh_primo = False  
                break 
            divisor += 1

        if eh_primo and numero >= 2:
            print(f'{numero} é primo')
        else:
            print(f'{numero} não é primo')

        numero += 1  

main()
