from collections import Counter
def citire_lista():
    """
    Citeste o lista de numere intregi cu n elemente
    :param lst:
    :return:
    """
    lst=[]
    n = int(input("Introduceti numarul de elemente: "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst


def gaseste_numar_pozitie(lst, numar, pozitie):
    """
    Verifica daca un numar data se afla in lista dupa o anumita pozitie
    :param lst: lista de numere intregi
    :param numar: numar intreg
    :param pozitie: numar natural
    :return: 1 daca numarul dat se regaseste in lista dupa pozitia data, 0 in caz contrar
    """
    gasit = 0
    for i in range (pozitie, len(lst)):
        if lst[i] == numar:
            gasit = 1
    return gasit


def test_gaseste_numar_pozitie():
    assert gaseste_numar_pozitie([87, 92, 45, 6], 3, 1) == 0
    assert gaseste_numar_pozitie([12, 45, 16, 72, 45], 45, 1) == 1
    assert gaseste_numar_pozitie([17, 19, 63, 45, 21], 21, 3) == 1


def suma_numere_pare(lst):
    """
    Calculeaza suma elementelor pare dintr-o lista
    :param lst: lista numere intregi
    :return: suma elementelor pare
    """
    suma = 0
    for x in lst:
        if x % 2 == 0:
            suma += x
    return suma


def test_suma_numere_pare():
    assert suma_numere_pare([12, 7, 4]) == 16
    assert suma_numere_pare([3, 7, 5]) == 0
    assert suma_numere_pare([12, 4, 6]) == 22


def lst_numere_pare(lst):
    """
    Determina elementele pare dintr-o lista
    :param lst: lista numere intregi
    :return: elementele pare din lista
    """
    rezultat = []
    for x in lst:
        if x % 2 == 0 and rezultat.count(x) == 0:
            rezultat.append(x)
    return rezultat


def test_lst_numere_pare():
    assert lst_numere_pare([12, 5, 18, 92, 12]) == [12, 18, 92]
    assert lst_numere_pare([13, 15, 17, 5]) == []
    assert lst_numere_pare([12, 14, 18, 20, 14]) == [12, 14, 18, 20]


def inlocuire_numar_cu_tuplu_suma(lst):
    """
    Inlocuieste fiecare număr cu un tuplu format din două numere de pe
    poziții distincte din listă care adunate dau acel număr, daca este posibil
    :param lst: lista numere intregi
    :return: lista obtinuta in urma inlocuirilor
    """
    rezultat =[]
    for x in range(len(lst)):
        gasit = 0
        for i in range (0, len(lst)):
            for j in range (i+1, len(lst)):
                if lst[i] + lst[j] == lst[x]:
                    if x is not i and i is not j and x is not j:
                        tuplu = (lst[i], lst[j])
                        gasit = 1
        if gasit:
            rezultat.append(tuplu)
        else:
            rezultat.append(lst[x])
    return rezultat


def test_inlocuire_numar_cu_tuplu_suma():
    assert inlocuire_numar_cu_tuplu_suma([4, 8, 6, 3, 2, 1]) == [(3,1), (6, 2), (4,2), (2,1), 2, 1]
    assert inlocuire_numar_cu_tuplu_suma([2, 4, 5, 6, 1, 9]) == [2, 4, (4,1), (5,1), 1, (4,5)]
    assert inlocuire_numar_cu_tuplu_suma([7, 10, 15, 96]) == [7, 10, 15, 96]


def main():
    lst = []
    test_gaseste_numar_pozitie()
    test_suma_numere_pare()
    test_lst_numere_pare()
    test_inlocuire_numar_cu_tuplu_suma()
    while True:
        print("1.Citire lista cu un numar dat de elemente")
        print("2.Afisare daca un numar se gaseste in lista de la o pozitie data")
        print("3.Afisare suma numere pare")
        print("4.Afisare numere pare din lista")
        print("5.Exercitiul 5")
        print("a.Afisare lista")
        print("x.Exit")
        optiune = input("Alegeti optiunea: ")
        if optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        elif optiune == "1":
            lst = citire_lista()
        elif optiune =="2":
            numar = int(input("Introduceti numarul: "))
            pozitie = int(input("Introduceti pozitia: "))
            ok = gaseste_numar_pozitie(lst, numar, pozitie)
            if ok:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            afisare = suma_numere_pare(lst)
            print(afisare)
        elif optiune == "4":
            afisare = lst_numere_pare(lst)
            print(afisare)
        elif optiune == "5":
            afisare = inlocuire_numar_cu_tuplu_suma(lst)
            print(afisare)
        else:
            print("Optiune inexistenta! Reincercati!")


main()