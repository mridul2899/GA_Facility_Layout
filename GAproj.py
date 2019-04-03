import math
import numpy as np
import random

alpha = 5
populationsize = 5
Flow = [[0, 0, 2, 1, 0, 4, 3, 0, 0, 5],
[0, 0, 3, 0, 2, 2, 8, 0, 10, 0],
[2, 3, 0, 0, 0, 6, 3, 0, 5, 0],
[1, 0, 0, 0, 7, 1, 0, 5, 0, 0],
[0, 2, 0, 7, 0, 0, 0, 0, 0, 0],
[4, 2, 6, 1, 0, 0, 0, 0, 0, 1],
[3, 8, 3, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 5, 0, 0, 1, 0, 3, 0],
[0, 10, 5, 0, 0, 0, 0, 3, 0, 0],
[5, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

def ini_pop(populationsize):
	init_pop = []
	Area = np.random.uniform(5, 15, len(Flow)) # section 4.2.3
	ratioareatoflow = [Area[j] / (sum(Flow[j][i] for i in range(len(Flow[0])))) for j in range(len(Flow))]
	AspectRatios = np.random.uniform(0.176, 5.664, len(Flow))
	for k in range(populationsize):
		intisequence = np.argsort(ratioareatoflow) + 1
		initRCL = [intisequence[j] for j in range(alpha)]
		placed = random.choice(initRCL)
		sequence = []
		IncresingRiFlow = []
		sequence.append(placed)
		for j in range(len(Flow) - 1):
			flowfacility = np.nonzero(Flow[placed - 1])[0] + 1
			flowfrmfacility = list(set(flowfacility) - set(sequence))
			if len(flowfrmfacility) > 0:
				for i in range(len(intisequence)):
					if intisequence[i] in flowfrmfacility:
						IncresingRiFlow.append(intisequence[i])	
			else:
				unplaced = list(set(intisequence) - set(sequence))
				for i in range(len(intisequence)):
					if intisequence[i] in unplaced:
						IncresingRiFlow.append(intisequence[i])
			if len(IncresingRiFlow) > alpha:
				RCL = [IncresingRiFlow[j] for j in range(alpha)]
			else:
				RCL = IncresingRiFlow
			placed = random.choice(RCL)
			sequence.append(placed)
			IncresingRiFlow.clear()
		init_pop.append(sequence)
	return init_pop, Area, ratioareatoflow, AspectRatios

if __name__ == "__main__":
	pop = ini_pop(populationsize)[0]
	print(pop)