X = int(input())

if 1 <= X <= 1000:
    for i in range(1, X + 1):
        if i % 2 != 0:
            print(i)
else:
    print("O valor deve estar entre 1 e 1000.") 