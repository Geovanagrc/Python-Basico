verificador = False
while verificador == False:
    try:
        idade = int(input("Insira a sua idade: "))
        if type(idade) == int: verificador = True
    except ValueError:
        print("O valor inserido não é um número inteiro, por favor insira novamente!\n")

for i in range(1,idade+1):
    print(i, end=", ")
    if i%5==0:print()