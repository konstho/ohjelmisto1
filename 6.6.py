import math
def laske(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija/2)**2
    yht = hinta/halkaisija
    return yht

pizza1 = int(input("anna halkaisija: "))
hinta1 = int(input("anna hinta: "))
pizza2 = int(input("anna halkaisija; "))
hinta2 = int(input("anna hinta: "))

y1 = laske(pizza1, hinta1)
y2 = laske(pizza2, hinta2)
if y1 < y2:
    print("ensimmäinne pizza antaa paremman vastineen")
elif y1 > y2:
    print("toinen pizza anta paremman vastineen")
else:
    print("molemmat ovat samanhintaisia")