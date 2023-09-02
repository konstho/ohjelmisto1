luku = int(input("anna luku: "))
for i in range(2, luku - 1):
    if luku % i == 0:
        print("luku ei ole alkuluku")
        break
else:
    print("luku on alkuluku")