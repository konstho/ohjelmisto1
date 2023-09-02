luvut = []
while True:
    luku = input("anna luku: ")
    if luku == "":
        break
    lukux = int(luku)
    luvut.append(lukux)
luvut.sort(reverse=True)
print(luvut[:5])