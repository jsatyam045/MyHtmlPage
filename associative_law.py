# ---------------------------
# Associative Property Program
# ---------------------------

# --- Addition ---
print("\n--- Associative Property: Addition ---")
a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
c = int(input("Enter third number c: "))

lhs_add = (a + b) + c
rhs_add = a + (b + c)

print("LHS = (a + b) + c =", lhs_add)
print("RHS = a + (b + c) =", rhs_add)

if lhs_add == rhs_add:
    print("=> Addition is Associative\n")
else:
    print("=> Addition is NOT Associative\n")


# --- Multiplication ---
print("\n--- Associative Property: Multiplication ---")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

lhs_mul = (a * b) * c
rhs_mul = a * (b * c)

print("LHS = (a * b) * c =", lhs_mul)
print("RHS = a * (b * c) =", rhs_mul)

if lhs_mul == rhs_mul:
    print("=> Multiplication is Associative\n")
else:
    print("=> Multiplication is NOT Associative\n")


# --- Boolean AND ---
print("\n--- Associative Property: Boolean AND ---")
A = bool(int(input("Enter A (1 for True, 0 for False): ")))
B = bool(int(input("Enter B (1 for True, 0 for False): ")))
C = bool(int(input("Enter C (1 for True, 0 for False): ")))

lhs_and = (A and B) and C
rhs_and = A and (B and C)

print("LHS = (A and B) and C =", lhs_and)
print("RHS = A and (B and C) =", rhs_and)

if lhs_and == rhs_and:
    print("=> Boolean AND is Associative\n")
else:
    print("=> Boolean AND is NOT Associative\n")


# --- Boolean OR ---
print("\n--- Associative Property: Boolean OR ---")
A = bool(int(input("Enter A (1 for True, 0 for False): ")))
B = bool(int(input("Enter B (1 for True, 0 for False): ")))
C = bool(int(input("Enter C (1 for True, 0 for False): ")))

lhs_or = (A or B) or C
rhs_or = A or (B or C)

print("LHS = (A or B) or C =", lhs_or)
print("RHS = A or (B or C) =", rhs_or)

if lhs_or == rhs_or:
    print("=> Boolean OR is Associative\n")
else:
    print("=> Boolean OR is NOT Associative\n")
