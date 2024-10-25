def cw1a():
    # skrypt zostanie wykonany pomyślnie
    n =5    # n: 5
    s = 1   # s: 1
    for i in range(1,n+1): # inkrementacja i od 1 do n+1
        s*=i # mnożenie s przez i
    print(s) # wynik końcowy mnożenia w pętli for

def cw1b():
    # skrypt nie zostanie wykonany pomyślnie
    a = 1   # a: 1
    c = 0   # c: 0
    while (a < 3): # pętla będzie się wykonywać dopóki a jest mniejsze od 3, a będzie większe od 3 pętla się zakończy
        for b in range(1, 3):   # inkrementacja b od 1 do 3
            c += a + b + 1 # do c dodajemy wartości a, b oraz 1
    c += 8 # c nie zostanie zwiększone o 8 ponieważ pętla while nie zostanie zakończona
    a += 1 # a nie zostanie zwiększone o 1 ponieważ pętla while nie zostanie zakończona
    print(c) # wartość nie zostanie wyświetlona

def dziel(liczba1,liczba2):
    if liczba2 != 0:
        print(liczba1/liczba2)
    else:
        print('Druga liczba musi być rózna od zera')
def konwert_temp(stopnie):
    print("Domyślnie stopnie są ustawione na C")
    znak = str(input("Wpisz znak stopnia C lub F"))
    if znak == 'F' or znak == 'f':
        stopnie2 = (stopnie - 32) / 1.8
        round(stopnie2,2)
        print(f'Jest {stopnie2} C')
    if znak == '' or znak == 'C' or znak == 'c':
        stopnie2 = stopnie * 1.8 + 32
        round(stopnie2,2)
        print(f'Jest {stopnie2} F')
def liczba_pierwsza(liczba):
    pom = 0
    for i in range(1,101):
        if liczba%i == 0:
            pom += 1
    if pom > 2:
        print("To nie jest liczba pierwsza")
    else:
        print("To jest liczba pierwsza")
def rownanie_kwadratowe(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print('Równanie nie ma rozwiązań')
    else:
        delta = pow(b,2) - 4*a*c
        if delta > 0:
            x1 = (-b+pow(delta,1/2))/2*a
            x2 = (-b-pow(delta,1/2))/2*a
            print(f'Delta jest dodatnai, x1 wynosi {x1}, x2 wynosi {x2}')
        elif delta == 0:
            x_0 = -b/2*a
            print(f'Delta jest równa 0 i wynik x_0 wynosi {x_0} ')
        elif delta < 0:
            print("Brak rozwiązania")

def main():
    # ćw1a
    # cw1a()

    # ćw1b
    # cw1b()

    # ćw2a
    # dziel(5.0,2)
    # dziel(3,0)

    # ćw2b
    # konwert_temp(27)

    # ćw3b
    # liczba_pierwsza(67)

    # ćw4
    # print('Skrypt pobiera trzy liczby całkowite')
    # a = int(input('Pierwsza lcizba'))
    # b = int(input('Druga liczba'))
    # c = int(input('Trzecia liczba'))
    # rownanie_kwadratowe(a,b,c)
main()