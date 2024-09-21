print("Bem Vindo ao Pique Bank")

menu = (
    "[1]: SACAR \n"
    "[2]: DEPOSITO \n"
    "[3]: VER EXTRATO \n"
    "[4]: SAIR\n"
)

saldo = 500
limite_por_saque = 500
extrato = ""  # Armazena o histórico de transações
saques_diario = 0
NUM_SAQUE_PERMITIDO = 3

while True:
    if saques_diario >= NUM_SAQUE_PERMITIDO:
        print("Você não pode mais realizar saques hoje! Reinicie o App.")
        break

    opcao = int(input(f"Escolha uma das opções abaixo:\n{menu}"))

    # PARTE DO SAQUE
    if opcao == 1:
        sacar = float(input("Quanto você deseja sacar: "))

        if sacar <= saldo and sacar <= limite_por_saque:
            saldo -= sacar
            saques_diario += 1
            extrato += f"Saque de R${sacar:.2f}\n"  # Adiciona o saque ao extrato
            print(f"Você sacou R${sacar:.2f}. Seu novo saldo é de R${saldo:.2f}")
        else:
            print("Saque não permitido. Verifique o saldo ou o limite de saque.")

    # PARTE DEPOSITO
    elif opcao == 2:
        depositar = float(input("Quanto você deseja depositar: "))
        
        if depositar > 0:
            saldo += depositar
            extrato += f"Depósito de R${depositar:.2f}\n"  # Adiciona o depósito ao extrato
            print(f"Você depositou R${depositar:.2f}. Seu saldo atual é de R${saldo:.2f}")
        else:
            print("Depósito inválido.")

    # VER EXTRATO
    elif opcao == 3:
        print("\n==== EXTRATO ====")
        print("Sem movimentações." if not extrato else extrato)  # Mostra o extrato se houver movimentações
        print(f"Saldo atual: R${saldo:.2f}")
        print("=================\n")

    # SAIR
    elif opcao == 4:
        print("Obrigado por usar o Pique Bank!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")
