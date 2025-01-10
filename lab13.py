import random

f1 = open('event.txt','r+')
f2 = open('odd.txt','r+')

class Bohater:
    def szczegoly(self,imie,zrecznosc,sila,hp,pt):
        self.imie = imie
        self.zrecznosc = int(zrecznosc)
        self.sila = int(sila)
        self.hp = max(0,min(int(hp),100))
        self.pt = int(pt)

    def leczenie(self,uleczono):
        self.hp = max(0,min(self.hp+int(uleczono),100))

    def dmg(self):
        if self.imie == 'Wojownik' and self.hp < 20 or self.imie == 'Wojownik':
            self.hp = 150
            return self.sila * self.pt * self.hp
        else: return self.zrecznosc * self.pt * self.hp

def main():
    for i in range(100):
        generowana = random.randint(-100,100)
        if generowana % 2 == 0:
            generowana = str(generowana)
            f1.write(generowana)
        else:
            generowana = str(generowana)
            f2.write(generowana)
    f1.close()
    f2.close()

    nazwy = ['odd','event']
    pom = 0
    for i in nazwy:
        f = open(f'{i}.txt','r')
        zawartosc = f.read().split()
        f.close()
        for j in zawartosc:
            pom += int(j)
    print(pom)
main()