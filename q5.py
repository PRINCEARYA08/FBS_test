L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 5, 6, 7]

union = L1.copy()

for num in L2: 
    if num not in union:
        union.append(num)

print(union) 