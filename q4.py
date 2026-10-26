L = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

D = {}

for num in L:
    D[num] = L.count(num)

print(D)