valor = int(input("Informe o valor: "))

#Uso do if ternario
teste = "Situação normal!" if valor > 100 else "Situação: Pré-diabetes!" if valor in range (100,125) else "Diabetes"

#Exibição
print(teste)