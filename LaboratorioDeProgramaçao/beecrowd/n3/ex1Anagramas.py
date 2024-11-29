MOD = 10**9 + 7

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i % MOD
    return f

def mod_inverse(a):
    return pow(a, MOD - 2, MOD)

def count_anagrams(word):
    from collections import Counter
    n = len(word)
    freq = Counter(word)
    
    total_fact = factorial(n)
    
    for count in freq.values():
        total_fact = total_fact * mod_inverse(factorial(count)) % MOD
    
    return total_fact

word = input().strip()

result = count_anagrams(word)

print(result)