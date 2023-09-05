lista = [1,2,3,4,5,6,7,8,9,10]
def x(lista):
    parittomat = [i for i in lista if i % 2 == 0]
    return parittomat
a = lista
b = x(lista)
print(a)
print(b)