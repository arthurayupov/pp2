import math
def Valume(radius):
    valume = (4 / 3) * math.pi * radius**3
    return valume

rad = float(input("enter radius values: "))
ans = Valume(rad)
print("Valume equal: ", ans)