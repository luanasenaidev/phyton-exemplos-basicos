# menu com opções de comida
print("Escolha uma opção:")
print("1: Pizza")
print("2: Hambúrguer")
print("3: Salada")

opcao = int(input("Digite o número da opção desejada: "))

match opcao:
    case 1:
        comida = "Pizza"
    case 2:
        comida = "Hambúrguer"
    case 3:
        comida = "Salada"
    case _:
        comida = "Opção inválida"

# Exibe a comida selecionada ou uma mensagem de erro
print(f"Você escolheu: {comida}")
