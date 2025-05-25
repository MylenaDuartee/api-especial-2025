# Início: 24/05, às 16:41
# Término: 24/05, às 17:32
def main():
    
    casos_inicial = receber_caso_valido()
    while casos_inicial == 'fim':
        print('por favor, inicie com um número!')
        casos_inicial = receber_caso_valido()

    n_casos = casos_inicial
    casos = 0

    while True:
        casos = receber_caso_valido()
        if casos == 'fim':
            break
        aumento = casos
        porcentagem = ((aumento - n_casos) / n_casos) * 100
        n_casos = aumento
        if porcentagem < 0:
            conceito = 'em queda'
        elif porcentagem <= 15:
            conceito = 'estável'
        else:
            conceito = 'em alta'
        print(conceito)



def receber_caso_valido():
    entrada = input('digite a quantidade de casos de covid: ')
    try:
        if entrada != 'fim':
            numero = int(entrada)
            return numero
        else:
            return entrada
    except:
        print('o número digitado é inválido, digite novamente!')
        return receber_caso_valido()



main()