menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()[0]

    if opcao == "d":
         valor = input("Digite o valor a ser depositado: ")
         try:
            valor = float(valor)

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            else:
                print("Operação falhou! O valor informado é inválido.")
         except ValueError:
            print("Valor de depósito inválido. Por favor, insira um número válido.")
    elif opcao == "s":
        valor = input("Informe o valor do saque: ")
        try:
            valor = float(valor)
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
                print(f"Saque de R$ {valor:.2f} realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Valor de saque inválido. Por favor, insira um número válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
