# kanał elektronowy

import math
import numpy as np

filename1 = 'electrons_test.txt'
filename2 = 'electrons.txt'
filename11 = 'jets_test.txt'
filename22 = 'jets.txt'

# ładuję dane z pliku do macierzy
muonstest_arr = np.loadtxt(filename1) # muontest to ogólna nazwa zmiennej
int_muonstest_arr = muonstest_arr.astype(int)  # potrzebuję kolumny eventów jako integerów do porównywania logicznego

# ładuję dane z pliku jetów do kolejnej macierzy
# będzie potrzebne do przypadków, gdy jeden z elektronów zapisano jak jet
jets_arr = np.loadtxt(filename11)
int_jets_arr = jets_arr.astype(int)  # potrzebuję kolumny eventów jako integerów do porównywania logicznego


muonstest_count = 0

i = 0
while (i < len(muonstest_arr) - 1):
   # oraz żeby przejść przez 1000 pierwszych eventów, o których wiem, że są elektronowe
   if int_muonstest_arr[i][0] < 2000:
        # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
        if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
            # żądam, żeby suma energii była większa niż 80 Gevów, wyklucza kanał taonowy
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
                # suma pędu poprzecznego > 25 Gevów -- chcemy wykluczyć rozproszenia e- e+, które zachodzą pod małymi kątami
                if muonstest_arr[i][4] + muonstest_arr[i+1][4] > 25:
                    muonstest_count += 1
                    #print(i, int_muonstest_arr[i][0], muonstest_count, '2 e')
                    i += 1
        # przypadek, gdy wykryto jeden elektron, a drugi zaksięgowano jako mało masowy jet
        elif int_muonstest_arr[i][0] != int_muonstest_arr[i+1][0] and muonstest_arr[i][1] > 40:
            for h in range(len(jets_arr) - 1):
                # sprawdzam czy numer eventów się zgadza
                # czy energia e i jetu > 80 Gev
                # czy P_t e i jetu > 25 Gev
                # i czy masa jetu < 1 Gev
                if int_muonstest_arr[i][0] == int_jets_arr[h][0] and jets_arr[h][1] + muonstest_arr[i][1] > 80 and jets_arr[h][4] + muonstest_arr[i][4] > 25 and jets_arr[h][5] < 1:
                    muonstest_count += 1
                    #print(i,  int_muonstest_arr[i][0], int_jets_arr[h][0], muonstest_count, '1 e 1 jet')
   i += 1

print('ilosc elektronow w probce testowej', muonstest_count)
skutecznosc = muonstest_count/1000
print('skutecznosc', skutecznosc)


# teraz sprawdzam w jakim stopniu powyższy algorytm błędnie zlicza inne przypadki
muonstest_count = 0
i = 0
while (i < len(muonstest_arr) - 1):
   # sprawdzam resztę testu
   if int_muonstest_arr[i][0] > 1999:
        # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
        if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
            # żądam, żeby suma energii była większa niż 80 Gevów, wyklucza kanał taonowy
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
                # suma pędu poprzecznego > 25 Gevów -- chcemy wykluczyć rozproszenia e- e+, które zachodzą pod małymi kątami
                if muonstest_arr[i][4] + muonstest_arr[i+1][4] > 25:
                    muonstest_count += 1
                    #print(i, int_muonstest_arr[i][0], muonstest_count, '2 e')
                    i += 1
        # przypadek, gdy wykryto jeden elektron, a drugi zaksięgowano jako mało masowy jet
        elif int_muonstest_arr[i][0] != int_muonstest_arr[i+1][0] and muonstest_arr[i][1] > 40:
            for h in range(len(jets_arr) - 1):
                # sprawdzam czy numer eventów się zgadza
                # czy energia e i jetu > 80 Gev
                # czy P_t e i jetu > 25 Gev
                # i czy masa jetu < 1 Gev
                if int_muonstest_arr[i][0] == int_jets_arr[h][0] and jets_arr[h][1] + muonstest_arr[i][1] > 80 and jets_arr[h][4] + muonstest_arr[i][4] > 25 and jets_arr[h][5] < 1:
                    muonstest_count += 1
                    #print(i,  int_muonstest_arr[i][0], int_jets_arr[h][0], muonstest_count, '1 e 1 jet')
   i += 1
print('ilosc blednych rejestracji', muonstest_count)
blad = muonstest_count/3000
print('blad', blad)



# teraz przechodzę do próbki właściwej

muonstest_arr = np.loadtxt(filename2)
int_muonstest_arr = muonstest_arr.astype(int)
jets_arr = np.loadtxt(filename22)
int_jets_arr = jets_arr.astype(int)

muonstest_count = 0
i = 0
while (i < len(muonstest_arr) - 1):
        # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
        if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
            # żądam, żeby suma energii była większa niż 80 Gevów, wyklucza kanał taonowy
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
                # suma pędu poprzecznego > 25 Gevów -- chcemy wykluczyć rozproszenia e- e+, które zachodzą pod małymi kątami
                if muonstest_arr[i][4] + muonstest_arr[i+1][4] > 25:
                    muonstest_count += 1
                    #print(i, int_muonstest_arr[i][0], muonstest_count, '2 e')
                    i += 1
        # przypadek, gdy wykryto jeden elektron, a drugi zaksięgowano jako mało masowy jet
        elif int_muonstest_arr[i][0] != int_muonstest_arr[i+1][0] and muonstest_arr[i][1] > 40:
            for h in range(len(jets_arr) - 1):
                # sprawdzam czy numer eventów się zgadza
                # czy energia e i jetu > 80 Gev
                # czy P_t e i jetu > 25 Gev
                # i czy masa jetu < 1 Gev
                if int_muonstest_arr[i][0] == int_jets_arr[h][0] and jets_arr[h][1] + muonstest_arr[i][1] > 80 and jets_arr[h][4] + muonstest_arr[i][4] > 25 and jets_arr[h][5] < 1:
                    muonstest_count += 1
                    #print(i,  int_muonstest_arr[i][0], int_jets_arr[h][0], muonstest_count, '1 e 1 jet')
        i += 1
print('ilosc elektronow w probce wlasciwej', muonstest_count)
print('z poprawka na blad', math.floor(muonstest_count - blad * muonstest_count))
print('z poprawka na skutecznosc', math.floor(math.floor(muonstest_count - blad * muonstest_count)/skutecznosc))
print('z poprawka2 na skutecznosc', math.floor((muonstest_count)/(skutecznosc - blad)))
print(len(muonstest_arr))

