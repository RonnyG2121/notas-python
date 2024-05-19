# Sucesión de fibonacci


limite = 15
n1 = 0
n2 = 1
s = 0
while s < limite:
    print(f"n1 {n1}")
    print(f"n2 {n2}")
    print(F"s {s}")
    n1 = n2
    n2 = s
    s = n1  + n2
