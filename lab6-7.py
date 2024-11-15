def pascal(n):
    tab = []
    for i in range(0,n):
        pom = []
        for j in range(0,i+1):
            if j==0 or j == i:
                pom.append(1)
            else:
                pom.append(tab[i-1][j-1]+tab[i-1][j])
        tab.append(pom)
    return tab

def pierwsza(liczba):
    for i in range(1,liczba):
        if liczba % i == 0:
            return 1
        return 0
def blizniacze(n=1000):
    for x in range(1,n,2):
        if pierwsza(x) and pierwsza(x+2):
            print(x,x+2)

def catalan(n=1000000):
    par = 0
    npar = 0
    pom = 0
    for i in range(0,n):
        if i < n:
            if i == 0:
                print(1)
            else:
                pom = ((4*n+2)/n+1)*(i)
                print(int(pom))
        if pom % 2 == 0:
            par += 1
        else: npar += 1
        print(f'Liczb parzystych: {par}, nieparzystych: {npar}')
def doskonale(liczba):
    pom = 0
    zapisac = 0
    for i in range(1,liczba):
        if liczba % i == 0:
            zapisac = i
        pom += zapisac
    if pom == liczba:
        print(f'{liczba} jest liczbą doskonałą')
    else:
        print(f'{liczba} nie jest liczbą doskonałą')
def main():
    # pascal
    # n = 5
    # pom2 = pascal(n)
    # for i in range(len(pom2)):
    #     for j in range(len(pom2[i])):
    #         print(pom2[i][j],end=' ')
    #     print()

    # bliżniacze
    # blizniacze()

    # catalan
    # print(catalan())

    # doskonała
    doskonale(6)
main()
