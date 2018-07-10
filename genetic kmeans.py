# GKA dengan non-fixed number of K

import math
import random
import copy
import matplotlib.pyplot as plt
import popfunction
import reproduksi
import evaluasi


def ngerandom(minval, maxval):
    alfa = random.random()
    hasil = alfa*minval + (1-alfa) * maxval
    return hasil


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
pop = popfunction.popinit(popsize, klusmin, klusmax)

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
    if math.fmod(iter, 20) == 0:
        # input('syarat terpenuhi, maka akan dilakukan random injection..')
        tambahpop = popfunction.popinit(injek, klusmin, klusmax)
        for i in tambahpop:
            pop.append(i)


    # REPRODUKSI
    pop = copy.deepcopy(reproduksi.co(pop, crossover_rate, popsize))
    # print(idvdke)
    pop = copy.deepcopy(reproduksi.mut(pop, mutation_rate, popsize))
    # print(idvdke)

    print('========== ITERASI KE-' + str(iter) + ' ==========')
