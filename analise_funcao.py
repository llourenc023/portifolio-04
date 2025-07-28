def menu():
    print('1 - Para inserir o nome da ameaça, probabilidade, consequência e medida de risco')
    print('2 - Para salvar em arquivo')
    print('3 - Para visualizar')
    print('4 - Para sair')
    choose = int(input("Digite a opção desejada: "))
    return choose

def esc1(tabela):
    parar = "S"
    while parar == "S":
     tabela[input("Digite o ID da ameaça: ")] = [input("Digite a probabilidade: "),
                                                       input("Digite a consequência: "),
                                                       input("Digite a medida de risco: ")]
     parar = input("Deseja fazer outra ameaça? <S/N>: ").upper()
     if parar == "N":
         print("Parando....")
         break
def esc2(tabela):
    with open('Análise.csv', 'a') as arquivo:
        for chave, dado in tabela.items():
            arquivo.write(chave + ',' + dado[0] + ',' + dado[1] + ',' + dado[2] + '\n')

def esc3(tabela):
    with open('Análise.csv', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha)