from datetime import datetime
from decimal import *
menu = """Escolha uma das opções:
[s] = Sacar
[d] = Depositar
[c] = Consultar
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def monetary_input(input_message: str):    
    while True:
        value = input(input_message).strip()
        value = value.replace(',', '.')
        try:
            return Decimal(value)
        except:
            print("Valor inválido, tente novamente\n")

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = monetary_input("Informe o valor => ")
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - R$ {deposito}\n"
            print("Depósito realizado com sucesso\n\nPressione ENTER para retornar ao menu")
            input()
        else:
            print("Valor negativo informado, tente novamente\nPressione ENTER para retornar ao menu")
            input()
    elif opcao == "c":
        print("============== EXTRATO BANCARIO ============== \n")
        print("== XPTO BANK ================================= \n")
        print(f"{extrato}\n")
        print(f"Saldo disponível: R$ {saldo}\n")
        print(f"== XPTO BANK ======== {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} ==== \n\nPressione ENTER para retornar ao menu")
        input()
    elif opcao == "s":
        saque = monetary_input("Quanto quer sacar: ")
        if saque < 0:
            print("Não é possível fazer saque de valor negativo\nPressione ENTER para retornar ao menu")
            input()
            continue
        if saque > saldo:
            print("Saldo insuficiente\nPressione ENTER para retornar ao menu")
            input()
            continue
        if saque > limite:
            print("Valor acima do permitido\nPressione ENTER para retornar ao menu")
            input()
            continue
        elif numero_saques < LIMITE_SAQUES:
            saldo -= saque
            extrato += f"Saque {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - R$ {saque}\n"
            numero_saques += 1
            print(f"Valor retirado: R$ {saque}\n")
            print(f"Saldo em conta: R$ {saldo}\n\nPressione qualquer tecla para retornar ao menu")
            input()
        else:
            print("Limite de saques diários atingido, saque não realizado\nPressione qualquer tecla para retornar ao menu")
            input()
            continue
    elif opcao == "q":
        print("Hasta la vista baby")
        break
    else:
        print("Opção inválida")