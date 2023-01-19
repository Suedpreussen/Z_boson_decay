# kanał hadronowy
import math
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

filename1 = 'jets_test.txt'
filename2 = 'jets.txt'



muonstest_arr = np.loadtxt(filename1) # muontest to ogólna nazwa zmiennej
int_muonstest_arr = muonstest_arr.astype(int)




muonstest_count = 0
#print('i', ' evt', ' ctn', ' mltp')
i = 0
M = 3 # granica dolna sumarycznej masy jetów
E = 40 # granica dolna sumy energii jetów

while(i < len(muonstest_arr) - 3):
    # sprawdzam tylko rozpady qq testowe
    if int_muonstest_arr[i][0] < 1000:
        # przypadek 3-jetowy
        if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] == int_muonstest_arr[i+2][0]:
            # suma energii jetów > E oraz mas jetów > M
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] + muonstest_arr[i+2][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i+2][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 3')
                i += 2
        # przypadek 2-jetowy
        elif int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] != int_muonstest_arr[i+2][0]:
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 2')
                i += 1
        # przypadek 4-jetowy
        elif int_muonstest_arr[i][0] == int_muonstest_arr[i + 1][0] == int_muonstest_arr[i + 2][0] == int_muonstest_arr[i + 3][0]:
            if muonstest_arr[i][1] + muonstest_arr[i + 1][1] + int_muonstest_arr[i + 2][0] + int_muonstest_arr[i + 3] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i + 2][5] + muonstest_arr[i+3][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 4')
                i += 3
    i += 1
print('ilosc przypadkow qq w probce testowej', muonstest_count)
skutecznosc = muonstest_count/1000
print('skutecznosc', skutecznosc)


# teraz sprawdzam w jakim stopniu powyższy algorytm błędnie zlicza inne przypadki

muonstest_count = 0
#print('i', ' evt', ' ctn', ' mltp')
i = 0
while(i < len(muonstest_arr) - 3):
    # sprawdzam tylko rozpady qq testowe
    if int_muonstest_arr[i][0] > 999:
        # przypadek 3-jetowy
        if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] == int_muonstest_arr[i+2][0]:
            # suma energii jetów > E oraz mas jetów > M
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] + muonstest_arr[i+2][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i+2][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 3')
                i += 2
        # przypadek 2-jetowy
        elif int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] != int_muonstest_arr[i+2][0]:
            if muonstest_arr[i][1] + muonstest_arr[i+1][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 2')
                i += 1
        # przypadek 4-jetowy
        elif int_muonstest_arr[i][0] == int_muonstest_arr[i + 1][0] == int_muonstest_arr[i + 2][0] == int_muonstest_arr[i + 3][0]:
            if muonstest_arr[i][1] + muonstest_arr[i + 1][1] + int_muonstest_arr[i + 2][0] + int_muonstest_arr[i + 3] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i + 2][5] + muonstest_arr[i+3][5] > M:
                muonstest_count += 1
                #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 4')
                i += 3
    i += 1
print('ilosc blednych rejestracji', muonstest_count)
blad = muonstest_count/4000
print('blad', blad)




# teraz przechodzę do próbki właściwej



muonstest_arr = np.loadtxt(filename2)
int_muonstest_arr = muonstest_arr.astype(int)




muonstest_count = 0
#print('i', ' evt', ' ctn', ' mltp')
i = 0
while(i < len(muonstest_arr) - 3):
    # przypadek 3-jetowy
    if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] == int_muonstest_arr[i+2][0]:
        # suma energii jetów > E oraz mas jetów > M
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] + muonstest_arr[i+2][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i+2][5] > M:
            muonstest_count += 1
            #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 3')
            i += 2
    # przypadek 2-jetowy
    elif int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0] != int_muonstest_arr[i+2][0]:
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] > M:
            muonstest_count += 1
            #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 2')
            i += 1
    # przypadek 4-jetowy
    elif int_muonstest_arr[i][0] == int_muonstest_arr[i + 1][0] == int_muonstest_arr[i + 2][0] == int_muonstest_arr[i + 3][0]:
        if muonstest_arr[i][1] + muonstest_arr[i + 1][1] + int_muonstest_arr[i + 2][0] + int_muonstest_arr[i + 3] > E and muonstest_arr[i][5] + muonstest_arr[i+1][5] + muonstest_arr[i + 2][5] + muonstest_arr[i+3][5] > M:
            muonstest_count += 1
            #print(i, ' ', int_muonstest_arr[i][0], ' ', muonstest_count, ' 4')
            i += 3
    i += 1
print('ilosc przypadkow qq w probce wlasciwej', muonstest_count)
print('z poprawka na blad', math.floor(muonstest_count - blad * muonstest_count))
print('z poprawka na skutecznosc', math.floor(math.floor(muonstest_count - blad * muonstest_count)/skutecznosc))
print('z poprawka2 na skutecznosc', math.floor((muonstest_count)/(skutecznosc - blad)))
print(len(muonstest_arr))



