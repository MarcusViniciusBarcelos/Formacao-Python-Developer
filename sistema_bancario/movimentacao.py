from banco import Banco

class Movimentacao:
    def __init__(self):
        self.banco = Banco()

    def realizar_deposito(self):
        valor = float(input('Digite o valor a depositar: '))
        self.banco.depositar(valor)

    def realizar_saque(self):
        valor = float(input('Digite o valor a sacar: '))
        self.banco.sacar(valor)

    def visualizar_extrato(self):
        self.banco.extrato()