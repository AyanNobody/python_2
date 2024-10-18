import math
def rady_na_stopnie(rad,x,pi):
    stopnie = rad*(x/pi)
    return stopnie
def stopnie_na_rady(sto,x,pi):
    rady = sto*(pi/x)
    return rady
def binarne_na_dziesietne(liczba):
    bini = bin(liczba)
    bini = int(bini,2)
    return bini
    # def binary_to_decimal(binary_num):
#     decimal_num = int(binary_num, 2)
#     return decimal_num

# def decimal_to_binary(decimal_num):
#     binary_num = bin(decimal_num).replace("0b", "")
#     return binary_num
# def octal_to_decimal(octal_num):
#     decimal_num = int(octal_num, 8)
#     return decimal_num

# def decimal_to_octal(decimal_num):
#     octal_num = oct(decimal_num).replace("0o", "")
#     return octal_num
# def hexadecimal_to_decimal(hexadecimal_num):
#     decimal_num = int(hexadecimal_num, 16)
#     return decimal_num

# def decimal_to_hexadecimal(decimal_num):
#     hexadecimal_num = hex(decimal_num).replace("0x", "")
#     return hexadecimal_num
# def binary_to_hexadecimal(binary_num):
#     decimal_num = int(binary_num, 2)
#     hexadecimal_num = hex(decimal_num).replace("0x", "")
#     return hexadecimal_num

# def ćw7a(cena):
#     cena2= cena * 0.4
#     cena -= cena2
#     cena2 = cena * 0.4
#     cena += cena2
#     return cena

# def ćw7b(znaczki_polskie,znaczki_zagraniczne):
#     suma_znaczków = znaczki_polskie+znaczki_zagraniczne
#     suma_znaczków /= 2
#     print(f'Panu Jackowi zostało: {suma_znaczków} znaczków')

def ćw7c(skrzynka1,skrzynka2,skrzynka3):
 skrzynka1 *= 15
 skrzynka2 *= 14
 skrzynka3 *= 11
 zaplacil = skrzynka1 + skrzynka2 + skrzynka3
 najtansze = zaplacil/15
 print(f'Właściciel sklepu zapłacił: {zaplacil}, gdyby kupił tylko najtańsze mógł by kupić {najtansze} skrzyń')

def main():
    # suma = 5+5
    # print("Suma ", suma)
    # odejmowanie = 10-5
    # print("odejmowanie ", odejmowanie)
    # mnozenie = 5*3
    # print("Mnozenie ", mnozenie)
    # dzielenie = 10/2
    # print("dzielenie ", dzielenie)
    # modulo = 10 % 2
    # print("Modulo ", modulo)
    # nap1 = "Stefan "
    # nap2 = "Praca"
    # print("Nazywam się", nap1+nap2,sep=':',end='!')
    # x = 10
    # y = 25
    # x+=y
    # print(x)
    # print(0x1a)
    # print(0b101)
    # hex(15)
    # bin(5)

    # ćw2a

   # print("Polskie znaki ęóąśłżźćń")
   # ą=5
   # print(ą)

    # ćw2b
    # czl1 = "Karolina"
    # czl2 = "Wojciech"
    # czl3 = "Jakub"
    # czl4 = "Magda"
    # czl5 = "Ja"
    # print("Członkowie mojej rodziny: ", czl1, czl2, czl3, czl4, czl5)
    # print("Członkowie mojej rodziny: ", czl1, czl2, czl3, czl4, czl5,sep='\n')

    #ćw2c
    # nap1 = "cos ciekawego"
    # nap2 = "cos nieciekawego"
    # print(nap1*nap2)
    # print(nap1-nap2)

    #ćw2d
    # for i in range(101):
    #     print(f'{i}Nie wiem sam')

    #ćw2e
    # a =10
    # b = 5
    # print(a+b)
    # print(pow(a,b))

    #ćw3
     # suma1 = math.sqrt(9+4*math.sqrt(5))
     # suma2 = pow(100-4*math.sqrt(17),1/3)
     # mnozenie1 = (pow(9,-1/4)+pow(3*math.sqrt(3),4/3))*(pow(9,-1/4)-pow(3*math.sqrt(3),4/3))
     # mnozenie2 = (pow(8,-1/6)-pow(2*math.sqrt(2),-5/6)) * (pow(8,-1/6)+1/pow(2*math.sqrt(2),5/6))
     # odejmowanie = math.sqrt(5+2*math.sqrt(6))-1/math.sqrt(5+2*math.sqrt(6))
     # print(suma1,suma2,mnozenie1,mnozenie2,odejmowanie,sep='\n')

    # ćw 4
    # pi = 3.14151926
    # e = 2.718281828
    # dz1 = 25*pi
    # dz2 = pow(pi,2)
    # dz3 = 18*e+pi
    # dz4 = e*(pi+2)
    # dz5 = pow(pi,2)
    # dz6 = math.sqrt(12*e)
    # dz7 = e-pi
    # dz8 = pi/pow(e,2)
    # dz9 = math.sqrt(2)
    # dz10 = math.sqrt(pi)
    # print(dz1,dz2,dz3,dz4,dz5,dz6,dz7,dz8,dz9,dz10,sep='\n')

    # ćw 5
    # pi = 3.14151926
    # x = 180
    # pytanie = int(input('Co chcesz przeliczyć 1 rady na stopnie 2 stopnie na rady: '))
    # if(pytanie==1):
    #     print(rady_na_stopnie((2*pi/3),x,pi))
    # else:
    #     print(stopnie_na_rady(105,x,pi))

    # ćw6
    # print(binarne_na_dziesietne(10))
    ćw7c(5,8,0)
main()