# Implementation of BGA (hard)

import math
import numpy as np
import random
from GAproj import ini_pop, alpha, populationsize, Flow

def construct(pop, Area, ratioareatoflow, AspectRatios):
    for row in range(len(pop)):
        chromosome = pop[row]
        print(chromosome)
        EMSlist = []
        coordinates = []
        w = math.sqrt(AspectRatios[chromosome[0] - 1] * Area[chromosome[0] - 1])
        h = math.sqrt(Area[chromosome[0] - 1] / AspectRatios[chromosome[0] - 1])
        coordinates.append([w / 2, h / 2])
        EMSlist.append([w, -math.inf, math.inf, math.inf])
        EMSlist.append([-math.inf, -math.inf, math.inf, 0])
        EMSlist.append([-math.inf, -math.inf, 0, math.inf])
        EMSlist.append([-math.inf, h, math.inf, math.inf])
        for i in range(1, len(chromosome)):
            
            # w = math.sqrt(AspectRatios[i - 1] * Area[i - 1])
            # h = math.sqrt(Area[i - 1] / AspectRatios[i - 1])
            # new_coordinates = []
            # for EMS in EMSlist:
            #     x = 0
            #     y = 0
            #     if (x_mean >= EMS[0] and x_mean <= EMS[2]):
            #         if (x_mean - EMS[0] >= w / 2):
            #             x = x_mean
            #         else:
            #             x = EMS[0] + w / 2
            #     else if (x_mean > EMS[2]):
            #         x = EMS[2] - w / 2
            #     else:
            #         x = EMS[0] + w / 2
            #     if (y_mean >= EMS[1] and x_mean <= EMS[3]):
            #         if (y_mean - EMS[1] >= h / 2):
            #             y = y_mean
            #         else:
            #             y = EMS[1] + h / 2
            #     else if (y_mean > EMS[3]):
            #         y = EMS[3] - h / 2
            #     else:
            #         y = EMS[1] + h / 2
            #     new_coordinates.append([x, y])
        print(EMSlist)
        break

if __name__ == "__main__":
    returned = ini_pop(populationsize)
    pop = returned[0]
    Area = returned[1]
    ratioareatoflow = returned[2]
    AspectRatios = returned[3]
    construct(pop, Area, ratioareatoflow, AspectRatios)