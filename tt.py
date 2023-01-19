# kanał taonowy
import math
import numpy as np

filename1 = 'electrons_test.txt'
filename2 = 'electrons.txt'
filename11 = 'jets_test.txt'
filename22 = 'jets.txt'
filename111 = 'muons_test.txt'
filename222 = 'muons.txt'
filename1111 = 'energy_test.txt'
filename2222 = 'energy.txt'



electron_arr = np.loadtxt(filename1)
int_electron_arr = electron_arr.astype(int)

jets_arr = np.loadtxt(filename11)
int_jets_arr = jets_arr.astype(int)

muonstest_arr = np.loadtxt(filename111)
int_muonstest_arr = muonstest_arr.astype(int)

energy_arr = np.loadtxt(filename1111)
int_energy_arr = energy_arr.astype(int)
E_d = 10  # dolny limit sumy energii, chcemy wykluczyć tło
E_g = 70  # górny limit sumy energii, straty energii na produkcję neutrin
E_2 = 70  # górny limit sumy energii obu składników
M = 4 # górny limit masy jetów
taon_count = 0
i = 0
while (i < len(electron_arr) - 1):
    # oraz żeby przejść przez 1000 eventów, o których wiem, że są taonowe
    if 2999 < int_electron_arr[i][0] < 4000:
         # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
         if int_electron_arr[i][0] == int_electron_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał elektronowy
             if electron_arr[i][1] + electron_arr[i+1][1] < E_2:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count += 1
                        #print(i, int_electron_arr[i][0], taon_count, '2e', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 elektron 1 muon
         elif int_electron_arr[i][0] != int_electron_arr[i + 1][0]:
            for m in range(len(muonstest_arr) - 1):
                if int_electron_arr[i][0] == int_muonstest_arr[m][0] and electron_arr[i][1] + muonstest_arr[m][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count += 1
                            #print(i,  int_electron_arr[i][0], int_muonstest_arr[m][0], electron_arr[i][1],  muonstest_arr[m][1], taon_count, '1e-1m', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2e 1e1m', taon_count)


# teraz sprawdzam przypadki z jetami
taon_count2 = 0
i = 0
while (i < len(jets_arr) - 1):
    # oraz żeby przejść przez 1000 eventów, o których wiem, że są taonowe
    if 2999 < int_jets_arr[i][0] < 4000:
         # przypadek dwu jetowy
         if int_jets_arr[i][0] == int_jets_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów i masa mniejsza niz M, wyklucza kanał hadronowy
             if jets_arr[i][1] + jets_arr[i+1][1] < E_2 and jets_arr[i][5] + jets_arr[i+1][5] < M:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_jets_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count2 += 1
                        #print(i, int_jets_arr[i][0], taon_count2, '2j', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 jet 1 elektron
         elif int_jets_arr[i][0] != int_jets_arr[i + 1][0]:
            for q in range(len(electron_arr) - 1):
                if int_electron_arr[q][0] == int_jets_arr[i][0] and electron_arr[q][1] + jets_arr[i][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_electron_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count2 += 1
                            #print(i,  int_electron_arr[q][0], int_jets_arr[i][0], electron_arr[q][1],  jets_arr[i][1], taon_count2, '1j-1e', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2j 1j1e', taon_count2)

# teraz sprawdzam pozostałe przypadki z muonami
taon_count3 = 0
i = 0
while (i < len(muonstest_arr) - 1):
    # oraz żeby przejść przez 1000 eventów, o których wiem, że są taonowe
    if 2999 < int_muonstest_arr[i][0] < 4000:
         # przypadek 2 muony
         if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał muonowy
             if muonstest_arr[i][1] + muonstest_arr[i+1][1] < E_2:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_muonstest_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count3 += 1
                        #print(i, int_muonstest_arr[i][0], taon_count3, '2m', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 muon 1 jet
         elif int_muonstest_arr[i][0] != int_muonstest_arr[i + 1][0]:
            for q in range(len(jets_arr) - 1):
                if int_jets_arr[q][0] == int_muonstest_arr[i][0] and jets_arr[q][1] + muonstest_arr[i][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_jets_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count3 += 1
                            #print(i,  int_jets_arr[q][0], int_muonstest_arr[i][0], jets_arr[q][1],  muonstest_arr[i][1], taon_count3, '1m-1j', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2m 1m1j', taon_count3)
print("calkowita liczba zliczen testowych taonów:", taon_count + taon_count2 + taon_count3)
skutecznosc = (taon_count + taon_count2 + taon_count3)/1000
print("skutecznosc:", skutecznosc)







# teraz sprawdzam w jakim stopniu powyższy algorytm błędnie zlicza inne przypadki
print('bledy')
taon_count = 0
i = 0
while (i < len(electron_arr) - 1):
    # żeby przejść przez resztę eventów, o których wiem, że nie są taonowe
    if not 2999 < int_electron_arr[i][0] < 4000:
         # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
         if int_electron_arr[i][0] == int_electron_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał elektronowy
             if electron_arr[i][1] + electron_arr[i+1][1] < E_2:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count += 1
                        #print(i, int_electron_arr[i][0], taon_count, '2e', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 elektron 1 muon
         elif int_electron_arr[i][0] != int_electron_arr[i + 1][0]:
            for m in range(len(muonstest_arr) - 1):
                if int_electron_arr[i][0] == int_muonstest_arr[m][0] and electron_arr[i][1] + muonstest_arr[m][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count += 1
                            #print(i,  int_electron_arr[i][0], int_muonstest_arr[m][0], electron_arr[i][1],  muonstest_arr[m][1], taon_count, '1e-1m', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2e 1e1m', taon_count)
blad = taon_count/3000
print('blad', blad)

# teraz sprawdzam przypadki z jetami
taon_count2 = 0
i = 0
while (i < len(jets_arr) - 1):
    # żeby przejść przez resztę eventów, o których wiem, że nie są taonowe
    if not 2999 < int_jets_arr[i][0] < 4000:
         # przypadek dwu jetowy
         if int_jets_arr[i][0] == int_jets_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał hadronowy
             if jets_arr[i][1] + jets_arr[i+1][1] < E_2 and jets_arr[i][5] + jets_arr[i+1][5] < M:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_jets_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count2 += 1
                        #print(i, int_jets_arr[i][0], taon_count2, '2j', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 jet 1 elektron
         elif int_jets_arr[i][0] != int_jets_arr[i + 1][0]:
            for q in range(len(electron_arr) - 1):
                if int_electron_arr[q][0] == int_jets_arr[i][0] and electron_arr[q][1] + jets_arr[i][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_electron_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count2 += 1
                            #print(i,  int_electron_arr[q][0], int_jets_arr[i][0], electron_arr[q][1],  jets_arr[i][1], taon_count2, '1j-1e', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2j 1j1e', taon_count2)
blad2= taon_count2/4000
print('blad2', blad2)

# teraz sprawdzam pozostałe przypadki z muonami
taon_count3 = 0
i = 0
while (i < len(muonstest_arr) - 1):
    # żeby przejść przez resztę eventów, o których wiem, że nie są taonowe
    if not 2999 < int_muonstest_arr[i][0] < 4000:
         # przypadek 2 muony
         if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
             # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał muonowy
             if muonstest_arr[i][1] + muonstest_arr[i+1][1] < E_2:
                 #sprawdzam sumaryczną energię
                 for e in range(len(energy_arr)):
                     if int_muonstest_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                        taon_count3 += 1
                        #print(i, int_muonstest_arr[i][0], taon_count3, '2m', int_energy_arr[e][0], energy_arr[e][1])
                        i += 1
         # przypadek 1 muon 1 jet
         elif int_muonstest_arr[i][0] != int_muonstest_arr[i + 1][0]:
            for q in range(len(jets_arr) - 1):
                if int_jets_arr[q][0] == int_muonstest_arr[i][0] and jets_arr[q][1] + muonstest_arr[i][1] < E_2:
                    # sprawdzam sumaryczną energię
                    for e in range(len(energy_arr)):
                        if int_jets_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                            taon_count3 += 1
                            #print(i,  int_jets_arr[q][0], int_muonstest_arr[i][0], jets_arr[q][1],  muonstest_arr[i][1], taon_count3, '1m-1j', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2m 1m1j', taon_count3)
blad3 = taon_count3/2000
print('blad3', blad3)
blad_sr = (blad + blad2 + blad3)/3
print('usredniony blad', blad_sr)

# przechodzimy do właściwej próbki

electron_arr = np.loadtxt(filename2)
int_electron_arr = electron_arr.astype(int)

jets_arr = np.loadtxt(filename22)
int_jets_arr = jets_arr.astype(int)

muonstest_arr = np.loadtxt(filename222)
int_muonstest_arr = muonstest_arr.astype(int)

energy_arr = np.loadtxt(filename2222)
int_energy_arr = energy_arr.astype(int)

taon_count = 0
i = 0
while (i < len(electron_arr) - 1):
    # żądam, żeby brać pod uwagę eventy z dwoma wykrytymi elektronami
    if int_electron_arr[i][0] == int_electron_arr[i+1][0]:
        # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał elektronowy
        if electron_arr[i][1] + electron_arr[i+1][1] < E_2:
            #sprawdzam sumaryczną energię
            for e in range(len(energy_arr)):
                if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                   taon_count += 1
                   #print(i, int_electron_arr[i][0], taon_count, '2e', int_energy_arr[e][0], energy_arr[e][1])
                   i += 1
    # przypadek 1 elektron 1 muon
    elif int_electron_arr[i][0] != int_electron_arr[i + 1][0]:
       for m in range(len(muonstest_arr) - 1):
           if int_electron_arr[i][0] == int_muonstest_arr[m][0] and electron_arr[i][1] + muonstest_arr[m][1] < E_2:
               # sprawdzam sumaryczną energię
               for e in range(len(energy_arr)):
                   if int_electron_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                       taon_count += 1
                       #print(i,  int_electron_arr[i][0], int_muonstest_arr[m][0], electron_arr[i][1],  muonstest_arr[m][1], taon_count, '1e-1m', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2e 1e1m', taon_count)


# teraz sprawdzam przypadki z jetami
taon_count2 = 0
i = 0
while (i < len(jets_arr) - 1):
    # przypadek dwu jetowy
    if int_jets_arr[i][0] == int_jets_arr[i+1][0]:
        # żądam, żeby suma energii była mniejsza niż E_2 Gevów i masa mniejsza niz M, wyklucza kanał hadronowy
        if jets_arr[i][1] + jets_arr[i+1][1] < E_2 and jets_arr[i][5] + jets_arr[i+1][5] < M:
            #sprawdzam sumaryczną energię
            for e in range(len(energy_arr)):
                if int_jets_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                   taon_count2 += 1
                   #print(i, int_jets_arr[i][0], taon_count2, '2j', int_energy_arr[e][0], energy_arr[e][1])
                   i += 1
    # przypadek 1 jet 1 elektron
    elif int_jets_arr[i][0] != int_jets_arr[i + 1][0]:
       for q in range(len(electron_arr) - 1):
           if int_electron_arr[q][0] == int_jets_arr[i][0] and electron_arr[q][1] + jets_arr[i][1] < E_2:
               # sprawdzam sumaryczną energię
               for e in range(len(energy_arr)):
                   if int_electron_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                       taon_count2 += 1
                       #print(i,  int_electron_arr[q][0], int_jets_arr[i][0], electron_arr[q][1],  jets_arr[i][1], taon_count2, '1j-1e', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2j 1j1e', taon_count2)

# teraz sprawdzam pozostałe przypadki z muonami
taon_count3 = 0
i = 0
while (i < len(muonstest_arr) - 1):
    # przypadek 2 muony
    if int_muonstest_arr[i][0] == int_muonstest_arr[i+1][0]:
        # żądam, żeby suma energii była mniejsza niż E_2 Gevów, wyklucza kanał muonowy
        if muonstest_arr[i][1] + muonstest_arr[i+1][1] < E_2:
            #sprawdzam sumaryczną energię
            for e in range(len(energy_arr)):
                if int_muonstest_arr[i][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                   taon_count3 += 1
                   #print(i, int_muonstest_arr[i][0], taon_count3, '2m', int_energy_arr[e][0], energy_arr[e][1])
                   i += 1
    # przypadek 1 muon 1 jet
    elif int_muonstest_arr[i][0] != int_muonstest_arr[i + 1][0]:
       for q in range(len(jets_arr) - 1):
           if int_jets_arr[q][0] == int_muonstest_arr[i][0] and jets_arr[q][1] + muonstest_arr[i][1] < E_2:
               # sprawdzam sumaryczną energię
               for e in range(len(energy_arr)):
                   if int_jets_arr[q][0] == int_energy_arr[e][0] and E_d < energy_arr[e][1] < E_g:
                       taon_count3 += 1
                       #print(i,  int_jets_arr[q][0], int_muonstest_arr[i][0], jets_arr[q][1],  muonstest_arr[i][1], taon_count3, '1m-1j', int_energy_arr[e][0], energy_arr[e][1])
    i += 1
print('2m 1m1j', taon_count3)
taon_count_sum = taon_count + taon_count2 + taon_count3
print("calkowita liczba zliczen taonów:", taon_count_sum)
print('z poprawka na blad', math.floor(taon_count_sum - blad_sr * taon_count_sum))
print('z poprawka na skutecznosc', math.floor(math.floor(taon_count_sum - blad_sr * taon_count_sum)/skutecznosc))
print('z poprawka2 na skutecznosc', math.floor((taon_count_sum)/(skutecznosc - blad_sr)))