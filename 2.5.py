l = float(input("anna leiviskät: "))
n = float(input("anna naulat:  "))
lu = float(input("anna luodit: "))
x =  l * 20 * 32 * 13.3
y = n * 32 * 13.3
z = lu * 13.3
kg = x + y + z
kilot = int(kg // 1000)
grammat = round(kg % 1000 , 2)
print(f"massa nykymittojen mukaan: {kilot} kilogrammaa ja {grammat} grammaa")