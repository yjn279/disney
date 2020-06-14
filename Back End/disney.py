import sys
import copy
import math
import random
import numpy as np
import pandas as pd
from pyproj import Geod
from fastpass import FastPass
from standby import StandBy


individual = 100
generation = 100
time_open  =  8.0 * 60
time_close = 22.0 * 60


request = []
for i in sys.argv[1:]:  request.append(int(i))

if len(request) < 2:
    print('ERROR: Please select at least 2 attractions.')
    exit()


fp = FastPass(request, time_open,time_close)
sb = StandBy(request, time_open, time_close)

fp.read_time('/home/bitnami/navigation/FP.csv')
sb.read_time('/home/bitnami/navigation/WaitingTime.csv')
sb.read_coordinate('/home/bitnami/navigation/Coordinate.csv', 2)

fp.generate(individual)
sb.generate(individual)

for i in range(generation):
    
    ticket = fp.calculate_fastpass()
    sb.calculate_standby(ticket, fp.order)

    score, evaluation = sb.score()
    if sum(evaluation) == 0:  break    
    fp.crossover(evaluation)
    sb.crossover(evaluation)

index  = score.argmax()
hour   = int(score.max() // 60)
minute = math.floor(score.max() % 60)

print('StandBy:', sb.order[index])
print('FastPass:', fp.order[index])
print('FP Time:', ticket[index])
print(str(hour) + ' hours and ' + str(minute) + ' minutes remain.' )