def menu():
    return input("""\n
Selecione a operação que deseja realizar:

[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo usuário
[5]\tNova Conta
[6]\tSair
=> """)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===========================================")

def criar_user(users):
    cpf = input("Informe o CPF (somente números): ")
    user = filtrar_user(cpf, users)

    if user:
        print("\nJá existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nº - Bairro - Cidade/UF): ")

    users.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_user(cpf, users):
    users_filtrados = [user for user in users if user["cpf"] == cpf]
    return users_filtrados[0] if users_filtrados else None

def criar_conta(agencia, num_conta, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filtrar_user(cpf, users)

    if user:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "num_conta": num_conta, "user": user}

    print("Usuário não encontrado. Fluxo de criação de conta encerrado.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    users = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_user(users)

        elif opcao == "5":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, users)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            break

        else:
            print("Operação inválida! Por favor, selecione novamente.")

main()
