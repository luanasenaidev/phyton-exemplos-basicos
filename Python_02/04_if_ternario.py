velocidade = int(input("Informe a velocidade: "))

#Uso do if ternario
alerta = "Alta velocidade!" if velocidade > 60 else "Dentro do limite de velocidade."

#Exibição
print(alerta)