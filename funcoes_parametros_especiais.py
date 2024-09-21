def criar_carro1(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro1("ELANTRA",2024,"LU5M34", marca = "HYUNDAY", motor = "2.0 HYBRID", 
            combustivel="GASOLINA, ALCOOL, BATERIA") #QUANDO ESTOU USANDO A BARRA ENTRE OS PARAMETROS
# E O PYTHON DIFERE QUE OQUE VEM ANTES DA BARRA TEM QUE SER ARGUMENTOS NAO NOMEADOS E OQUE VEM DEPOIS 
# PODE SE FAZER A ESCOLHA SE VAI SER NOMEADO OU NAO


def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo = "ELANTRA",ano = 2024,placa = "LU5M34", marca = "HYUNDAY", motor = "2.0 HYBRID", 
            combustivel="GASOLINA, ALCOOL, BATERIA")#Quando quero que todos os argumentos sejam 
# passados com chave e valor uso o asteristico no inicio da funcao antes dos parametros


def criar_carro3(modelo, ano, placa,/,*, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("ELANTRA",2024, "LU5M34", marca = "HYUNDAY", motor = "2.0 HYBRID", 
            combustivel="GASOLINA, ALCOOL, BATERIA")#Mais facil ultilizar o primeiro