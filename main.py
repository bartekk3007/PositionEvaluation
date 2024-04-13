import random
import time

start = time.time()

N = 3
x = 'X'
o = 'O'
xi = 'Ξ'
omega = 'Ω'

def printArray(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            print(tab[i][j], end=' ')
        print()
    print()


def createArray(rozmiar):
    return [['-' for i in range(rozmiar)] for j in range(rozmiar)]


def addSign(tab, sign, wiersz, kolumna):
    tab[wiersz][kolumna] = sign


def checkWin(tab):
    wynik = 0

    for i in range(0, len(tab)):
        pocz = 0
        for j in range(0, len(tab[0])):
            if tab[i][j] == o:
                pocz = pocz + 1
        if pocz == len(tab[0]):
            wynik = -1

    for j in range(0, len(tab[0])):
        pocz = 0
        for i in range(0, len(tab)):
            if tab[i][j] == o:
                pocz = pocz + 1
        if pocz == len(tab[0]):
            wynik = -1

    pocz = 0
    for k in range(0, len(tab)):
        if tab[k][k] == o:
            pocz = pocz + 1
    if pocz == len(tab):
        wynik = -1

    pocz = 0
    for k in range(0, len(tab)):
        if tab[k][len(tab) - 1 - k] == o:
            pocz = pocz + 1
    if pocz == len(tab):
        wynik = -1

    for i in range(0, len(tab)):
        pocz = 0
        for j in range(0, len(tab[0])):
            if tab[i][j] == x:
                pocz = pocz + 1
        if pocz == len(tab[0]):
            wynik = 1

    for j in range(0, len(tab[0])):
        pocz = 0
        for i in range(0, len(tab)):
            if tab[i][j] == x:
                pocz = pocz + 1
        if pocz == len(tab[0]):
            wynik = 1

    pocz = 0
    for k in range(0, len(tab)):
        if tab[k][k] == x:
            pocz = pocz + 1
    if pocz == len(tab):
        wynik = 1

    pocz = 0
    for k in range(0, len(tab)):
        if tab[k][len(tab) - 1 - k] == x:
            pocz = pocz + 1
    if pocz == len(tab):
        wynik = 1

    return wynik


def printWinner(tab):
    if checkWin(tab) == -1:
        print("Wygrał gracz O\n")
    elif checkWin(tab) == 1:
        print("Wygrał gracz X\n")
    else:
        print("Jest remis\n")


def returnSign(n):
    if n % 2 == 0:
        return x
    else:
        return o


def returnSpecial(n):
    if n % 2 == 0:
        return xi
    else:
        return omega


def readPosition(n):
    tab = [['-' for i in range(n)] for j in range(n)]
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            tab[i][j] = input("Wpisz liczbe z {0} kolumny i {1} wiersza\n".format(i, j))
    return tab


def readFromFile(n):
    tab = [['-' for i in range(n)] for j in range(n)]
    f = open("plansza.txt", "r")
    for i in range(0, len(tab)):
        wynikLine = f.readline()
        for j in range(0, len(tab[0])):
            tab[i][j] = wynikLine[2 * j]
    return tab


def freeSpaces(tab):
    licznik = 0
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j] == '-':
                licznik += 1
    return licznik


def fillOnePlace(tab):
    wyniki = []
    n = freeSpaces(tab)
    s = returnSign(n+1)
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j] == '-':
                newtab = [['*' for x in range(len(tab))] for y in range(len(tab))]
                for m in range(0, len(tab)):
                    for n in range(0, len(tab[0])):
                        if m == i and n == j:
                            newtab[m][n] = s
                        else:
                            newtab[m][n] = tab[m][n]
                wyniki.append(newtab)
    return wyniki


def fillOneSpecial(tab):
    wyniki = []
    n = freeSpaces(tab)
    s = returnSpecial(n+1)
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j] == '-':
                newtab = [['*' for x in range(len(tab))] for y in range(len(tab))]
                for m in range(0, len(tab)):
                    for n in range(0, len(tab[0])):
                        if m == i and n == j:
                            newtab[m][n] = s
                        else:
                            newtab[m][n] = tab[m][n]
                wyniki.append(newtab)
    return wyniki


def printMultipleArrays(tab):
    for i in range(len(tab)):
        printArray(tab[i])


def minimax(tab):
    if freeSpaces(tab) == 0:
        return checkWin(tab)

    elif freeSpaces(tab)%2 == 1 and checkWin(tab) != 0:
        maksimum = -1000000
        # uwaga moze byc zle tab
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            eval = minimax(res[i])
            maksimum = max(maksimum, eval)
        return maksimum

    elif freeSpaces(tab)%2 == 0 and checkWin(tab) != 0:
        minimum = 1000000
        # uwaga moze byc zle tab
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            eval = minimax(res[i])
            minimum = min(minimum, eval)
        return minimum

    elif freeSpaces(tab)%2 == 1:
        maksimum = -1000000
        # uwaga moze byc zle tab
        res = fillOnePlace(tab)
        for i in range(len(res)):
            eval = minimax(res[i])
            maksimum = max(maksimum, eval)
        return maksimum

    elif freeSpaces(tab)%2 == 0:
        minimum = 1000000
        # uwaga moze byc zle tab
        res = fillOnePlace(tab)
        for i in range(len(res)):
            eval = minimax(res[i])
            minimum = min(minimum, eval)
        return minimum


def allNodes(tab, tabela):
    if tabela == None:
        tabela = []

    if freeSpaces(tab) == 0:
        tabela.append(tab)

    elif freeSpaces(tab)%2 == 1 and checkWin(tab) != 0:
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            allNodes(res[i], tabela)

    elif freeSpaces(tab)%2 == 0 and checkWin(tab) != 0:
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            allNodes(res[i], tabela)

    elif freeSpaces(tab)%2 == 1:
        res = fillOnePlace(tab)
        for i in range(len(res)):
            allNodes(res[i], tabela)

    elif freeSpaces(tab)%2 == 0:
        res = fillOnePlace(tab)
        for i in range(len(res)):
            allNodes(res[i], tabela)

    return tabela


def allResults(tab, tabela):
    if tabela == None:
        tabela = []

    if freeSpaces(tab) == 0:
        tabela.append(checkWin(tab))

    elif freeSpaces(tab)%2 == 1 and checkWin(tab) != 0:
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            allResults(res[i], tabela)

    elif freeSpaces(tab)%2 == 0 and checkWin(tab) != 0:
        res = fillOneSpecial(tab)
        for i in range(len(res)):
            allResults(res[i], tabela)

    elif freeSpaces(tab)%2 == 1:
        res = fillOnePlace(tab)
        for i in range(len(res)):
            allResults(res[i], tabela)

    elif freeSpaces(tab)%2 == 0:
        res = fillOnePlace(tab)
        for i in range(len(res)):
            allResults(res[i], tabela)

    return tabela


def returnEvaluation(tab):
    wynik = minimax(tab)
    wartosciWezlow = allResults(tab, [])
    wynik += sum(wartosciWezlow)/len(wartosciWezlow)
    wynik /= 2
    return round(wynik, 2)


def returnSecondEvaluation(tab):
    wynik = minimax(tab)
    wartosciWezlow = allResults(tab, [])
    dlugosc = 0
    for i in range(len(wartosciWezlow)):
        if wartosciWezlow[i] != 0:
            dlugosc += 1
    wynik += sum(wartosciWezlow)/dlugosc
    wynik /= 2
    return round(wynik, 2)

'''
tabela = createArray(N)
printArray(tabela)
addSign(tabela, x, 2, 2)
addSign(tabela, x, 1, 1)
addSign(tabela, x, 0, 0)
printArray(tabela)
printWinner(tabela)
'''

'''
tabelaRand = createArray(N)
number_list = list(range(N * N))
iter = 0
while checkWin(tabelaRand) == 0 and iter < N * N:
    liczba = random.choice(number_list)
    addSign(tabelaRand, returnSign(iter), liczba // N, liczba % N)
    number_list.remove(liczba)
    iter += 1
    printArray(tabelaRand)

printWinner(tabelaRand)
'''


'''
wynikFile = readFromFile(N)
printArray(wynikFile)
printWinner(wynikFile)
print(freeSpaces(wynikFile))
print()
print("Wyniki to\n")
printMultipleArrays(fillOnePlace(wynikFile))

print("Wygrał")
print(minimax(wynikFile))
print()
print("Wszystkie węzły")
printMultipleArrays(allNodes(wynikFile, []))
print("Wszystkie wyniki węzłów")
wartosciWezlow = allResults(wynikFile, [])
print(wartosciWezlow)
print("Suma wyników")
print(sum(wartosciWezlow))
print("Ilość elementów")
print(len(wartosciWezlow))
print("Dodawany wspolczynnik")
print(sum(wartosciWezlow)/len(wartosciWezlow))
print(returnEvaluation(wynikFile))
'''

wynikFile = readFromFile(N)
print()
print("Wczytana pozycja to")
printArray(wynikFile)
print("Ewaluacja tej pozycji to")
print(returnEvaluation(wynikFile))
print(returnSecondEvaluation(wynikFile))
end = time.time()
print("Czas jaki zajal trening to", end-start)