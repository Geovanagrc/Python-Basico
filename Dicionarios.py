produtos = {
    "PROD001":{"nome":"Notebook","preco":1500.00,"ID":1,"quantidade":10},
    "PROD002":{"nome":"Televisão","preco":3000.00,"ID":2,"quantidade":5},
    "PROD003":{"nome":"Mouse","preco":120.00,"ID":3,"quantidade":50},
    "PROD004":{"nome":"Teclado","preco":200.00,"ID":4,"quantidade":17}
}
print(20*"=","\nPRODUTOS DISPONÍVEIS")
print(20*"=")
for x in produtos:
    print(f'--> {x}')
print(80*"-")
while True:
    pesquisa = input("Digite a chave do produto que deseja encontrar: ").upper()
    if produtos.get(pesquisa) != None:
        produto_encontrado = produtos[pesquisa]
        print(f'\n--- Detalhes do produto {produto_encontrado["nome"]} ---')
        for chave, valor in produto_encontrado.items():
            print(f'--> {chave}: {valor}')
        print(80*"-")
    else:
        print(f'--- Produto {pesquisa.upper()} não encontrado ---')
    continuar = input("\nDeseja fazer outra pesquisa?(s/n) ").lower()
    while continuar != 'n' and continuar != 's':
        continuar = input("\nOpção inválida... Digite 's' ou 'n' para prosseguir: ").lower()
    if continuar == "n": break
print(30*"-"," Obrigado! ",30*"-")


