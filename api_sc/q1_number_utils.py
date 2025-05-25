# Início: 25/05, às 13:06
# Termino: 25/05, às 13:20

def receber_num_int(label:str):
    while True:
        entrada = input(label)
        try:
            num = int(entrada)
            return num
        except:
            print('numero inválido, digite novamente!')


def num_int_positivo(label):
    while True:
        entrada = receber_num_int(label)
        if entrada > 0:
            return entrada
        else:
            print('Número inválido, por favor, digite um número positivo!')



def num_int_negativo(label):
    while True:
        entrada = receber_num_int(label)
        if entrada < 0:
            return entrada
        else:
            print('Número inválido, por favor, digite um número negativo!')


def num_int_min_x(label,min=6):
    while True:
        entrada = receber_num_int(label)
        if entrada >= min:
            return entrada
        else:
            print(f'Número inválido, por favor, digite um número maior ou igual a: "{min}"')



def num_int_max_x(label,max=6):
    while True:
        entrada = receber_num_int(label)
        if entrada <= max:
            return entrada
        else:
            print(f'Número inválido, por favor, digite um número menor ou igual a: "{max}"')


def num_int_na_faixa(label,max=4,min=1):
    while True:
        entrada = receber_num_int(label)
        if entrada >= min and entrada <= max:
            return entrada
        else:
            print(f'Número inválido, por favor, digite um número na faixa de {min} a {max}')






