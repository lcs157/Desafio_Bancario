# n1 = input("Digite um numero: ")
# n1_int = int(n1)
# print(n1_int)

# n1_int +=1
# print(n1_int)


# n1_int +=1
# print(n1_int)

# texto = input("Informe uma palavra: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end=" ")
# print()


# for numero in range (0,51,5):
#     print(numero)

numero = -1

while numero !=0:
    numero= input("[1] sacar \n [2] ver extrao \n [3] sair \n : ")
    numero_int = int(numero)

    if numero_int == 1:
        print("Ola mundo!")
    elif numero_int == 2:
        print("Ver extrato!")
    elif numero_int == 3:
        print("Finalizando")
        break

