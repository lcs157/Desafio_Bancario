# saldo = 2000.0
# saque = float(input("Digite um valor: "))


# if saldo >= saque:
#     print("Saque realizado com sucesso")

# if saldo < saque:
#     print("Voce nao tem saldo o suficiente")


# import sys


# opcao = int(input("Informe a opcao: [1]sacar \n[2] Extrato:  "))

# if opcao == 1:
#     valor = float(input("Digite um valor para o saque: "))
#     print(f"Voce sacou {valor}R$")


# elif opcao==2:
#     print("Exibindo o extrato...")
# else:
#     sys.exit("Opcao invalida")

# MAIOR_IDADE = 18

# idade = int(input("Qual sua idade ?"))

# if idade >= 18:
#     print("Voce e maior de idade, pode tirar sua CNH")
# else:
#     print("Voce é menor de idade.\n espere mais alguns anos para poder tirar sua carteira.")

saldo = 5000.0
cheque_especial = 1000.0
opcao = float(input("Qual conta vc quer ultilizar?\n" "[1]: conta_normal\n" "[2]: conta_universitaria:  "))
saque = float(input("Digite o valor que quer sacar:  "))


if opcao == 1:
    if saldo>= saque:
        print("Saque permitido. ")
    elif saque<= (saldo + cheque_especial):
        print("Saque realizado com cheque especial.")
    elif saque > (saldo + cheque_especial):
        print(f"Seu saldo excede seu limite com o cheque especial.\n Seu saldo e de {saldo + cheque_especial}")

if opcao == 2:
    if saldo >= saque:
        print("Saque permitido.")
    elif saldo < saque:
        print("Saque negado")

            