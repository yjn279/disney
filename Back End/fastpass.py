import random
import copy
import numpy as np
import pandas as pd
from route import Route

class FastPass(Route):

     def calculate_fastpass(self):

        time_loss  = np.full(len(self.order), self.time_open)
        ticket     = self.order.copy()

        for i in range(len(self.request)):
            t            = time_loss.reshape(-1,1)
            index        = np.argmax(np.where(self.index<=t,self.index,0), axis=1)
            ticket[:, i] = self.time[self.order[:,i], index]
            time_loss    = np.where((ticket[:,i]-time_loss>=120)|(ticket[:,i]==0), time_loss+120, ticket[:,i])
            time_loss    = np.where(ticket[:,i]==0, time_loss-120, time_loss)
        return ticket