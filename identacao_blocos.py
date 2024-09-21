# def sacar(self, valor: float)-> None: #Inicio do bloco Metodo 
#     if self.saldo >= valor: #Inicio do bloco if 
#         self.saldo -= valor
#     #fin do bloco do IF

# #Fin do bloco do metodo 



def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado") #executa caso o valor seja menor do que o saldo
        print("Retire seu dinheiro na boca do caixa ")#executa caso o valor seja menor do que o saldo
    print("Obrigado por ser nosso cliente")#executa em ambas situações pois esta fora do if
sacar(1000)

