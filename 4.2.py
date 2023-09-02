while True :
    tuuma = float(input("anna tuuma: "))
    if tuuma < 0:
        print("Ohjelma loppuu")
        break
    else:
        print(tuuma*2.54,"cm")
