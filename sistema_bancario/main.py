from usuario import Usuario
from conta import ContaBancariaSimples
from menu_admin import MenuAdmin

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
    menu_admin = MenuAdmin()
    menu_admin.executar()

if __name__ == "__main__":
    main()
