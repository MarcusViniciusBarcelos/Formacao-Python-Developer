from usuario import cadastrar_usuario
from menu_admin import menu_admin
from conta import cadastrar_conta
from conta import login



def main():
    contas = []
    usuarios = []

    while True:
        print('\n1 - Cadastrar Usuário')
        print('2 - Cadastrar Conta Bancária')
        print('3 - Login')
        print('4 - Menu Administrador')
        print('5 - Sair')

        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
            print('Usuário cadastrado com sucesso.')
            print(usuario)

        elif opcao == 2:
            if not usuarios:
                print('Cadastre um usuário primeiro.')
                continue
            usuario = usuarios[-1]
            conta = cadastrar_conta(usuario)
            contas.append(conta)
            print('Conta cadastrada com sucesso.')
            print(conta)

        elif opcao == 3:
            conta = login(contas)
            if conta:
                print('Login realizado com sucesso.')
                menu_conta(conta)
            else:
                print('Conta ou senha inválidos.')

        elif opcao == 4:
            menu_admin(contas)

        elif opcao == 5:
            break

        else:
            print('Opção inválida. Tente novamente.')

def menu_conta(conta):
    while True:
        print('\n1 - Depositar')
        print('2 - Sacar')
        print('3 - Visualizar Extrato')
        print('4 - Voltar')

        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            valor = float(input('Digite o valor a depositar: '))
            conta.depositar(valor)

        elif opcao == 2:
            valor = float(input('Digite o valor a sacar: '))
            conta.sacar(valor)

        elif opcao == 3:
            conta.extrato()

        elif opcao == 4:
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()