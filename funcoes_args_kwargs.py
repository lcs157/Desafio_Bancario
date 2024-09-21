def exibir_poema(data_extenso, *tupla, **dicionario):
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" 
                            for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
exibir_poema("zen of python ", "beautiful is better than ugly", 
             autor = "Tim Petters", ano = 1999) #args armazena argumentos nao nomeados, e transforma tudo em tupla 

#kwargs armazena argumentos nomeados e tem saida como dicionario pois recebe chave e valor