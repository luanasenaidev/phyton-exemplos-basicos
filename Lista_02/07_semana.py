# Solicita ao usuário que insira um dia da semana
dia = input("Digite um dia da semana: ").strip().capitalize()

# Usa a estrutura match para verificar se é um dia útil ou fim de semana
match dia:
    case "Segunda-feira" | "Terça-feira" | "Quarta-feira" | "Quinta-feira" | "Sexta-feira":
        tipo_dia = "Dia útil"
    case "Sábado" | "Domingo":
        tipo_dia = "Fim de semana"
    case _:
        tipo_dia = "Dia da semana inválido"

# Exibe se o dia é útil ou fim de semana, ou uma mensagem de erro
print(f"{dia} é um {tipo_dia}.")
