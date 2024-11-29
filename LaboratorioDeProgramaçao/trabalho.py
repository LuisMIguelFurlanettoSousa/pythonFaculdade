import json

# Função para carregar os dados do arquivo
def carregar_dados():
    try:
        with open("clientes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar os dados no arquivo
def salvar_dados():
    with open("clientes.json", "w") as f:
        json.dump(clientes, f, indent=4)

# Dicionário para armazenar dados do cliente
clientes = carregar_dados()

# Função para criar uma conta para o cliente
def criar_conta():
    nome = input("Digite o nome do cliente: ")
    if nome in clientes:
        print("Conta já existente!")
    else:
        clientes[nome] = {"saldo": 0, "historico": []}
        print(f"Conta criada para {nome}.")
        salvar_dados()

# Função para consultar saldo
def consultar_saldo(nome):
    if nome in clientes:
        print(f"Saldo de {nome}: R${clientes[nome]['saldo']:.2f}")
    else:
        print("Cliente não encontrado.")

# Função para realizar depósitos
def realizar_deposito(nome):
    if nome in clientes:
        valor = float(input("Digite o valor para depósito: R$"))
        if valor > 0:
            clientes[nome]['saldo'] += valor
            clientes[nome]['historico'].append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            salvar_dados()
        else:
            print("Valor inválido para depósito.")
    else:
        print("Cliente não encontrado.")

# Função para realizar saques
def realizar_saque(nome):
    if nome in clientes:
        valor = float(input("Digite o valor para saque: R$"))
        if 0 < valor <= clientes[nome]['saldo']:
            clientes[nome]['saldo'] -= valor
            clientes[nome]['historico'].append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            salvar_dados()
        else:
            print("Valor inválido ou saldo insuficiente.")
    else:
        print("Cliente não encontrado.")

# Função para mostrar histórico de transações
def mostrar_historico(nome):
    if nome in clientes:
        if clientes[nome]['historico']:
            print(f"Histórico de transações de {nome}:")
            for transacao in clientes[nome]['historico']:
                print(transacao)
        else:
            print(f"{nome} não tem transações registradas.")
    else:
        print("Cliente não encontrado.")

# Função principal com o menu de opções
def menu():
    while True:
        print("\nBem-vindo ao Sistema Bancário!")
        print("1. Criar conta")
        print("2. Consultar saldo")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Mostrar histórico de transações")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            nome = input("Digite o nome do cliente: ")
            consultar_saldo(nome)
        elif opcao == "3":
            nome = input("Digite o nome do cliente: ")
            realizar_deposito(nome)
        elif opcao == "4":
            nome = input("Digite o nome do cliente: ")
            realizar_saque(nome)
        elif opcao == "5":
            nome = input("Digite o nome do cliente: ")
            mostrar_historico(nome)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o sistema
menu()