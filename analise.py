from analise_funcao import *
bib = {}
while True:
        escolher = menu()
        if escolher == 1:
                esc1(bib)
                print('Ameaça anotada!')
        elif escolher == 2:
                esc2(bib)
                print('Salvo com sucesso no arquivo')
        elif escolher == 3:
                esc3(bib)
        elif escolher == 4:
                print('Saindo...')
                break
        else:
            print(f'Opção {escolher} inválida! \nTente novamente')