import math

liczbapi = math.pi



while 1:
    try:
        promienkola = float(input('Podaj promien kola w cm: '))
        break
    except ValueError:
        print("""
        Wartośc musi być liczba! Sproboj ponownie...
        """)
if promienkola == 0 or promienkola <= 0:
    print('Wartosc musi byc wieksza od zera! Sproboj ponownie uruchamiajac program kolejny raz!')
    quit()


#pole
wynikpole = round(liczbapi * pow(promienkola, 2),2)
print('Pole kola rowna sie: ', wynikpole)

#obowod

wynikoobwod = round(2*(liczbapi * promienkola), 2)
print('Obowd kola rowna sie: ', wynikoobwod)


