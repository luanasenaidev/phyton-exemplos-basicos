#Variáveis 
nome = "Kaue Xavier"
idade = 15

#Exibição de valores 
print(nome)
print(idade)
print("\n")

#1º método de concatenação (string: str)
print("O meu nome é: " + nome + " e tenho " + str(idade) + " anos.\n")

#2º método de concatenação (format)
print("O meu nome é {} e tenho {} anos.\n".format(nome, idade))

#3º método de concatenação (f string)
print(f"O meu nome é: {nome} e tenho {idade} anos.")