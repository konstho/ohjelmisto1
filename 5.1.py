import random
luku = int(input("anna lukumäärä: "))
x = 0
for i in range (luku):
    noppa = random.randint(1,6)
    x += noppa
print(x)