# Sistema Bancário Atualizado em Python

Este projeto consiste em um sistema bancário em Python que permite realizar operações bancárias básicas, como depósito, saque e visualização de extrato. O objetivo é simular as operações de um banco virtual, armazenando os dados em memória e fornecendo uma interface de texto para interação com o usuário.

O projeto foi organizado em diferentes arquivos com suas respectivas responsabilidades:

## Arquivo "conta.py":

Neste arquivo, está implementada a classe `ContaBancaria`, que representa a conta bancária do cliente. A classe possui os seguintes atributos:

### Atributos:

- `agencia`: Representa o número da agência bancária (fixo como "0001").
- `numero_conta`: Número único da conta bancária, gerado automaticamente.
- `usuario`: Referência ao objeto da classe `Usuario` associado à conta.
- `senha`: Senha da conta bancária.
- `saldo`: Saldo disponível na conta.
- `depositos`: Lista que armazena todos os depósitos e saques realizados, para posterior exibição do extrato.
- `saques`: Contador para controlar o número de saques realizados em um dia.

### Métodos:

- `__str__`: Método especial que retorna uma representação da conta no formato de string.
- `depositar(valor)`: Permite realizar um depósito na conta, incrementando o saldo e registrando o depósito na lista de movimentos.
- `sacar(valor)`: Permite realizar um saque na conta, decrementando o saldo e registrando o saque na lista de movimentos, respeitando as regras de limite diário e saldo disponível.
- `extrato()`: Exibe o extrato completo com todos os depósitos, saques e o saldo atual da conta.

## Arquivo "usuario.py":

Neste arquivo, está implementada a classe `Usuario`, que representa os dados do titular da conta bancária. A classe possui os seguintes atributos:

### Atributos:

- `nome`: Nome completo do usuário.
- `data_nascimento`: Data de nascimento do usuário.
- `cpf`: Cadastro de Pessoa Física do usuário.
- `endereco`: Endereço completo do usuário.

## Arquivo "main.py":

Neste arquivo, encontra-se a função `main`, responsável por executar o programa principal do sistema bancário. A função cria listas para armazenar as contas e usuários cadastrados, exibindo um menu para o usuário escolher a operação desejada. As principais funcionalidades do programa são:

### Funcionalidades:

- Login: Permite ao usuário fazer login em sua conta bancária, solicitando o número da conta e a senha correspondente.
- Menu Administrador: Oferece opções para listar contas e usuários, editar contas, excluir contas, cadastrar usuários e cadastrar novas contas.
- Menu Conta: Após o login bem-sucedido, permite ao usuário realizar operações bancárias, como depósito, saque e visualização do extrato.

O sistema bancário é projetado para ser simples e intuitivo, permitindo que o usuário interaja facilmente com as operações bancárias disponíveis. As validações são realizadas para garantir que as operações sejam feitas dentro dos limites definidos.

**Observação:** As operações bancárias e cadastros são armazenados em memória, e o sistema não possui persistência de dados entre execuções.

Sinta-se à vontade para explorar o código, fazer melhorias e customizações conforme suas necessidades!
