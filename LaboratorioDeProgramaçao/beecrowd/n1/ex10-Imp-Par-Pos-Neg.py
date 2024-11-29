pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(5):
    valor = int(input())
    
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
