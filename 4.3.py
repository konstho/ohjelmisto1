pnumero = float("inf")
snumero = float("-inf")
while True:
    luku = input("syötä minulle lukuja: ")
    if luku == "":
        break
    luku = float(luku)
    if snumero < luku:
        snumero = luku
    if pnumero > luku:
        pnumero = luku
print("pieni luku: ", pnumero)
print("suuri luku: " , snumero)