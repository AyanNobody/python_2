import random

class Bohater:
    def __init__(self,imie,hp,p_t):
        self.imie = imie
        self.hp = hp
        self.p_t = p_t

    def zmiana_punktow_hp(self,ilosc):
        if 0 <= self.hp + ilosc <=100:
            self.hp += ilosc
            print(f'{self.imie} posiada {self.hp}% życia')
        else:
            print('Żywotność musi być w zakresie 0% - 100%.')

class Lucznik(Bohater):
    def __init__(self,imie, hp, zrecznosc, p_t):
        super().__init__(imie,hp,p_t)
        self.zrecznosc = zrecznosc
    def sila_ataku(self):
        return self.zrecznosc * self.p_t * (self.hp/100)

class Wojownik(Bohater):
    def __init__(self,imie,hp,sila,p_t):
        super().__init__(imie,hp,p_t)
        self.sila = sila
    def sila_ataku(self):
        if self.hp <20:
            return self.sila*self.p_t*1.5
        return self.sila* self.p_t* (self.hp/100)

def main():
    # lucznik = Lucznik('Legolas',100,15,5)
    # wojownik = Wojownik('Thor',100,20,3)
    # print(f'Moc ataku łucznika {lucznik.imie}: {lucznik.sila_ataku()}')
    # print(f'Moc ataku wojownika {wojownik.imie}: {wojownik.sila_ataku()}')
    #
    # wojownik.zmiana_punktow_hp(-30)
    # lucznik.zmiana_punktow_hp(-50)
    # print(f'Moc ataku lucznika {lucznik.imie} po zmianie zdrowia: {lucznik.sila_ataku()}')
    # print(f'Moc ataku wojownika {wojownik.imie} po zmianie zdrowia: {wojownik.sila_ataku()}')

    with open('evem.txt','w') as f1, open('odd.txt','w') as f2:
        for i in range(100):
            generowana = random.randint(-100,100)
            if generowana % 2 == 0:
                f1.write(f'{generowana}\n')
            else: f2.write(f'{generowana}\n')

    for nazwa_pliku in ['evem.txt','odd.txt']:
        with open(nazwa_pliku,'r') as f:
            zawartosc = f.readlines()
            liczby = [int(linia.strip()) for linia in zawartosc]
            suma = sum(liczby)
            srednia = suma / len(liczby) if liczby else 0
            print(f'Plik: {nazwa_pliku}, Suma: {suma}, Średnia: {srednia}')

main()
