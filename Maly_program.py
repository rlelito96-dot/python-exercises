
def main():

    print()
    print("Welcome on my MINI PROGRAM!!!")

    zadania = []

    while True:


        print()
        print("1.Pokaż zadania")
        print("2.Dodaj zadanie")
        print("3.Usuń zadanie")
        print("4.Zapisz")
        print("5.Wyjdź")


        try:
            wybor_uzytkownika = int(input("Wybierz numer akcji 1-5: ".strip()))
            print()
            if wybor_uzytkownika not in [1, 2, 3, 4, 5]:
                print("Niepoprawny kod!Spróbuj ponownie..")
        except ValueError:
            continue


        def dodaj_zadanie():
            nowe_zadanie = input("Wpisz treść nowego zadania: ").strip()
            zadania.append(nowe_zadanie)
            print("Zadanie zostało dodane!")


        if wybor_uzytkownika == 5:
            print("Do zobaczenia!")
            break

        if wybor_uzytkownika == 1:
            print(zadania)
        elif wybor_uzytkownika == 2:
            dodaj_zadanie()
        elif wybor_uzytkownika == 3:
            usun_zadanie = int(input("Wybierz zadanie do usunięcia: "))
            zadania.pop(usun_zadanie)
            print("Zadanie zostało usunietę!")
        elif wybor_uzytkownika == 4:
            with open("zadania.txt", "w+") as f:
                for zadanie in zadania:
                    f.write(zadanie +"\n")
            print("Plik został zapisany!")



if __name__ == "__main__":
    main()













