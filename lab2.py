def main():
    # ćw1
    # imie = str(input("Jak się nazywasz?"))
    # print(f'Hello world,{imie}!')

    # ćw2
    # VAR1 = 2
    # VAR2 = 3
    # VAR1 += 2
    # VAR3 = VAR1
    # VAR *= 3
    # VAR4 = VAR1/VAR2

    # ćw3a
    # age = int(input("Wprowadz swój wiek"))
    # if 18<= age <=100:
    #     print("Autoryzacja uzyskana")
    # else: print("Odmowa")

    # ćw3b
    # a = int(input("Wprowadź liczbę: "))
    # if a >0:
    #     print("|a|= ", a)
    # if a <0:
    #     print("|a|= ",-a)

    # ćw3c
    # a = 10
    # b = 50
    # if a > b:
    #     print("Hello World")
    # else:
    #     print("Bye World")

    # ćw3d
    # liczba = int(input("Podaj liczbę: "))
    # if(liczba%2 == 0):
    #     print(f'Liczba {liczba} jest parzysta')
    # else:
    #     print(f'Liczba {liczba} jest nieparzysta')

    # ćw3e
    # liczba1 = float(input("Podaj liczbę1 zmiennoprzecinkową: "))
    # liczba2 = float(input("Podaj liczbę2 zmiennoprzecinkową: "))
    # if liczba1>liczba2:
    #     print(liczba1)
    # else:
    #     print(liczba2)

    # ćw3f
    # przedzial1 = []
    # przedzial2 = []
    # liczba = int(input("Podaj liczbę całkowitą: "))
    # for i in range(1,11):
    #     przedzial1.append(i)
    #     if liczba in przedzial1:
    #         print(f'{liczba} znajduję się w przedziale 1 ')
    #         break
    # for j in range(17,22):
    #     przedzial2.append(j)
    #     if liczba in przedzial2:
    #         print(f'{liczba} znajduję się w przedziale 2')
    #         break

    # ćw3g
    # liczba = int(input("Podaj liczbę: "))
    # if liczba%3 == 0 and liczba%5 == 0:
    #     print(f'{liczba} jest podzielna przez 3 i 5')
    # if liczba%3 == 0 and liczba%5 != 0:
    #     print(f'{liczba} jest podzielna przez 3, ale nie przez 5')
    # if liczba%3 != 0 and liczba%5 != 0:
    #     print(f'{liczba} nie jest podzielna przez 3 i 5')

    # ćw3h
    # print('Mały kalkulator, pobieram dwie liczby całkowite oraz znaki "+ - * /"')
    # liczba1 = int(input("Podaj liczbę1: "))
    # liczba2 = int(input("Podaj liczbę2: "))
    # znak = str(input("Podaj znak: "))
    # if znak == "+":
    #     print(liczba1+liczba2)
    # if znak == "-":
    #     print(liczba1-liczba2)
    # if znak == "*":
    #     print(liczba1*liczba2)
    # if znak == "/":
    #     print(liczba1/liczba2)
    # if znak == "":
    #     print("Zamykanie kalkulatora")

    # ćw3i
    # print("Zamieniam stopnie Celcjusza na Farenhaita lub odwrotnie")
    # print("Jeśli nie zostanie podany żaden znak konwenter się wyłączy")
    # stopnie = float(input("Podaj ile jest stopni: "))
    # znak = str(input("Podaj znak: "))
    # if znak == 'C' or znak == 'c':
    #     stopnie2 = stopnie*1.8 + 32
    #     print(f'Jest {stopnie2} F')
    # if znak == 'f' or znak == 'F':
    #     stopnie2 = (stopnie-32)/1.8
    #     print(f'Jest {stopnie2} C')
    # if znak == "":
    #     print("Zamykanie konwentera")

    # ćw3j
    liczba1 = pow(int(input("Podaj liczbę1: ")), 2)
    liczba2 = pow(int(input("Podaj liczbę2: ")), 2)
    liczba3 = pow(int(input("Podaj liczbę3: ")), 2)
    if liczba1 > liczba2 and liczba1 > liczba3:
        pomoc = liczba2 + liczba3
        if pomoc == liczba1:
            print("Liczby stanowią trójkę pitagorejską")
        else:
            print("To nie jest trójka pitagorejska")
    if liczba2 > liczba1 and liczba2 > liczba3:
        pomoc = liczba1 + liczba3
        if pomoc == liczba2:
            print("Liczby stanowią trójkę pitagorejską")
        else:
            print("To nie jest trójka pitagorejska")
    if liczba3 > liczba1 and liczba3 > liczba2:
        pomoc = liczba1 + liczba2
        if pomoc == liczba3:
            print("Liczby stanowią trójkę pitagorejską")
        else:
            print("To nie jest trójka pitagorejska")
main()
