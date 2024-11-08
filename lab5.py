def gmean(*args):
    s = 0
    for i in range(0,len(args)):
        s += args[i]
    s = s/len(args)
    return s
def func1(*args):
    for i in range(0,len(args)):
        for j in range(0,i+1):
            print(args[j],end=' ')
        print(' ')
def func2(*args):
    for i in range(0,len(args)):
        for j in range(0,i+1):
            print(args[i],end=' ')
        print(' ')
def my_max_2(a,b):
    if b<a:
        return a
    elif a<b:
        return b
    elif a == b:
        return "Liczby są takie same"
def my_max_3(a,b,c):
    if a<b and c<b:
        return b
    elif b<a and c<a:
        return a
    elif a<c and b<c:
        return c
    elif a == b and a == c:
        return "Liczby są takie same"
# def my_max_nies(*args):
def rekurencja(liczba):
    return liczba * rekurencja(liczba-1)
def algorytm_euklidesa(a,b):
    while a != b:
        if a < b:
            b - a
        elif b < a:
            a - b
    return f'Największym wspólnym dzielnikiem jest {a}'
def main():
    # ćw 1a
    # print(gmean(2,5,10))
    # ćw 1b
    # func1(3,'Ala',5)
    # ćw 1c
    # func2(3,'Ala',5)
    # ćw 2a
    # print(my_max_2(5,5))
    # ćw 2b
    # print(my_max_3(10,10,10))
    # ćw 3a
    # print(rekurencja(6))
    # ćw 4a
    algorytm_euklidesa(1989,867)
main()