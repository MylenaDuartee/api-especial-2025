# Início: 24/05, às 14:39
# Termino: 24/05, às 15:13

def main():
    n = receber_n()
    if n == 0:
        print('nenhuma sequência foi digitada!')
    num_sequencia = 0

        
    

    while n > 0:
        soma = 0
        soma_pares = 0
        qtd_numeros = 0
        maior_num = None
        menor_num = None
        while True:
            numeros = int(input('digite um número: '))
            if numeros == 0:
                break
            
            if maior_num is None or numeros > maior_num:
                maior_num = numeros
            if menor_num is None or numeros < menor_num:
                menor_num = numeros
            soma += numeros
            qtd_numeros += 1
            media = soma/qtd_numeros
            if numeros % 2 == 0:
                soma_pares += numeros
        num_sequencia +=1

        
        saida = f'''\n
    ---> Sequência {num_sequencia} <---
    Soma dos números pares: {soma_pares}
    Média da sequência: {media:.2f}
    Maior número: {maior_num}
    Menor número: {menor_num}
    \n'''    
            
        print(saida)
        
        n -= 1


def receber_n():
    entrada = input('digite o número de sequências que vc irá digitar: ')
    try: 
        numero = int(entrada)
        return numero
    except:
        print('número inválido, digite novamente!')
        return(entrada)

    

main()