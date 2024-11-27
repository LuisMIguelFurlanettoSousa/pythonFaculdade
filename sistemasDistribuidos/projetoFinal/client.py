import socket
import time

# Configurações do servidor
HOST = '192.168.0.110'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            print("\nEscolha uma opção:")
            print("1 - Criptografar mensagem")
            print("2 - Descriptografar mensagem")
            print("3 - Sair")
            opcao = input("Opção: ").strip()

            if opcao == '3':
                print("Encerrando o cliente...")
                break

            mensagem = input("Insira a mensagem: ")
            tipo = input("Tipo (padrao/simetrica/assimetrica): ").strip()
            chave = input("Insira a chave (para simétrica, deixe em branco para outras): ").strip() or '0'

            if opcao == '1':
                operacao = 'criptografar'
            elif opcao == '2':
                operacao = 'descriptografar'
            else:
                print("Opção inválida. Tente novamente.")
                continue

            envio = f"{operacao};{mensagem};{tipo};{chave}"
            s.sendall(envio.encode())

            data = s.recv(1024).decode()
            resultado, relogio_logico = data.split(';')
            print(f"Resultado: {resultado}")
            print(f"Relógio lógico: {relogio_logico}")

if __name__ == "__main__":
    main()
