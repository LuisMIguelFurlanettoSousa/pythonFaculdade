index = int(input().strip())
c = input().strip() 

m = []
for i in range(12):
    row = list(map(float, input().split())) 
    m.append(row)

sum_value = sum(m[index])

if c == 'S':
    print(f"{sum_value:.1f}")
elif c == 'M':
    average_value = sum_value / 12
    print(f"{average_value:.1f}")
