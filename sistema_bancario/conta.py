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

    def realizar_operacao(self, operacao):
        operacao.executar()
