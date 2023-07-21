class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = 0

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