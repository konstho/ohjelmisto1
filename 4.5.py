x = 0
while x < 5:
    kt = input("anna käyttäjätunnus: ")
    sa = input("anna salasana: ")
    if kt == "python" and sa == "rules":
        print("tervetuloa")
        break
    else:
        print("väärä tunnus")
    x = x + 1