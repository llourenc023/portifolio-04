# identificacao.py (CORRIGIDO)
from identificacao_funcoes import *

# A variável 'dados' é inicializada uma vez, fora do loop. Perfeito!
dados = {}

# Usamos um loop infinito que só é quebrado pela opção de sair.
while True: 
    
    escolha = menu() # <--- CHAMADO DENTRO DO LOOP, A CADA RODADA

    if escolha == 1:
        # Passamos 'dados' para a função poder modificá-la
        criar(dados)
    elif escolha == 2:
        salvar(dados)
    elif escolha == 3:
        exibir(dados)
    elif escolha == 4:
        # A condição de saída agora quebra o loop
        print("Saindo do programa...")
        break
    else:
        # Mensagem para qualquer outra entrada que não seja 1, 2, 3 ou 4
        print("Opção inválida. Por favor, tente novamente.")