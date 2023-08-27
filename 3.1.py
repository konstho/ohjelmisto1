kuhapituus = float(input("anna kuhan pituus: "))
raja = 37
if kuhapituus < raja:
    puuttuva = raja - kuhapituus
    print(f"kuhan pituudesta puuttuu {puuttuva} cm.")
else:
    print("kuhan pituus on yli rajan.")

