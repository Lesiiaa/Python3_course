###trying out sets###
A = {1, 54, 20, -1, 20}
B = {2,1,25,40,20}

A.add(7)
A.discard(54)
print(A)

print(A&B)
print(A|B)
print(A-B)
print(A^B)

print(A.issubset(B))

C = [3,4,5,7,7,8,4,-1]
print(set(C))