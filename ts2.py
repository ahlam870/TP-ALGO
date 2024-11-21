def tri(T):
    n = len(T)

    
    for i in range(n // 2 - 1, -1, -1):  
        entasser(T, n, i)

    
    for i in range(n - 1, 0, -1):
        
        T[0], T[i] = T[i], T[0]

        
        entasser(T, i, 0)  
    return T

def entasser(T, n, i):
    max_idx = i  
    g = 2 * i + 1  # Fg
    d = 2 * i + 2  # Fd

    
    if g < n and T[g] > T[max_idx]:
        max_idx = g

    
    if d < n and T[d] > T[max_idx]:
        max_idx = d

    
    if max_idx != i:
        T[i], T[max_idx] = T[max_idx], T[i]
        
        entasser(T, n, max_idx)

AR = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]

print("Avant le tri par tas :")
print(AR)


AR_trie = tri(AR)

print("Après le tri par tas :")
print(AR_trie)

