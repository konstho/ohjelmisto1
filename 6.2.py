import random
def noppa():
    return random.randint(1, max)


max = int(input("anna maksimisilmä luku: "))
while True:
    luku = noppa()
    print(luku)
    if luku == max:
        break