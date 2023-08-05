from abc import ABC, abstractmethod

class ContaBancaria(ABC):
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

    @abstractmethod
    def deposita(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def extrato(self):
        print('Extrato:')
        for movimento in self.depositos:
            if movimento > 0:
                print(f'Depósito de R$ {movimento:.2f}')
            else:
                print(f'Saque de R$ {-movimento:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')

class ContaBancariaSimples(ContaBancaria):
    def deposita(self, valor):
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
