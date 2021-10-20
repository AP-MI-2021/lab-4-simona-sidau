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


def main():
    lst = []
    test_gaseste_numar_pozitie()
    while True:
        print("1.Citire lista cu un numar dat de elemente")
        print("2.Afisare daca un numar se gaseste in lista de la o pozitie data")
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
        else:
            print("Optiune inexistenta! Reincercati!")


main()