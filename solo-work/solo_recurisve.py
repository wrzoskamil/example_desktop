# funkcja sum_list(l) zwraca sumę wszystkich elementów 
# jeżeli l puste zwróc 0
# jeżeli l niepuste dodaj pierwszy element listy do sumy reszty listy

def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_list(l[1:])

# przykład użycia:
list = [1, 2, 3, 4, 5, 6, 7]
result = sum_list(list)
print(result)    
# result = 28


# funkcja find_max(l) zwraca największy element w liście l
# jeżeli l puste zwróć None
# jeżeli l niepuste rekurencyjnie znajdź największy element reszty listy i porównuj go z pierwszym elementem

def find_max(l):
    if not l:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        max_rest = find_max(l[1:])
        if l[0] > max_rest:
            return l[0]
        else:
            return max_rest

# przykład użycia:
list = [6, 1, 9, 11, 3]
result = find_max(list)
print(result)  
# result = 11


# funkcja silnia(n) zwraca silnię liczby n
# jeżeli n = 0 lub n = 1, zwróć 1
# w innym wypadku, rekurencyjnie oblicz silnię mnożąc n przez silnia(n-1)

def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

# przykład użycia:
liczba = 7
result = silnia(liczba)
print(result)   
# result = 5040


# funkcja fibonacci(n) zwraca n-ty element ciągu Fibonacciego
# jeżeli n = 0, zwróć 0.
# jeżeli n = 1 lub n = 2, zwróć 1.
# w innym wypadku rekurencyjnie oblicz n-ty element sumując dwa poprzednie elementy

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# przykład użycia:
liczba = 6
result = fibonacci(liczba)
print(result)  
# result = 8


