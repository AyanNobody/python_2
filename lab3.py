import random
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
    koniec = 0
    liczby = []
    while koniec !=3:
        koniec += 1
        try:
            liczba = int(input("Prowaź liczbę "))
            if liczba < 0 :
                print("Liczba ujemna proszę spróbować ponownie.")
                koniec -= 1
            else:
                liczby.append(liczba)
        except ValueError:
            print("To nie jest liczba całkowita! Spróbuj ponownie")
            koniec -= 1
    if 0 in liczby:
        print("Wprowadzono zero.")
    else:
        print("Nie wprowadzono zera")
    for i in range(len(liczby)):
        print(liczby[i], end=" ")
def cw2d():
    a = random.randint(1,101)
    print("Gra, zgadnij liczbę zakres od 1 do 100")
    b = int(input("Podaj liczbę: "))
    if b==a:
        print("Brawo zgadłeś!")
    else:
        print(f'Niestety nie, zgadywaną liczbą było {a}')
def cw2e():
    print("Uwaga! Wartość m musi być większa od 2")
    m = int(input("Proszę wprowadzić wartość m"))
    if m <= 2 :
        print("M musi być większe od 2")
    else:
        potega = 0
        while True:
            potegowanie = pow(3,potega)
            print(f'Liczba z potęgowania: {potegowanie}')
            if potegowanie > m:
                print(f'{potegowanie} jest większe od {m}')
                break
            potega += 1
def cw2f():
    print("Program wczytuje liczbę z klawiatury z przedziału 1-12, jak przedział z miesiąca")
    print("Uwaga dostępne są tylko trzy próby")
    proba = 0
    while proba != 3:
        liczba = int(input("Proszę wprowadzić liczbę: "))
        if liczba > 12 or liczba < 1:
            proba += 1
            print("liczba nie jest w przedziale")
        else:
            print(f'{liczba} jest w przedziale 1-12')
            break
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

    # ćw2c
    # cw2c()

    # ćw2d
    # cw2d()

    # ćw2e
    # cw2e()

    # ćw2f
    # cw2f()
main()
