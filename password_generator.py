import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

signs = ['(', ')', '*', '&', '#', '@', '%', '$', '!', '?']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_pw = []

mali_bukvi = int(input("Vnesi kolku mali bukvi sakas da ima vo passwordot "))
golemi_bukvi = int(input("Vnesi kolku golemi bukvi sakas da ima vo passwordot "))
znaci = int(input("Kolku znaci: "))

for i in range(mali_bukvi):
    lista_pw.append(random.choice(mali_bukvi))

for i in range(golemi_bukvi):
    lista_pw.append(uppercase_letters[random.randint(0,len(uppercase_letters) - 1)])

for i in range(znaci):
    lista_pw.append(signs[random.randint(0,len(signs) - 1)])

random.shuffle(lista_pw)

pasword_text = "".join(lista_pw)
print(pasword_text)
