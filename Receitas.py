import json

print("Cadastro de receitas")

receitas = []

def cadastrar_receita():
    ingredientes = input("Digite os ingredientes necessários: ")
    modo_de_preparo = input("Digite o modo de preparo: ")
    receita = {
        "ingredientes": ingredientes,
        "modo de preparo": modo_de_preparo
    }
    receitas.append(receita)
    print("Receita cadastrada com sucesso!")

def listar_receitas():
    if not receitas:
        print("Nenhuma receita cadastrada.")
    else:
        for i, receita in enumerate(receitas):
            print(f"Receita {i + 1}:")
            print(f"Ingredientes: {receita['ingredientes']}")
            print(f"Modo de Preparo: {receita['modo de preparo']}\n")

def buscar_receita():
    ingrediente_busca = input("Digite um ingrediente para buscar a receita: ")
    encontradas = [receita for receita in receitas if ingrediente_busca in receita['ingredientes']]
    
    if not encontradas:
        print("Nenhuma receita encontrada com esse ingrediente.")
    else:
        for i, receita in enumerate(encontradas):
            print(f"Receita {i + 1}:")
            print(f"Ingredientes: {receita['ingredientes']}")
            print(f"Modo de Preparo: {receita['modo de preparo']}\n")

def salvar_receitas():
    with open('receitas.json', 'w') as file:
        json.dump(receitas, file)
    print("Receitas salvas com sucesso!")

def carregar_receitas():
    global receitas
    try:
        with open('receitas.json', 'r') as file:
            receitas = json.load(file)
    except FileNotFoundError:
        receitas = []
    print("Receitas carregadas com sucesso!")

carregar_receitas()

while True:
    opcao = input("\nDigite 1 para cadastrar uma receita, 2 para listar receitas, 3 para buscar receita, 4 para salvar receitas, ou qualquer outra tecla para sair: ")

    if opcao == "1":
        cadastrar_receita()
    elif opcao == "2":
        listar_receitas()
    elif opcao == "3":
        buscar_receita()
    elif opcao == "4":
        salvar_receitas()
    else:
        print("Saindo...")
        break