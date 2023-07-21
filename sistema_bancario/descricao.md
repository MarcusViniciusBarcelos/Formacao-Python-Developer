# Sistema Bancario

Este projeto consiste na criação de um sistema bancário simples em Python que permite a realização de operações bancárias básicas, como depósito, saque e visualização de extrato. O objetivo é simular as operações de um banco virtual, armazenando os dados em memória e fornecendo uma interface de texto para interação com o usuário.

O sistema bancário é dividido em três arquivos: banco.py, main.py e movimentacao.py, cada um com sua responsabilidade específica.

## banco.py: 
Neste arquivo, está implementada a classe Banco, que representa a conta bancária do cliente. A classe possui os seguintes atributos:

### saldo: 
Representa o saldo disponível na conta.
### depositos: 
Uma lista que armazena todos os depósitos e saques realizados, para posterior exibição do extrato.
### saques: 
Contador para controlar o número de saques realizados em um dia.
Além disso, a classe possui os métodos depositar, sacar e extrato, que permitem a realização das operações de depósito, saque e visualização do extrato, respectivamente. A classe também faz as devidas validações, como verificar se o valor do depósito é positivo e se o limite máximo de saques diários foi atingido.

## movimentacao.py: 
Este arquivo contém a classe Movimentacao, que serve como uma interface entre o usuário e as operações bancárias disponíveis. A classe possui um objeto da classe Banco e possui três métodos:

### realizar_deposito: 
Permite ao usuário realizar um depósito, solicitando o valor a ser depositado.
### realizar_saque:
Permite ao usuário realizar um saque, solicitando o valor a ser sacado.
### visualizar_extrato: 
Exibe o extrato com todos os depósitos, saques e o saldo atual da conta.
## main.py: 
Neste arquivo, está a função main, responsável por executar o programa. Ela cria um objeto da classe Movimentacao e, através de um loop, exibe um menu para o usuário escolher a operação desejada. O usuário pode depositar, sacar, visualizar o extrato ou sair do programa.

O sistema bancário é projetado para ser simples e intuitivo, permitindo que o usuário interaja facilmente com as operações bancárias disponíveis. Os depósitos e saques são armazenados em uma lista para que o extrato possa ser exibido ao final da sessão. Além disso, o sistema realiza validações para garantir que as operações sejam feitas dentro dos limites definidos.

Este projeto é uma demonstração básica de como um sistema bancário pode ser implementado em Python e pode ser usado como ponto de partida para o desenvolvimento de sistemas mais complexos e completos.
