import copy
import math


def breaker(populasi, inisialisasi, popsize, klusmin, klusmax, elitism_box, restarts_box, break_box):
    # RESTARTS DAN BREAKER
    
    bre = 0
    pop = copy.deepcopy(populasi)
    pop.sort()
    pop.reverse()
    if elitism_box[0] <= pop[0][0]:
        if elitism_box[0] < pop[0][0]:
            elitism_box = copy.deepcopy(pop[0]) # elitism_box simpan individu terbaik iterasi terawal
        restarts_box.insert(0, elitism_box[0])
        # inputcostsave += 1
    if len(restarts_box) > 3:
        restarts_box.pop(3)

    if len(restarts_box) == 3:
        if restarts_box[0] == restarts_box[1] == restarts_box[2]:
            # input('syarat terpenuhi, maka akan dilakukan restarts..')
            pop = inisialisasi(popsize, klusmin, klusmax) # restarts
            if break_box[0] <= restarts_box[0]:
                break_box.insert(0, restarts_box[0])
            restarts_box = []
            # nocostsave += 1
    
    if len(break_box) > 5:
        break_box.pop(5)
    if len(break_box) == 5:
        if break_box[0] == break_box[1] == break_box[2] == break_box[3] == break_box[4]:
            bre = 1 # break

    return pop, bre, elitism_box, restarts_box, break_box


def rech(fitness_t, fitness_tmin1, elitism_box, iter, mutation_rate, rech_score):
    #RECHENBERG
    fitness_t = copy.deepcopy(elitism_box[0])
    if fitness_t > fitness_tmin1:
        rech_score.append(1)
    else:
        rech_score.append(0)
    fitness_tmin1 = copy.deepcopy(fitness_t)

    if math.fmod(iter, 5) == 0:
        # input('syarat rechenberg terpenuhi, maka akan dilakukan..')
        if sum(rech_score) >= 3:
            mutation_rate = ((mutation_rate*10) + 1) / 10
        else:
            if (((mutation_rate*10) - 1) / 10) > 0:
                mutation_rate = ((mutation_rate*10) - 1) / 10
        rech_score = []

    return fitness_t, fitness_tmin1, mutation_rate, rech_score