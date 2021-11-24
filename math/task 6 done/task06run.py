import random

ilerazy = 0

while 1:
    losowa = random.randint(1, 10)
    while 1:
        try:
            gracza = int(input('Podaj liczbe: '))
            if gracza <= 10 and gracza >= 0:
                break
            else:
                print('Wpisz liczbę z zakresu od 1 do 10!')
        except ValueError:
            print('Wpisz LICZBE z zakresu od 1 do 10!')
    if losowa == gracza:
        break
    else:
        print('Nie udało ci się zgadnąć!')
        ilerazy = ilerazy + 1
        if losowa >= gracza:
            print('Twoja liczba była mniejsza od losowanej')
        elif losowa <= gracza:
            print('Twoja liczba była większa od losowanej')

print('Brawo udało ci się zgadnąć za', ilerazy, 'razem, gratulacje!')