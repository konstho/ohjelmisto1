sukup = input("anna sukupuoli: ")
hemog = float(input("anna hemoglobiini arvo: "))
if sukup == "nainen":
    if 117 <= hemog <= 175:
        print("normaali arvo")
    elif hemog < 117:
        print("alhainen arvo")
    else:
        print("korkea arvo")
if sukup == "mies":
    if 134 <= hemog <= 195:
        print("normaali arvo")
    elif hemog < 134:
        print("alhainen arvo")
    else:
        print("korkea arvo")