# Criar um programa que leia uma variável nota com input e mostre na tela:
# > 90 "Conceito A"
# entre 89 E 71 "Conceito B"
# entre 70 e 61 "Conceito C"
# entre 60 e 50 "Conceito D"
# < 49 "Conceito E"

nota = int(input("Digite uma nota: "))
if nota >= 90:
    print("Conceito A")
elif nota <= 89 and nota >= 71:
    print("Conceito B")
elif nota <= 70 and nota >= 61:
    print("Conceito C")
elif nota<= 60 and nota >= 50:
    print("Conceito D")
else: 
    print("Conceito E")



