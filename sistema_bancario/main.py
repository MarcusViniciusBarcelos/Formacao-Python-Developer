from movimentacao import Movimentacao

def exibir_menu():
    print('\n1 - Depositar')
    print('2 - Sacar')
    print('3 - Visualizar Extrato')
    print('4 - Sair')

def main():
    movimentacao = Movimentacao()

    while True:
        exibir_menu()
        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            movimentacao.realizar_deposito()
        elif opcao == 2:
            movimentacao.realizar_saque()
        elif opcao == 3:
            movimentacao.visualizar_extrato()
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()