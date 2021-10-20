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



def main():
    lst = []
    while True:
        print("1.Citire lista cu un numar dat de elemente")
        print("a.Afisare lista")
        print("x.Exit")
        optiune = input("Alegeti optiunea: ")
        if optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        elif optiune == "1":
            lst = citire_lista()
        else:
            print("Optiune inexistenta! Reincercati!")


main()