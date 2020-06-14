import random
import copy
import numpy as np
import pandas as pd

class Route():

    def __init__(self, request, time_open, time_close):
        self.request    = request
        self.time_open  = time_open
        self.time_close = time_close

    def read_time(self, file):
        data       = pd.read_csv(file).values.T
        self.index = data[0]
        self.time  = data[1::]

    def generate(self, individual):
        order = np.array([np.random.choice(self.request, len(self.request), replace=False) for i in range(individual)])
        self.order = order

    def crossover(self, evaluation):

        population_c = np.empty((len(self.order), len(self.request)), dtype=int)

        for i in range(0, len(self.order), 2):

            parents   = np.random.choice(len(self.order), 2, replace=False, p=evaluation)
            crossover = np.random.choice(len(self.request), 2, replace=False)

            if crossover[0] > crossover[1]:  crossover[0], crossover[1] = crossover[1], crossover[0]

            population_c[i]   = self.order[parents[0]].copy()
            population_c[i+1] = self.order[parents[1]].copy()
        
            for j in range(crossover[0], crossover[1]+1):

                index0 = np.where(population_c[i]   == self.order[parents[1]][j])
                index1 = np.where(population_c[i+1] == self.order[parents[0]][j])

                population_c[i][j],   population_c[i][index0[0][0]]   = population_c[i][index0[0][0]],   population_c[i][j]
                population_c[i+1][j], population_c[i+1][index1[0][0]] = population_c[i+1][index1[0][0]], population_c[i+1][j]
    
        self.order =  population_c.copy()