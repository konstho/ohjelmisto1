import random
oikein = random.randint(1,10)
while True:
    luku = int(input("arvaa luku: "))
    if luku < oikein:
        print("luku on pieni")
    elif luku > oikein:
        print("luku on iso")
    else:
        print("luku on oikein")
        break