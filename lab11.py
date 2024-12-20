class Account:
    def __init__(self, saldo,
                 przelew_miedzy_kontami,
                 przelew_zewnetrzny,
                 wplata,wyplata):
        self.saldo = saldo
        self.przelew_kont = przelew_miedzy_kontami
        self.przelew_zew = przelew_zewnetrzny
        self.wplata = wplata
        self.wyplata = wyplata
    def wyswietl_saldo(self):
        print(self.saldo)
    def wplata_wyplata(self,ilosc):
        if self.wplata > 0:
            self.saldo += ilosc
            self.wyswietl_saldo()
    def wyplata_z_konta(self,ilosc):
        if self.wyplata > 0:
            self.saldo -= ilosc
            self.wyswietl_saldo()
    def przelew_zewnetrzny(self,ilosc):
        if 0<ilosc<self.saldo:
            self.saldo -= ilosc
            print(f'Przelew na {ilosc} PLN, został pomyślnie dokonany')
        else:
            print(f'Przelew na {ilosc} nie został dokonany')
        self.wyswietl_saldo()
class PrivateAccount(Account):
    def przelew_wynagrodzenia(self,wynagrodzenie):
        if wynagrodzenie > 0:
            self.saldo += wynagrodzenie
            self.wyswietl_saldo()

class FirmAccount(Account):
class Vector:
def main():

main()