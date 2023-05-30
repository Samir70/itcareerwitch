'''test code'''
A = 5
B = 5
C = A
print("[A, B, C] = ", A, B, C)
print("A is B: ", A is B)
print("A is C: ", A is C)

print("------------------------------")

A = [1, 2, 3]
B = [1, 2, 3]
C = A
print("[A, B, C] = ", A, B, C)
print("A is B: ", A is B, "A == B", A == B)
print("A is C: ", A is C)

# [A, B, C] =  5 5 5
# A is B:  True
# A is C:  True
# ------------------------------
# [A, B, C] =  [1, 2, 3] [1, 2, 3] [1, 2, 3]
# A is B:  False A == B True
# A is C:  True
