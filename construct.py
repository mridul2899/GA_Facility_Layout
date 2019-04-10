# Implementation of BGA (hard)

import math
import numpy as np
import random
from GAproj import ini_pop, alpha, populationsize, Flow

def construct(pop, Area, ratioareatoflow, AspectRatios):
    z_values = []
    for row in range(len(pop)):
        total_z = 0
        chromosome = pop[row]
        #print(chromosome)
        EMSlist = []
        coordinates_set = []
        w = math.sqrt(AspectRatios[chromosome[0] - 1] * Area[chromosome[0] - 1])
        h = math.sqrt(Area[chromosome[0] - 1] / AspectRatios[chromosome[0] - 1])
        coordinates_set.append([w / 2, h / 2])
        EMSlist.append([w, -math.inf, math.inf, math.inf])
        EMSlist.append([-math.inf, -math.inf, math.inf, 0])
        EMSlist.append([-math.inf, -math.inf, 0, math.inf])
        EMSlist.append([-math.inf, h, math.inf, math.inf])
        for i in range(1, len(chromosome)):
            x_mean = 0
            y_mean = 0
            total_flow = 0
            for j in range(i):
                x_mean += (Flow[chromosome[i] - 1][chromosome[j] - 1] * coordinates_set[j][0])
                y_mean += ((Flow[chromosome[i] - 1][chromosome[j] - 1] * coordinates_set[j][1]))
                total_flow += Flow[chromosome[i] - 1][chromosome[j] - 1]
            if total_flow != 0:
                x_mean /= total_flow
                y_mean /= total_flow
            #print(x_mean, y_mean)
            
            w = math.sqrt(AspectRatios[chromosome[i] - 1] * Area[chromosome[i] - 1])
            h = math.sqrt(Area[chromosome[i] - 1] / AspectRatios[chromosome[i] - 1])
            #print(w, h)
            new_coordinates = []
            
            for EMS in EMSlist:
                if (EMS[2] - EMS[0] < w or EMS[3] - EMS[1] < h):
                    new_coordinates.append([-math.inf, -math.inf])
                    continue
                else:
                    if (x_mean < EMS[0]):
                        x = EMS[0] + w / 2
                    elif (x_mean > EMS[2]):
                        x = EMS[2] - w / 2
                    elif (x_mean - EMS[0] >= w / 2 and EMS[2] - x_mean >= w / 2):
                        x = x_mean
                    elif (x_mean - EMS[0] > EMS[2] - x_mean):
                        x = EMS[2] - w / 2
                    else:
                        x = EMS[0] + w / 2
                    
                    if (y_mean < EMS[1]):
                        y = EMS[1] + h / 2
                    elif (y_mean > EMS[3]):
                        y = EMS[3] - h / 2
                    elif (y_mean - EMS[1] >= h / 2 and EMS[3] - y_mean >= h / 2):
                        y = y_mean
                    elif (y_mean - EMS[1] > EMS[3] - y_mean):
                        y = EMS[3] - h / 2
                    else:
                        y = EMS[1] + h / 2
                    
                    new_coordinates.append([x, y])
            #print(new_coordinates)
            #break
            min_z = math.inf
            min_coord = new_coordinates[0]
            for new_coordinate in new_coordinates:
                z = 0
                for j in range(i):
                    distance = math.sqrt(((coordinates_set[j][0] - new_coordinate[0]) ** 2) + ((coordinates_set[j][1] - new_coordinate[1]) ** 2))
                    z += distance * Flow[chromosome[j] - 1][chromosome[i] - 1]
                if z < min_z:
                    min_z = z
                    min_coord = new_coordinate
            total_z += min_z
            #print(min_z, min_coord, distance)
            coordinates_set.append(min_coord)
            for k in range(len(EMSlist)):
                EMS = EMSlist[k]
                if min_coord[0] + w / 2 < EMS[0] or min_coord[0] - w / 2 > EMS[2] or min_coord[1] + h / 2 < EMS[1] or min_coord[1] - h / 2 > EMS[3]:
                    continue
                else:
                    if (min_coord[0] + w / 2 != EMS[2]):
                        EMSlist.append([min_coord[0] + w / 2, EMS[1], EMS[2], EMS[3]])
                    if (min_coord[0] - w / 2 != EMS[0]):
                        EMSlist.append([EMS[0], EMS[1], min_coord[0] - w / 2, EMS[3]])
                    if (min_coord[1] - h / 2 != EMS[1]):
                        EMSlist.append([EMS[0], EMS[1], EMS[2], min_coord[1] - h / 2])
                    if (min_coord[1] + h / 2 != EMS[3]):
                        EMSlist.append([EMS[0], min_coord[1] + h / 2, EMS[2], EMS[3]])
                    del EMSlist[k]
            #break
        z_values.append(total_z)
        
        #break
    print(z_values)
    return z_values

if __name__ == "__main__":
    returned = ini_pop(populationsize)
    pop = returned[0]
    print(pop)
    Area = returned[1]
    ratioareatoflow = returned[2]
    AspectRatios = returned[3]
    z_values = construct(pop, Area, ratioareatoflow, AspectRatios)