age = 25
name = "Lucas"
print(f"Your age is {age}, and your name is {name}")

age, name = (25, "Lucas")
print(f"your age is {age}, and your name is {name}")


valor = 500
valor_saque= float(input("Quanto vc quer sacar: "))
novo_valor = valor - valor_saque
print(f"Seu saldo é de {valor}, sacando {valor_saque}, voce ficara com o saldo de {novo_valor}")