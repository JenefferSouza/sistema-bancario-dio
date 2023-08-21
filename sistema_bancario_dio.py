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
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação: O valor informado é inválido, tente novamente!")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação: Saldo insuficiente!")
        elif excedeu_limite:
            print("Falha na operação: O valor inserido excede o limite de saque, tente novamente!")
        elif excedeu_saques:
            print("Falha na operação: Limite de saques diários atingido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação: O valor informado é inválido!")

    elif opcao == "e":
        print("\n******* EXTRATO *******")
        print("Não houve movimentações realizada!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("***********************")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor tente novamente!")
