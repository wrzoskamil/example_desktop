#zadanie 1.1
hello = "Hello"
student = "Kamil"
wynik = "{}, {}".format(hello,student)
print(wynik)

#zadanie 1.2
student = input("Podaj imię: ")
komunikat = "Hello, {}!".format(student)
print(komunikat)

#zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentów wynosi: ", liczba_studentow)

#zadanie 1.4
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

for student in studenci:
    print("Hello", student)

#zadanie 1.5
liczba = 3
potega = 4
wynik = liczba**potega
print("Wynik wynosi: ", wynik)

#zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == "(":
        liczba_nawiasow_otwierajacych += 1

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

#zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

studenci.sort(key=lambda x: x.split()[0])

print("Alfabetyczna lista studentow wynosi: ", studenci)

#zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

studenci.sort(key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow wynosi: ", studenci)

#zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0

for student in studenci:
    if student.split()[-1].startswith("N"):
        liczba_n += 1

print("Liczba studentow na N wynosi: ", liczba_n)

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

import numpy as np

wynik1 = np.array(wykres_1[1]) - np.array(wykres_1[0])
wynik2 = np.array(wykres_1[2]-np.array(wykres_1[1]))

if wynik1[0] == wynik2[0] and wynik1[1] == wynik2[1]:
    wykres_1_funkcja_liniowa = True

wynik1 = np.array(wykres_2[1]) - np.array(wykres_2[0])
wynik2 = np.array(wykres_2[2]-np.array(wykres_2[1]))

if wynik1[0] == wynik2[0] and wynik1[1] == wynik2[1]:
    wykres_2_funkcja_liniowa = True

wynik1 = np.array(wykres_3[1]) - np.array(wykres_3[0])
wynik2 = np.array(wykres_3[2]-np.array(wykres_3[1]))
wykres_3_funkcja_liniowa = None
if wynik1[0] == wynik2[0] and wynik1[1] == wynik2[1]:
    wykres_3_funkcja_liniowa = True

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")