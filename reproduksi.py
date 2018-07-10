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
