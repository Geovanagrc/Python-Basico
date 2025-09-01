firstName = 'Geovana' #String
altura = 1.62   # Float
idade = 20 #Integer
professor = True # Boolean

print(type(firstName)) # Método que imprime o tipo de dado
print(idade,end = ' e ')
print(altura)
print(professor)
print(20*'-')
#Entradas(inputs)
frase = '\nHoje é dia {:>02} de {} de {}' # {:>02} especificador de formato de String.
dia,mes,ano = input("Que dia é hoje?"), input("De que mês?"),input("De qual ano?")
print(frase.format(dia,mes.capitalize(),ano))