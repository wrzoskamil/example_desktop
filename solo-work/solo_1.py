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