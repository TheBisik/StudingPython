import math

print("Rownanie ax^2 + bx + c = 0")

#dla a
while 1:
    try:
        a = float(input('Wartosc a: '))
        break
    except ValueError:
        print("""
        Wartosc musi byc liczba!
        """)

#dla b

while 1:
    try:
        b = float(input('Wartosc b: '))
        break
    except ValueError:
        print("""
        Wartosc musi byc liczba!
        """)

#dla c
while 1:
    try:
        c = float(input('Wartosc c: '))
        break
    except ValueError:
        print("""
        Wartosc musi byc liczba!
        """)

delta = pow(b, 2) - 4 * a * c


if delta == 0:
    #dla delta = 0
    wynikdelta0 = -b / (2 * a)
    print(""" Wynik działania
     
     x = -b / 2*a
     
     """,wynikdelta0)
elif delta >= 0:
    # dla x1

    wynix1 = (-b + math.sqrt(delta)) / 2 * a
    wynix1 = round(wynix1, 2)
    print(""" Wynik działania 
    
    x1 = -b + √Δ / 2 * a
    
    """, wynix1)

    # dla x2

    wynix2 = (-b - math.sqrt(delta)) / 2 * a
    wynix2 = round(wynix2, 2)
    print(""" Wynik działania 

    x1 = -b - √Δ / 2 * a

    """, wynix2)
else:
    quit(print('równanie sprzeczne, nie ma rozwiązania'))






