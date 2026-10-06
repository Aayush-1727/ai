1. Associative add :

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

lhs = (a + b) + c
rhs = a + (b + c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Associative law of addition is satisfied")
else:
    print("Associative law of addition is not satisfied")

2. associative multiply:

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

lhs = (a * b) * c
rhs = a * (b * c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Associative law of multiplication is satisfied")
else:
    print("Associative law of multiplication is not satisfied")


3. associative bool :
a = True
b = False
c = True

lhs = (a and b) and c
rhs = a and (b and c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Associative law of AND is satisfied")
else:
    print("Associative law of AND is not satisfied")


4. distributive add/multi

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

lhs = a * (b - c)
rhs = (a * b) - (a * c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Distributive law is satisfied")
else:
    print("Distributive law is not satisfied")

5. dist subtraction:

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

lhs = a * (b - c)
rhs = (a * b) - (a * c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Distributive law is satisfied")
else:
    print("Distributive law is not satisfied")

6. dist bool:

a = True
b = False
c = True

lhs = a and (b or c)
rhs = (a and b) or (a and c)

print("LHS =", lhs)
print("RHS =", rhs)

if lhs == rhs:
    print("Distributive law of AND over OR is satisfied")
else:
    print("Distributive law of AND over OR is not satisfied")
