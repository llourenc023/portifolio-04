def menu():
    print("Bem-vindo à tabela de identificação")
    print('Digite: ')
    print('1 - Para criar a tabela')
    print('2 - Para salvar em arquivo')
    print('3 - Para exibir a tabela')
    print('4 - Para sair')
    escolher = int(input('Escolha uma opção: '))
    return escolher
def criar(tabela):
    continuar = 'S'
    while continuar == 'S':
        tabela[input('Digite o ID: ')] = [input('Digite a ameaça: '),
                                        input('Digite o controle existente:'),
                                        input('Digite a vulnerabilidade: '),
                                        input('Digite a consequência: ')]
        continuar = input('Deseja continuar? (S/N): ').upper()
        if continuar == 'N' or continuar == 'n':
            print('Tabela criada com sucesso!')
            break
def salvar(tabela):
    with open('Identificação.csv', 'a') as arquivo:
        for ids, itenss in tabela.items():
            arquivo.write(ids + ',' + itenss[0] + ',' + itenss[1] + ',' + itenss[2] + ',' + itenss[3] + '\n')
        return 'Dados salvos com sucesso!'
def exibir(tabela):
    idh = input('Digite o ID: ')
    with open('Identificação.csv', 'r') as arquivo:
        linha = arquivo.readlines()
        for linhas in linha:
            if idh in linhas:
                print(linhas)
        
       

        