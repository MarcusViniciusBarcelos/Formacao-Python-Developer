from menu_admin import menu_admin

def login(contas):
    num_conta = int(input('Digite o número da conta: '))
    senha = input('Digite a senha: ')

    for conta in contas:
        if conta.numero_conta == num_conta and conta.senha == senha:
            return conta

    return None

def menu_conta(conta):
    while True:
        print('\n1 - Depositar')
        print('2 - Sacar')
        print('3 - Visualizar Extrato')
        print('4 - Voltar')

        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            valor = float(input('Digite o valor a depositar: '))
            conta.deposita(valor)

        elif opcao == 2:
            valor = float(input('Digite o valor a sacar: '))
            conta.sacar(valor)

        elif opcao == 3:
            conta.extrato()

        elif opcao == 4:
            break

        else:
            print('Opção inválida. Tente novamente.')

def main():
    contas = []
    usuarios = []

    while True:
        print('\n1 - Login')
        print('2 - Menu Administrador')
        print('3 - Sair')

        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            conta = login(contas)
            if conta:
                print('Login realizado com sucesso.')
                menu_conta(conta)
            else:
                print('Conta ou senha inválidos.')

        elif opcao == 2:
            menu_admin(contas, usuarios)

        elif opcao == 3:
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
