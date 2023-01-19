# Mamy 4 kanały rozpadu zauważalne w detektorze oraz przypadki tła (niestety neutrina są obsługiwane przez ten detektor)
# Zacznijmy od muonów, warunki:
# muszą być dwa zarejestrowane muony o sumarycznej energii większej niż 60 Gevów
# w ten sposób wyeliminujemy muony zauważane w rozpadzie taonowym oraz tła


import math
import numpy as np
filename1 = 'muons_test.txt'
filename2 = 'muons.txt'

# ładuję dane z pliku do macierzy
muonstest_arr = np.loadtxt(filename1)
int_muonstest_arr = muonstest_arr.astype(int) # potrzebuję kolumny eventów jako integerów do porównywania logicznego

#print('i', 'evt', 'ctn')
muonstest_count = 0
for i in range(len(muonstest_arr) - 1):
    # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi muonami
    # oraz żeby przejść przez 1000 pierwszych eventów, o których wiem,że są muonowe
    if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] and int_muonstest_arr[i][0] < 3000:
        # żądam, żeby suma energii była większa niż 80 Gevów
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
            muonstest_count += 1
            #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count)
print('ilosc muonow w probce testowej', muonstest_count)
skutecznosc = muonstest_count/1000
print('skutecznosc', skutecznosc)



# teraz sprawdzam w jakim stopniu powyższy algorytm błędnie zlicza inne przypadki
muonstest_count = 0
for i in range(len(muonstest_arr) - 1):
    if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] and 3000 < int_muonstest_arr[i][0] < 5000:
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
            muonstest_count += 1
print('ilosc blednych rejestracji', muonstest_count)
blad = muonstest_count/2000
print('blad', blad)



# teraz przechodzę do próbki właściwej

muonstest_arr = np.loadtxt(filename2)
int_muonstest_arr = muonstest_arr.astype(int)

muonstest_count = 0
for i in range(len(muonstest_arr) - 1):
    if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] > 80:
            muonstest_count += 1


print('ilosc muonow w probce wlasciwej', muonstest_count)
print('z poprawka na skutecznosc', math.floor(muonstest_count/skutecznosc))
print(len(muonstest_arr))

