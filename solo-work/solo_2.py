class Trojkat:
    def __init__ (self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
# self.obwod = a + b + c + d

def obwod(self):
    return self.a + self.b + self.c

def pole(self):
    return (self.a * self.h_a) /2

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_kamil = Trojkat(14, 6, 7, 11)
# print(trojkat_rownoboczny.obwod())
# print(trojkat_kamil.pole())

class Trapez:
    def __init__ (self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

def obwod(self):
    return self.a + self.b + self.c + self.d

def pole(self):
    return ((self.a + self.b) * self.h) / 2

trapez = Trapez(7, 11, 6, 5, 4)
# print(trapez.obwod())
# print(trapez.pole())

print("--------------------------")

class Student:
    def __init__ (self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__ (self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)


student_kamil = Student("Kamil", "Wrzos", 120153)
student_kamil.dodaj_ocene(4.5)
student_kamil.dodaj_ocene(5)

print(student_kamil.oceny)

class Mieszkanie:
    def __init__(self, cena_za_metr_kwadratowy, metraz, liczba_pokoi, miasto, ulica, pietro, rok_budowy, winda_w_budynku):
        self.cena_za_metr_kwadratowy = cena_za_metr_kwadratowy
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi
        self.miasto = miasto
        self.ulica = ulica
        self.pietro = pietro
        self.rok_budowy = rok_budowy
        self.winda_w_budynku = winda_w_budynku

    def __str__(self):
        return f"Mieszkanie: {self.miasto}, {self.ulica}, {self.pietro}"

    def oblicz_cene(self):
        return self.cena_za_metr_kwadratowy * self.metraz

    def czy_winda(self):
        return "Tak" if self.winda_w_budynku else "Nie"


mieszkanie = Mieszkanie(5000, 70, 3, "Warszawa", "Aleje Jerozolimskie 1", 5, 2005, True)
print(mieszkanie)
print("Cena mieszkania:", mieszkanie.oblicz_cene())
print("Czy jest winda w budynku?", mieszkanie.czy_winda())
