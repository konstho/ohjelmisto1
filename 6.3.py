def bensiini(gallons):
    return gallons * 3.785

while True:
    gas = float(input("anna bensiinin määrä: "))
    if gas < 0:
        break
    litra = bensiini(gas)
    print(f"bensiinin määrä on {litra} litraa")