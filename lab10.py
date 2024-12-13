def print_home_numbers(slownik):
    for i in slownik:
        print(i,' ma numer ', slownik.get(i))

def main():
    zbr_set = {'Polska','Niemcy','Litwa','Czechy','Włochy'}
    print(zbr_set)

    zbr_set.add('Polska')
    print(zbr_set)

    if 'Polska' in zbr_set:
        print('Polska jest w zbiorze',sep='\n')
    else: print('Polski nie ma w zbiorze')

    zbr_set.remove('Niemcy')
    print(zbr_set)

    zbior1 = {'Wrocław','Kraków','Warszawa','Nidzica'}
    zbior2 = {'Gdańsk','Warszawa','Kielce','Nidzica'}
    suma_zbr = zbior1.union(zbior2)
    print(suma_zbr,sep='\n')

    czesc_wspl_zbr = zbior1.intersection(zbior2)
    print(czesc_wspl_zbr)

    roznica_zbr1 = zbior2.difference(zbior1)
    roznica_zbr2 = zbior1.difference(zbior2)
    print(roznica_zbr1,sep='\n')
    print(roznica_zbr2,sep='\n')

    # działa poprawnie
    is_subset_operator = zbior1 <= zbior2
    print(is_subset_operator,sep='\n')

    # działa poprawnie
    is_subset_method = zbior1.issubset(zbior2)
    print('Użucie .issubset() ',is_subset_method,sep='\n')

    # nie działa poprawnie
    is_subset_lenght_check = len(zbior1) <= len(zbior2)
    print('Nie prawidłowo działający sprawdzacz podzbioru ',is_subset_lenght_check,sep='\n')

    slownik = {
        'Jakub':1234,
        'Michał':5678,
        'Stefan':9012,
        'Adrian':3456,
        'Random':7890,
    }
    # print(slownik.items())
    # print(slownik.keys())
    # print(slownik.values())
    print_home_numbers(slownik)
main()