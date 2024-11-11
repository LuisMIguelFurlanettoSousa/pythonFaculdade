T = int(input())

for t in range(1, T + 1):
    method = input().strip()
    
    R, G, B = map(int, input().split())

    if method == "eye":
        P = int(0.30 * R + 0.59 * G + 0.11 * B)
    elif method == "mean":
        P = int((R + G + B) / 3)
    elif method == "max":
        P = max(R, G, B)
    elif method == "min":
        P = min(R, G, B)
    else:
        continue

    print(f"Caso #{t}: {P}")