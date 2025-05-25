# Início: 25/05, às 01:35
# Término: 25/05, às 02:02

def main():
    premio = receber_int('digite o valor do premi da mega_sena: ')
    valor_bilhete = 0
    maior_premio_individual = None
    menor_premio_individual = None

    imposto = (premio * 20) / 100
    premio_sem_imposto = premio - imposto
    while True:
        colaboracao = receber_float('digite o valor da colaboração: ')
        valor_bilhete += colaboracao
        if colaboracao == 0:
            break
        premio_individual = (premio_sem_imposto * colaboracao) / valor_bilhete
        
        if maior_premio_individual is None or premio_individual > maior_premio_individual:
            maior_premio_individual = premio_individual
        if menor_premio_individual is None or premio_individual < menor_premio_individual:
            menor_premio_individual = premio_individual
    print(menor_premio_individual, maior_premio_individual)


def receber_int(label:str):
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero < 0:
            print('valor inválido, tente novamente')
            return receber_int(label)
        else:
            return numero
        
    except:
        print('entrada inválida, digite novamente!')
        return receber_int(label)
    

def receber_float(label:str):
    entrada = input(label)
    try:
        numero = float(entrada)
        if numero < 0:
            print('valor inválido, tente novamente')
            return receber_float(label)
        else:
            return numero
    except:
        print('entrada inválida, digite novamente!')
        return receber_float(label)
    

main()