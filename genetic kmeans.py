# GKA dengan non-fixed number of K

import math
import random
import copy
import matplotlib.pyplot as plt
import datasets
import popfunction
import evaluasi
import otherfunction


def ngerandom(minval, maxval):
    alfa = random.random()
    hasil = alfa*minval + (1-alfa) * maxval
    return hasil


def popinit(popsize, klusmin, klusmax):
# inisialisasi populasi (kumpulan solusi)
    global idvdke
    global minx
    global maxx
    global miny
    global maxy
    pop = []
    for k in range(klusmin, klusmax+1):
        for i in range(int(popsize/(klusmax+1 - klusmin))):
            ss = [-10]
            for j in range(k):
                ss.append([ngerandom(minx-1, maxx+1), ngerandom(miny-1, maxy+1)])
            idvdke = idvdke + 1
            ss.append('ke-' + str(idvdke))
            ss.append('random')
            pop.append(ss)
    return pop


def co(populasi, co_rate, popsize):
    # crossover
    cr = math.ceil(co_rate * popsize)
    anakanak = []
    global idvdke
    while len(anakanak) < cr:
    #for i in range(cr):
        ortu1 = copy.deepcopy(populasi[random.randint(0, len(populasi)-1)])
        ortu2 = copy.deepcopy(populasi[random.randint(0, len(populasi)-1)])

        anak1 = copy.deepcopy(ortu1)
        anak2 = copy.deepcopy(ortu2)

        gen1_idx = random.randint(1, len(anak1)-3)
        gen2_idx = random.randint(1, len(anak2)-3)

        anak1[gen1_idx], anak2[gen2_idx] = copy.deepcopy(anak2[gen2_idx]), copy.deepcopy(anak1[gen1_idx])
        idvdke += 1
        anak1[len(anak1)-2] =  'ke-' + str(idvdke) + ''
        anak1[0] = -10
        anak1[len(anak1)-1] =  'crossover'
        idvdke += 1
        anak2[len(anak2)-2] =  'ke-' + str(idvdke) + ''
        anak2[0] = -10
        anak2[len(anak2)-1] =  'crossover'
        anakanak.append(anak1)
        anakanak.append(anak2)

    for i in anakanak:
        populasi.append(i)

    return populasi


def mut(populasi, mut_rate, popsize):
# mutasi
    global idvdke
    global minx
    global maxx
    global miny
    global maxy
    poplama = copy.deepcopy(populasi)
    for mr in range(math.ceil(mut_rate * popsize)):

        ortu = copy.deepcopy(populasi[random.randint(0, len(populasi)-1)])
        anak = copy.deepcopy(ortu)

        idvdke += 1

        for i in range(1, len(anak)-2):
            while True:
                gaux = (random.gauss(0, 1)*maxx)
                if (anak[i][0] + gaux >= minx-10) and (anak[i][0] + gaux <= maxx+10):
                    anak[i][0] = anak[i][0] + gaux
                    break
            while True:
                gauy = (random.gauss(0, 1)*maxy)
                if (anak[i][1] + gauy >= miny-10) and (anak[i][1] + gauy <= maxy+10):
                    anak[i][1] = anak[i][1] + gauy
                    break
        anak[len(anak)-2] =  'ke-' + str(idvdke) + ''
        anak[0] = -10
        anak[len(anak)-1] =  'mutasi'
        poplama.append(anak)
    return poplama



global idvdke
idvdke = 0
mutation_rate = float(input('masukkan mutation rate: '))
crossover_rate = float(input('masukkan crossover rate: '))
popsize = int(input('masukkan ukuran populasi: '))

klusmin = 2
klusmax = 8
injek = klusmax - klusmin + 1

maxiter = 100
popsize = int((math.floor(popsize/(klusmax+1 - klusmin))) * (klusmax+1 - klusmin))
iter = 1

#inisialisasi titik
titik = datasets.data682min10

# kluster benar untuk rand index
klusterbenar = datasets.klusterbenardata682min10

# perhitungan minx maxx miny maxy untuk inisialisasi populasi
x = []
y = []
for ttk in titik:
    x.append(ttk[0]) # *10
    y.append(ttk[1]) # *10

global minx
global maxx
global miny
global maxy
minx = math.floor(min(x))
maxx = math.ceil(max(x))
miny = math.floor(min(y))
maxy = math.ceil(max(y))

#inisialisasi pop awal
pop = popinit(popsize, klusmin, klusmax)


elitism_box = [-10]
restarts_box = []
break_box = [-10]
# nocostsave = 0
# inputcostsave = 0

fitness_t = -10
fitness_tmin1 = -10
rech_score = []

print(popsize)
input('lanjut: ')
while ( iter <= maxiter ):
    

    # INJEK POP
    tambahpop = []
    if math.fmod(iter, 20) == 0: # insert random individu setiap 20 iterasi
        # input('syarat terpenuhi, maka akan dilakukan random injection..')
        tambahpop = popinit(injek, klusmin, klusmax)
        for i in tambahpop:
            pop.append(i)


    # REPRODUKSI
    pop = copy.deepcopy(co(pop, crossover_rate, popsize))
    # print(idvdke)
    pop = copy.deepcopy(mut(pop, mutation_rate, popsize))
    # print(idvdke)

    print('========== ITERASI KE-' + str(iter) + ' ==========')


    # EVALUASI
    for u in range(len(pop)):
        if pop[u][0] == -10:
            centroid = copy.deepcopy(pop[u]) 

            kluster, centroidkm = evaluasi.km(centroid, titik)

            # menghitung nilai fitness individu (kombinasi centroid awal)
            pop[u][0] = evaluasi.RandIndex(titik, klusterbenar, kluster) + 0

        print('===== CENTROIDS-' + str(u) + ' =====')
        print(pop[u])

        print('===== KLUSTERING =====')


    # SELEKSI
    idvd_terbaik = copy.deepcopy(pop[0]) # idvd_terbaik simpan individu terbaik iterasi terbaru
    pop = copy.deepcopy(popfunction.selection(pop[1:len(pop)], popsize-1)) # individu terbaik langsung lolos
    pop.insert(0, idvd_terbaik)


    # BREAKER
    pop, bre, elitism_box, restarts_box, break_box = otherfunction.breaker(pop, popinit, popsize, klusmin, klusmax, elitism_box, restarts_box, break_box)
    if bre == 1:
        break


    # RECHENBERG
    fitness_t, fitness_tmin1, mutation_rate, rech_score = otherfunction.rech(fitness_t, fitness_tmin1, elitism_box, iter, mutation_rate, rech_score)


    iter = iter + 1

print(" ")
print("========== ITERASI DIHENTIKAN ==========")
print(" ")
print("Iterasi: ")
print(iter)
print(" ")
print("Individu Terbaik: ")
print(elitism_box)