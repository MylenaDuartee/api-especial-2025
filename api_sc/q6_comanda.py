# Início: 24/05, às 18:41
# Término: 24/05, às 19:26

def main():
    valor_agua = 0
    valor_cerveja = 0
    valor_tira_gosto = 0
    qtd_cervejas = 0

    while True:
        menu_entrada()
        entrada = input('>>> digite o produto: ')
        quantidade = int(entrada.split()[0]) 
        produto = entrada.split()[1]


        if produto == 'C' or produto == 'c':
            qtd_cervejas += quantidade
            valor_cerveja += quantidade * 9
        if produto == 'T' or produto == 't':
            valor_tira_gosto += quantidade * 39
        if produto == 'A' or produto == 'a':
            valor_agua += quantidade * 5

        valor_conta = valor_cerveja + valor_tira_gosto + valor_agua
        
        if qtd_cervejas > 10 or valor_conta > 200:
            taxa_servico = 0
            conta = valor_conta
        else:
            taxa_servico = valor_conta * 0.10
            conta = valor_conta + taxa_servico


        qtd_pagadores = int(input('digite a quantidade de pessoas que irão pagar: '))
        divisao = conta / qtd_pagadores
        
        mostrar_conta(valor_conta,qtd_pagadores,divisao,taxa_servico,conta)
        confirmar = input('>>> digite (0) para confirmar pagamento ou enter para pedir mais algo: ')
        if confirmar == '0':
            print('pagamento concluído!')
            break





    
def mostrar_conta(valor_conta,qtd_pagadores,divisao,taxa_servico,conta):
    saida = f'''
                > Valor da conta: R${valor_conta:.2f}
                > Valor dividido para "{qtd_pagadores}" pessoas: R${divisao:.2f}
                > Valor da taxa de serviço: R${taxa_servico:.2f}
                > Valor com taxa de serviço: R${conta:.2f}
                 '''
    print(saida)


def menu_entrada():
    menu = f'''
    C- Cerveja: R$ 9.00
    T- Tira-Gosto: R$ 39.00
    A- Água: R$ 5.00
    '''
    print(menu)

main()