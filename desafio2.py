def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input (menu)

def depositar(saldo, valor, extrato):
    if valor < 0:
        saldo += valor
        extrato += f"Depósito no valor de   {valor:.2f}"
        print ("Depósito efetuado com sucesso")
    
    else:
        print ('Operação falhou')

    return saldo,extrato
    





saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(*, saldo, valor, extrato, limite, numero-saques, limite_saques):
    
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

    def exibir_extrato (sado, extrato): 

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    def criar_usuario (usuarios):
        cpf = input ('Informe o número do cpf - sem traços e pontos: ')
        usuario = filtrar_usuario(cpf, usuarios) 

        if usuario:
            print ('Já existe usuário informado com esse CPF')
            return

        nome = input ('Informe o nome completo: ')
        data_nascimento = input ('Informe data de nascimento: ')

        usuarios.append ({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf} )

        print ('Usuário criado com sucesso')

    def fitrar_usuario(cpf, usuarios):
        usuarios_filtrados=[usuario for usuario in usuarios if usuario  ['cpf'] == cpf ]
        return usuarios_filtrados [0] if usuarios_filtrados else None    


    def criar_conta(agencia, num_conta, usuarios):
        cpf = input ('Informe o CPF: ')
        usuario = fitrar_usuario (cpf, usuarios)

        if usuario:
            print ("Conta criada com sucesso!")
            return {'Agência': agencia, 'Num_conta': num_conta, 'Usuários': usuarios}

    def listar_contas(contas):
        for conta in contas:
            Agência: {conta ['agencia']}
            Conta: {conta ['numero da conta']}
            Titular: {conta ['usuario'] ['nome']}


    