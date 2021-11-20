import datetime

#pobieranie daty
rok = datetime.datetime.now()
rok = (rok.year)

#imie

imie = input('Twoje imie: ')

# urodzenie

while 1:
    try:
        urodziny = int(input('Podaj rok urodzneia: '))
        break
    except ValueError:
        print("""
        Blad, podaj liczbę
        """)

wiek = rok - urodziny

print('Nazywasz sie:', imie, " ", 'Masz:', wiek, 'lat')