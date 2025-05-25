# Início: 25/05, às 00:28
# Termino: 25/05, às 01:13

def main():
   
    print('---> primeira data <---')
    d1 = receber_dia('dia(s): ')
    m1 = receber_mes('mês(ses): ')
    a1 = receber_ano('ano: ')

    print('---> segunda data <---')
    d2 = receber_dia('dia(s): ')
    m2 = receber_mes('mês(ses): ')
    a2 = receber_ano('ano: ')

    if d1 != 0 and d1 < d2:
        m1 -= 1
        d1 += 30
    if m1 != 0 and m1 < m2:
        a1 -= 1
        m1 += 12
    
    diferenca_dia = d1 - d2
    diferenca_mes = m1 - m2
    diferenca_ano = a1 - a2

    if d1 == 0 and d2 == 0 and diferenca_dia == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_mes} mes(ses)
            {diferenca_ano} anos
            '''
    elif d1 == 0 and d2 == 0 and diferenca_dia == 0 and m1 == 0 and m2 == 0 and diferenca_mes == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_ano} anos
            '''
    elif d1 == 0 and d2 == 0 and diferenca_dia == 0 and a1 == 0 and a2 == 0 and diferenca_ano == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_mes} mes(ses)
            '''
    elif m1 == 0 and m2 == 0 and diferenca_mes == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_dia} dia(s)
            {diferenca_ano} anos
            '''
    elif m1 == 0 and m2 == 0 and diferenca_mes == 0 and a1 == 0 and a2 == 0 and diferenca_ano == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_dia} dia(s)
            '''
    elif a1 == 0 and a2 == 0 and diferenca_ano == 0:
        saida = f''' 
            a diferença das datas é: 
            {diferenca_dia} dia
            {diferenca_mes} mes(ses)
            '''
    else: 
        saida = f''' 
            a diferença das datas é: 
            {diferenca_dia} dias
            {diferenca_mes} mes(ses)
            {diferenca_ano} anos
            '''
        
    print(saida)

    
    

def receber_int(label:str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except:
        print('entrada inválida, digite novamente!')
        return receber_int(label)
    

def receber_dia(label):
    entrada = receber_int(label)
    if entrada == 0 or entrada <= 30:
        return entrada
    else:
        print('dia(s) inválido, digite novamente!')
        return receber_dia(label)
    

def receber_mes(label):
    entrada = receber_int(label)
    if entrada == 0 or entrada <= 12:
        return entrada
    else:
        print('mês(ses) inválido, digite novamente!')
        return receber_mes(label)
    

def receber_ano(label):
    entrada = receber_int(label)
    if entrada == 0 or entrada <= 3000:
        return entrada
    else:
        print('ano(s) inválido, digite novamente!')
        return receber_ano(label)

main()
