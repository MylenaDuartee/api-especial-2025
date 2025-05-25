# Início: 24/05, às 23:17
# Termino: 24/05, às 23:36

def main():
    num = int(input('digite o numero: '))
    total_alunos = 0
    backend = 0
    frontend = 0
    mobile = 0
    dados = 0
    while num != 0:
        entrada = input('digite a quantidade e a habilidade: ')
        quantidade = int(entrada.split()[0]) 
        tipo = entrada.split()[1] 
        total_alunos += quantidade
        num -= 1

        if tipo == 'B' or tipo == 'b':
            backend += quantidade
        elif tipo == 'F' or tipo == 'f':
            frontend += quantidade
        elif tipo == 'M' or tipo == 'm':
            mobile += quantidade
        elif tipo == "D" or tipo == 'd':
            dados += quantidade


    porcentagem_back = (backend * 100) / total_alunos
    porcentagem_front = (frontend * 100) / total_alunos
    porcentagem_mobi = (mobile * 100) / total_alunos
    porcentagem_dados = (dados * 100) / total_alunos
    
    saida = f'''
    Total: {total_alunos} alunos 
    Total de Backend: {backend} 
    Total de Frontend: {frontend} 
    Total de Mobile: {mobile} 
    Total de Dados: {dados} 
    Percentual de Backend: {porcentagem_back:.2f}% 
    Percentual de Frontend: {porcentagem_front:.2f}% 
    Percentual de Mobile: {porcentagem_mobi:.2f}% 
    Percentual de Dados: {porcentagem_dados:.2f}% 
    '''
    print(saida)

main()