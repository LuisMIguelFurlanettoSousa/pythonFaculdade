from random import shuffle
from time import sleep
import base64
import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Lista de caracteres para criptografia padrão e simétrica
caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", ',', '.', '<', '>', '?', '/']

# Função de criptografia padrão
def criptografa_padrao(msg):
    msgCriptografada = list()
    for l in msg:
        if l == " ":
            msgCriptografada.append(" ")
        elif l in caracteres:
            index = caracteres.index(l)
            msgCriptografada.append(caracteres[(index + 3) % len(caracteres)])  # Deslocamento fixo de 3
    return "".join(msgCriptografada)

# Função de descriptografia padrão
def descriptografa_padrao(msg):
    msgDescriptografada = list()
    for l in msg:
        if l == " ":
            msgDescriptografada.append(" ")
        elif l in caracteres:
            index = caracteres.index(l)
            msgDescriptografada.append(caracteres[(index - 3) % len(caracteres)])  # Reverso do deslocamento fixo
    return "".join(msgDescriptografada)

# Função de criptografia simétrica
def criptografa_simetrica(msg, key):
    msgCriptografada = list()
    for l in msg:
        if l == " ":
            msgCriptografada.append(" ")
        elif l in caracteres:
            index = caracteres.index(l)
            msgCriptografada.append(caracteres[(index + key) % len(caracteres)])
    return "".join(msgCriptografada)

# Função de descriptografia simétrica
def descriptografia_simetrica(msg, key):
    msgDescriptografada = list()
    for l in msg:
        if l == " ":
            msgDescriptografada.append(" ")
        elif l in caracteres:
            index = caracteres.index(l)
            msgDescriptografada.append(caracteres[(index - key) % len(caracteres)])
    return "".join(msgDescriptografada)

# Funções para criptografia assimétrica
def gerar_chaves():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def criptografar_assimetrico(mensagem, public_key):
    ciphertext = public_key.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()

def descriptografar_assimetrico(ciphertext, private_key):
    decrypted_data = private_key.decrypt(
        base64.b64decode(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode()

# Inicialização
private_key, public_key = None, None
print("=== Criptografia Segura ===\n")

# Escolha do tipo de criptografia
while True:
    print("Escolha o tipo de criptografia:\n")
    print("1 - Padrão")
    print("2 - Simétrica")
    print("3 - Assimétrica")
    print("4 - Sair")
    
    opcaoS = input("Opção: ").strip()
    
    if opcaoS == "1":
        print("Você escolheu a criptografia padrão.\n")
        break
    elif opcaoS == "2":
        print("Você escolheu a criptografia simétrica.\n")
        break
    elif opcaoS == "3":
        print("Você escolheu a criptografia assimétrica.\n")
        private_key, public_key = gerar_chaves()
        print("Chaves geradas com sucesso!\n")
        break
    elif opcaoS == "4":
        print("Encerrando o programa", end="")
        for _ in range(3):
            sleep(0.5)
            print(".", end="")
            sys.stdout.flush()
        sleep(0.5)
        sys.exit()
    else:
        print("Opção inválida. Por favor, escolha novamente.\n")

# Menu principal
while True:
    try:
        print("\nEscolha uma opção:")
        print("1 - Criptografar mensagem")
        print("2 - Descriptografar mensagem")
        print("3 - Sair")
        opcao = int(input("Opção: "))

        if opcao == 1:
            mensagem = input("Insira a mensagem para ser criptografada: ")
            if opcaoS == "1":  # Padrão
                resultado = criptografa_padrao(mensagem)
            elif opcaoS == "2":  # Simétrica
                key = int(input("Insira a chave (número): "))
                resultado = criptografa_simetrica(mensagem, key)
            elif opcaoS == "3":  # Assimétrica
                resultado = criptografar_assimetrico(mensagem, public_key)
            print(f"Mensagem criptografada: {resultado}")

        elif opcao == 2:
            mensagem = input("Insira a mensagem para ser descriptografada: ")
            if opcaoS == "1":  # Padrão
                resultado = descriptografa_padrao(mensagem)
            elif opcaoS == "2":  # Simétrica
                key = int(input("Insira a chave (número): "))
                resultado = descriptografia_simetrica(mensagem, key)
            elif opcaoS == "3":  # Assimétrica
                resultado = descriptografar_assimetrico(mensagem, private_key)
            print(f"Mensagem descriptografada: {resultado}")

        elif opcao == 3:
            print("Encerrando o programa", end="")
            for _ in range(3):
                sleep(0.5)
                print(".", end="")
                sys.stdout.flush()
            sleep(0.5)
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
