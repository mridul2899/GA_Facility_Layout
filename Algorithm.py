import math
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import operator

from GAproj import ini_pop, alpha, nPop, Flow
from construct import construct


def crossover(p1,p2):
    parent = random.randint(0,1)
    N_inherit = random.randint(0,9)
    fixed = list(random.sample(range(1, 10), N_inherit))
    child = []
    index = list(np.array([0,1,2,3,4,5,6,7,8,9]))
    ele_inserted = []
    count = 0
    if(parent == 0):
        parent = p1
        other = p2
    else:
        parent = p2
        other = p1
    for i in fixed:
        ele_inserted.append(parent[i])
    for i in range (0,10):
        if(i in fixed):
            child.append(parent[i])
        else:
            while(other[count] in ele_inserted):
                count+=1
            child.append(other[count])
            count+=1
    
    return list(child)

def algorithm1(alpha,nPop):
    t = 0
    returned = ini_pop(nPop)
    pop = returned[0]
    Area = returned[1]
    ratioareatoflow = returned[2]
    AspectRatios = returned[3]
    GC = 1
    QGA = 1
    z_values = construct(pop, Area, ratioareatoflow, AspectRatios, GC, QGA)
    no_change = 0
    diff = 10000
    while((no_change!=nPop) and (diff>0.05)):
        child_pop = []
        for i in range(0,nPop):
            child_pop.append(pop[i])
            p1 = pop[random.randint(0,9)]
            p2 = pop[random.randint(0,9)]
            d = crossover(p1,p2)
            child_pop.append(d)
        z_values = construct(child_pop,Area,ratioareatoflow, AspectRatios, GC, QGA)
        indexed_values = list(enumerate(z_values)) 
        top_n = sorted(indexed_values, key=operator.itemgetter(1))[:nPop]
        top_n = list(([i for i, v in top_n]))
        count = 0
        no_change = 0
        sums = 0
        for i in top_n:
            if(child_pop[i] in pop):
                no_change += 1
            pop[count] = child_pop[i] 
            count+=1
            sums += z_values[i]
        diff = 100 * abs((sums/nPop)-z_values[top_n[0]])/(sums/nPop)
    return pop[0],z_values[top_n[0]]

if __name__ == "__main__":
	solution = algorithm1(alpha,nPop)
	print("The optimal solution is")
	print(solution)


