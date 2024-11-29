from math import factorial

def anagramas(p):
    # Calcula o fatorial do número total de letras
    fatNum = factorial(len(p))
    letrasR = 1
    
    # Contabiliza as repetições de cada letra
    for letra in set(p):  # Usa `set` para evitar contar a mesma letra  vezes
        qnt = p.count(letra)
        if qnt > 1:
            letrasR *= factorial(qnt)  # Multiplica o fatorial das repetições
    
    # Divide o fatorial total pelas repetições
    return int(fatNum / letrasR)


p = input().lower()

anaG = anagramas(p)
print(anaG)