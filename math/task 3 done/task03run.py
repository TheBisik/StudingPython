import math

while 1:
    try:
        liczba1 = int(input('Liczba 1: '))
        break
    except ValueError:
        print("""
        Blad, podaj liczbę
        """)



while 1:
    try:
        liczba2 = int(input('Liczba 2: '))
        break
    except ValueError:
        print("""
        Blad, podaj liczbę
        """)


suma = liczba1 +  liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2
iloraz = liczba1 / liczba2
pierwiastek = math.sqrt(suma)
potenga_ab = pow(liczba1, liczba2)
potenga_ba = pow(liczba2, liczba1)

print('Suma liczb', liczba1, liczba2, 'to', suma)
print('Różnica liczb', liczba1, liczba2, 'to', roznica)
print('Iloczyn liczb', liczba1, liczba2, 'to', iloczyn)
print('Iloraz liczb', liczba1, liczba2, 'to', iloraz)
print('Pierwiastek liczb √(', liczba1,'+', liczba2, ') to', pierwiastek)
print('Potenga ', liczba1, '^', liczba2, ' to ', potenga_ab)
print('Potenga ', liczba2, '^', liczba1, ' to ', potenga_ba)