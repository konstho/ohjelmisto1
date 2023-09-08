talvi = (12,1,2)
kevät = (3,4,5)
kesä = (6,7,8)
syksy = (9,10,11)
kk = int(input("anna kuukausi: "))
if kk in (talvi):
    print("talvi")
elif kk in (kevät):
    print("kevät")
elif kk in (kesä):
    print("kesä")
elif kk in (syksy):
    print("syksy")