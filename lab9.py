import math
# def czy_posortowane(lista):
#     pom = 0
#     naj_wieksza = lista[0]
#     for i in range(len(lista)):
#         if lista[0]<lista[i]:
#             return False
#         else:
#             return True

def func1(lista,n1,n2):
    for i in range(len(lista)):
        if lista[i] == n1:
            lista[i] = n2
    return None

def func2(lista,n1,n2):
    nowa_lista = []
    for i in range(len(lista)):
        if lista[i] == n1:
            nowa_lista.append(n2)
        else:
            nowa_lista.append(lista[i])
    return nowa_lista
def func3(lista,n1,n2):
    for i in range(len(lista)):
        if math.isclose(lista[i],n1):
            lista[i] = n2
    return lista
def kalendarz():
    miesiace =[{'1':'Styczen'},{'2':'Luty'},{'3':'Marzec'},
               {'4':'Kwiecień'},{'5':'Maj'},{'6':'Czerwiec'},
               {'7':'Lipiec'},{'8':'Sierpień'},{'9':'Wrzesień'},
               {'10':'Pażdziernik'},{'11':'Listopad'},{'12':'Grudzień'}]

def main():
    lista = [1,2.5,True,'Ala',5,8.5,False,'ma',10]
    # lista[2] = 50

    # print(lista[8])

    # for i in range(len(lista),0,-1):
        # if i%2 == 0:
            # print(i, lista[i])

    # for i in range(4,len(lista)):
        # print(i, lista[i])

    # lista = [1,2,3,4,1]


main()