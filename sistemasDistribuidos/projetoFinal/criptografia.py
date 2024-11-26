from random import shuffle
from time import sleep
import sys

# Lista de todos os caracteres possíveis para criptografia
caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", ',', '.', '<', '>', '?', '/']

def criptografa(msg, key):
    # Função de criptografia que desloca caracteres usando a chave fornecida
    msgCriptografada = list()
    for l in msg:
        if l == " ":
            msgCriptografada.append(" ")
        for i in caracteres:
            if l == i:
                # Usa módulo para manter o índice dentro do limite da lista
                index = caracteres.index(l)
                msgCriptografada.append(caracteres[(index + key) % len(caracteres)])
    return "".join(msgCriptografada)

def descriptografia(msg, key):
    # Função de descriptografia que reverte o deslocamento da criptografia
    msgDescriptografada = list()
    for l in msg:
        if l == " ":
            msgDescriptografada.append(" ")
        for i in caracteres:
            if l == i:
                # Desloca para trás usando a mesma lógica da criptografia
                index = caracteres.index(l)
                msgDescriptografada.append(caracteres[(index - key) % len(caracteres)])
    return "".join(msgDescriptografada)

print("=== Criptografia Segura ===\n")

# Loop para escolher entre criptografia padrão ou segura
while True:
    opcaoS = input("Você prefere uma criptografia padrão ou uma versão mais segura? ").strip().lower()

    if "padrão" in opcaoS or "padrao" in opcaoS:
        # Modo padrão: lista de caracteres fixa
        opcaoS = False
        print("Você escolheu a criptografia padrão.\n")
        break
    elif "segura" in opcaoS or "mais segura" in opcaoS:
        # Modo seguro: embaralha a lista de caracteres
        opcaoS = True
        print("Você escolheu uma criptografia mais segura...\n")
        break
    else:
        print("Opção inválida. Por favor, escolha entre 'padrão' ou 'mais segura'.\n")
        continue

# Menu principal do programa
while True:
    print("Escolha uma opcao:\n")
    print("1 - Criptografar mensagem")
    print("2 - Descriptografar mensagem")
    print("3 - Sair")
    opcao = int(input("Opcao: "))

    match opcao:
        case 1:
            # Caso de criptografia: embaralha caracteres se modo seguro estiver ativo
            if opcaoS:
                shuffle(caracteres)

            # Solicita mensagem e chave para criptografia
            mensagem = input("Insira a mensagem para ser criptografada: ")
            key = int(input("Insira a chave: "))
            msgCriptografada = criptografa(list(mensagem), key)
            print(f"Mensagem criptografada: {msgCriptografada}")

        case 2:
            # Caso de descriptografia: solicita mensagem e chave
            mensagem = input("Insira a mensagem para ser descriptografada: ")
            key = int(input("Insira a chave: "))
            msgDescriptografada = descriptografia(list(mensagem), key)
            print(f"Mensagem descriptografada: {msgDescriptografada}")

        case 3:
            # Caso de saída: adiciona animação de encerramento
            if opcaoS:
                # Animação de "apagando dados" no modo seguro
                print("Apagando Dados", end="")
                for _ in range(3):
                    sleep(0.5)
                    print(".", end="")
                    sys.stdout.flush()
                sleep(0.5)

                # Animação de encerramento
                print("\nEncerrando o programa", end="")
                for _ in range(3):
                    sleep(0.5)
                    print(".", end="")
                    sys.stdout.flush()
                sleep(0.5)
                break
            else:
                # Animação de encerramento no modo padrão
                print("Encerrando o programa", end="")
                for _ in range(3):
                    sleep(0.5)
                    print(".", end="")
                    sys.stdout.flush()
                sleep(0.5)
                break
        case _:
            # Trata opções inválidas
            print("Opção invalida, selecione novamente\n")