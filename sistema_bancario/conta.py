class ContaBancaria:
    num_conta = 1

    def __init__(self, usuario, senha):
        self.agencia = "0001"
        self.numero_conta = ContaBancaria.num_conta
        ContaBancaria.num_conta += 1
        self.usuario = usuario
        self.senha = senha
        self.saldo = 0
        self.depositos = []
        self.saques = 0
    
    def __str__(self):
        return f"Conta Número: {self.numero_conta}\nUsuário vinculado: {self.usuario.nome}"


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if self.saques < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques += 1
            self.depositos.append(-valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saques >= 3:
            print('Limite máximo de saques diários atingido.')
        elif valor > 500:
            print('Valor máximo por saque é R$ 500,00.')
        else:
            print('Saldo insuficiente para o saque.')

    def extrato(self):
        print('Extrato:')
        for movimento in self.depositos:
            if movimento > 0:
                print(f'Depósito de R$ {movimento:.2f}')
            else:
                print(f'Saque de R$ {-movimento:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')

def login(contas):
    num_conta = int(input('Digite o número da conta: '))
    senha = input('Digite a senha: ')

    for conta in contas:
        if conta.numero_conta == num_conta and conta.senha == senha:
            return conta

    return None