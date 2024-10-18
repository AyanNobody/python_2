def cw1a():
    pom = 0
    for i in range(2,101):
         if i%2==0:
             pom += i
    return pom
def cw1b():
    parzyste = 0
    nieparzyste = 0
    for i in range(5):
        liczba = int(input("Podaj liczbę: "))
        if liczba%2==0:
            parzyste += 1
        else:
            nieparzyste += 1
    print(f'Jest {parzyste} liczb parzystych oraz {nieparzyste} nieparzystych')
def cw1c():
    pom = 0
    for i in range(1,101):
        pom += pow(i,2)
    print(f'Suma kwadratów liczb od 1 do 100, wynosi: {pom}')
def cw1d():
    pom = 0
    for i in range(1,64):
        pom += pow(2,i)
    print(pom)
def cw1e():
    print("Program wczytuję dwie wartości")
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    pom = 0
    if a > b:
        return 0
    else:
        for i in range(a,b+1):
           if i%2!=0:
            pom += i
    return pom
def cw1f():
    liczba = int(input("Podaj liczbę, żeby narysować piramidę "))
    for i in range(1,liczba+1):
        for j in range(1,i+1):
           print(j,end=" ")
    print()

def cw1g():
    n = int(input("Proszę podać liczbę: "))
    pom = 0
    for i in range(1,n+1):
        pom += i
    print(pom)
def cw1h():
    n = int(input("Proszę podać liczbę: "))
    for i in range(1,n+1):
        liczba = int(input(f'Proszę podać {i} liczbę: '))
        if liczba%3 == 0:
            print(f'{liczba} jest podzielna przez 3')
        if liczba%5!=0:
            print(f'{liczba} nie jest podzielna przez 5')
def cw2a():
    i = 0
    while True:
        znak = str(input("Proszę wprowadzić znak: "))
        if znak == 'x':
            break
        else:
            i += 1
    return i
def cw2c():
    a = int(input("Proszę wpisać pierwszą liczbę: "))
    b = int(input("Proszę wpisać drugą liczbę: "))
    c = int(input("Proszę wpisać trzecią liczbę: "))
    while a < 0 or b < 0 or c < 0:
        pom = int(input("Proszę zamienić ujemną na dodatnią"))
def main():
    # ćw1a
    # print(cw1a())

    # ćw1b
    # print("Program pobiera pięc liczb całkowitych")
    # cw1b()

    # ćw1c
    # cw1c()

    # ćw1d
    # cw1d()

    # ćw1e
    # print(cw1e())

    # ćw1f
    # cw1f()

    # ćw1g
    # cw1g()

    # ćw1h
    # cw1h()

    # ćw2a
    # print(cw2a())

    # ćw2b

main()