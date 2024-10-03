senha_correta = "12345"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta!")
        tentativas += 1

if tentativas == 3:
    print("Número de tentativas excedido.")
