print("Seja muito bem-vindo(a) ao Quiz do Michel!")
escolha_usuario = input("Deseja iniciar? (Sim/Não)")
score = 0
print(escolha_usuario)
if escolha_usuario.strip().lower() != "sim":
    quit()
print("Iniciando...")

print("Qual é a capital do Brasil?\n A) São Paulo\n B) Rio de Janeiro\n C) Curitiba\n D) Brasília ")
alternativa_1 = input("Resposta")
print(alternativa_1)
if alternativa_1.strip().lower() == "d":
    print("Resposta correta!")
    score = score +1
else:
    print("Resposta errada :(")

print("Qual desses animais é um mamífero? \n A) Jacaré \n B) Tubarão \n C) Baleia \n D) Galinha ")
alternativa_1 = input("Resposta")
print(alternativa_1)
if alternativa_1.strip().lower() == "c":
    print("Resposta correta!")
    score = score +1
else:
    print("Resposta errada :(")

print("Qual planeta é conhecido como o Planeta Vermelho? \n A) Vênus \n B) Marte \n C) Júpiter \n D) Terra ")
alternativa_1 = input("Resposta")
print(alternativa_1)
if alternativa_1.strip().lower() == "b":
    print("Resposta correta!")
    score = score +1
else:
    print("Resposta errada :(")

print("Quantas cores tem o arco-íris? \n A) 5 \n B) 6 \n C) 7 \n D) 8 ")
alternativa_1 = input("Resposta")
print(alternativa_1)
if alternativa_1.strip().lower() == "c":
    print("Resposta correta!")
    score = score +1
else:
    print("Resposta errada :(")

print(f"Parabéns você chegou ao fim deste código, muito obrigado por participar! \nSeu total de pontos é {score}/4")
exit()
