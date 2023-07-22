from usuario import Usuario
from conta import ContaBancaria

def exibir_menu_admin():
    print('\nMenu Administrador')
    print('1 - Listar Contas')
    print('2 - Listar Usuários')
    print('3 - Editar Contas')
    print('4 - Excluir Contas')
    print('5 - Cadastrar Usuário')
    print('6 - Cadastrar Conta')
    print('7 - Editar Usuário')
    print('8 - Voltar')
    
def cadastrar_usuario():
    nome = input('Nome: ')
    data_nascimento = input('Data de Nascimento: ')
    cpf = input('CPF: ')
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade_uf = input("Digite a cidade/UF: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade_uf}"
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    detalhes_usuario = f"\nNome: {usuario.nome}\nData de Nascimento: {usuario.data_nascimento}\nCPF: {usuario.cpf}\nEndereço: {usuario.endereco}\n"
    print ("\n===usuario cadastrado com sucesso ===\n")
    print(detalhes_usuario)
    return usuario

def cadastrar_conta(usuarios):
    if not usuarios:
        print('Cadastre um usuário primeiro.')
        return None

    print('Usuários disponíveis:')
    for i, usuario in enumerate(usuarios, 1):
        print(f'{i} - {usuario.nome}')

    opcao = int(input('Digite o número do usuário para cadastrar a conta: '))
    if opcao < 1 or opcao > len(usuarios):
        print('Opção inválida.')
        return None

    usuario = usuarios[opcao - 1]
    senha = input('Digite a senha da conta: ')
    conta = ContaBancaria(usuario, senha)
    print(f'Conta cadastrada com sucesso para o cliente {usuario.nome}.')
    print(f'Número da conta: {conta.numero_conta}')
    return conta

def menu_admin(contas, usuarios):
    while True:
        exibir_menu_admin()
        opcao = int(input('Digite o número da operação desejada: '))

        if opcao == 1:
            listar_contas(contas)
        elif opcao == 2:
            listar_usuarios(usuarios)
        elif opcao == 3:
            editar_contas(contas)
        elif opcao == 4:
            excluir_conta(contas)
        elif opcao == 5:
            usuario = cadastrar_usuario()
            if usuario:
                usuarios.append(usuario)
        elif opcao == 6:
            conta = cadastrar_conta(usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 7:
            usuario = menu_editar_usuario(usuarios)
            if usuario:
                editar_usuario(usuario)
        elif opcao == 8:
            break
        else:
            print('Opção inválida. Tente novamente.')

def listar_usuarios(usuarios):
    print('\nLista de Usuários:')
    for usuario in usuarios:
        print(f'Nome: {usuario.nome} | CPF: {usuario.cpf} | Endereço: {usuario.endereco}')

def listar_contas(contas):
    print('\nContas Bancárias:')
    for conta in contas:
        print(f'Agência: {conta.agencia} | Conta: {conta.numero_conta} | Cliente: {conta.usuario.nome}')

def editar_contas(contas):
    num_conta = int(input('Digite o número da conta que deseja editar: '))
    for conta in contas:
        if conta.numero_conta == num_conta:
            print('Conta encontrada. Edite os dados:')
            nova_senha = input('Nova senha: ')
            conta.senha = nova_senha
            print('Senha atualizada com sucesso.')
            break
    else:
        print('Conta não encontrada.')

def excluir_conta(contas):
    num_conta = int(input('Digite o número da conta que deseja excluir: '))
    for i, conta in enumerate(contas):
        if conta.numero_conta == num_conta:
            del contas[i]
            print('Conta excluída com sucesso.')
            break
    else:
        print('Conta não encontrada.')

def menu_editar_usuario(usuarios):
    print('\nUsuários disponíveis:')
    for i, usuario in enumerate(usuarios, 1):
        print(f'{i} - {usuario.nome}')

    opcao = int(input('Digite o número do usuário que deseja editar: '))
    if opcao < 1 or opcao > len(usuarios):
        print('Opção inválida.')
        return None

    return usuarios[opcao - 1]

def editar_usuario(usuario):
    while True:
        print('\nEditar Usuário:')
        print('1 - Editar Nome')
        print('2 - Editar Data de Nascimento')
        print('3 - Editar CPF')
        print('4 - Editar Endereço')
        print('5 - Voltar')

        opcao = int(input('Digite o número da informação que deseja editar: '))

        if opcao == 1:
            novo_nome = input('Digite o novo nome: ')
            usuario.nome = novo_nome
            print('Nome atualizado com sucesso.')
        elif opcao == 2:
            nova_data_nascimento = input('Digite a nova data de nascimento: ')
            usuario.data_nascimento = nova_data_nascimento
            print('Data de Nascimento atualizada com sucesso.')
        elif opcao == 3:
            novo_cpf = input('Digite o novo CPF: ')
            usuario.cpf = novo_cpf
            print('CPF atualizado com sucesso.')
        elif opcao == 4:
            novo_logradouro = input('Digite o novo logradouro: ')
            novo_numero = input('Digite o novo número: ')
            novo_bairro = input('Digite o novo bairro: ')
            nova_cidade_uf = input('Digite a nova cidade/UF: ')
            novo_endereco = f"{novo_logradouro}, {novo_numero} - {novo_bairro} - {nova_cidade_uf}"
            usuario.endereco = novo_endereco
            print('Endereço atualizado com sucesso.')
        elif opcao == 5:
            break
        else:
            print('Opção inválida. Tente novamente.')
            
