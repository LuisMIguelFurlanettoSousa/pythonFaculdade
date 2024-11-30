import socket
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import threading
import time

# Configurações do servidor
HOST = '192.168.43.6'
PORT = 7890

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

# Função para lidar com o cliente
def handle_client(conn, addr, private_key, public_key):
    print(f"Conectado a {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            operacao, mensagem, tipo, chave = data.split(';')
            chave = int(chave) if chave.isdigit() else None

            if operacao == 'criptografar':
                if tipo == 'padrao':
                    resultado = criptografa_padrao(mensagem)
                elif tipo == 'simetrica' and chave is not None:
                    resultado = criptografa_simetrica(mensagem, chave)
                elif tipo == 'assimetrica':
                    resultado = criptografar_assimetrico(mensagem, public_key)
            elif operacao == 'descriptografar':
                if tipo == 'padrao':
                    resultado = descriptografa_padrao(mensagem)
                elif tipo == 'simetrica' and chave is not None:
                    resultado = descriptografia_simetrica(mensagem, chave)
                elif tipo == 'assimetrica':
                    resultado = descriptografar_assimetrico(mensagem, private_key)

            # Adiciona um relógio lógico à resposta
            resultado_com_relogio = f"{resultado};{time.time()}"
            conn.sendall(resultado_com_relogio.encode())

        except Exception as e:
            print(f"Erro ao processar dados: {e}")
            break

    conn.close()
    print(f"Desconectado de {addr}")

def main():
    private_key, public_key = gerar_chaves()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor ouvindo em {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr, private_key, public_key))
            client_thread.start()

if __name__ == "__main__":
    main()
