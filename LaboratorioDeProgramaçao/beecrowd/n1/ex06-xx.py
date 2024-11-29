N = int(input())

for i in range(1, N + 1):
    primeiro = i
    segundo = i ** 2
    terceiro = i ** 3
    
    print(f"{primeiro} {segundo} {terceiro}")
    
    print(f"{primeiro} {segundo + 1} {terceiro + 1}")
