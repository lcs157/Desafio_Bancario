# def exibir_mensagem(bom_dia):
#     return bom_dia

# n1 = exibir_mensagem("Bom dia")

# print(n1)


# def exibir_menssagem():
#     print("Olá Mundo!!")

# def exibir_menssagem_2(nome):
#     print(f"Seja bem vindo {nome}")

# def exibir_menssagem_3(nome = "Lucas"):
#     print(f"Seja bem vindo {nome}")

# exibir_menssagem()

# exibir_menssagem_2("Lucas")

# exibir_menssagem_3()

# exibir_menssagem_3("Massari")



# def calcular_numeros(numeros):
#     return sum(numeros)


# def sucessor_antecessor(numeros):
#     antecessor  = numeros - 1
#     sucessor = numeros + 1

#     return sucessor, antecessor



# print(calcular_numeros([10,20,30,40]))

# print(sucessor_antecessor(10))


def salvar_carro(marca, modelo, cor, ano):
    return marca, modelo, cor, ano


print(salvar_carro(marca = "Hyundai", modelo = "Elantra", cor = "Branco",ano =  2024))
print(salvar_carro(**{"marca": "Hyundau", "modelo": "Elantra", "cor": "Branco", "ano": "2024"}))


    