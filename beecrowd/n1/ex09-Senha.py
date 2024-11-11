import sys

for linha in sys.stdin:

    N = int(linha.strip())
    
    senha = N - 1
    
    print(senha)
