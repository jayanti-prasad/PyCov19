import numpy as np
from scipy.integrate import solve_ivp

def SIR (t, y, **kwargs):
   """
   Three compartment SIR Model  
   """

   N, beta, gamma = \
      kwargs['N'], kwargs['beta'], kwargs['gamma']

   S, I, R  = y[0]/N, y[1], y[2]

   return [-beta*S*I, beta*S*I-gamma*I, gamma*I]


def SEIR (t, y, **kwargs):
   """
   Succeptable-Exposed-Infected-Recovered model.
   One extra parameter sigma and 
   One extra initial condition for exposed - E0
   """
   N, beta, gamma, sigma =\
       kwargs['N'], kwargs['beta'], kwargs['gamma'], kwargs['sigma']

   S, E, I, R  = y[0]/N, y[1], y[2], y[3]

   return [-beta*S*I, beta*S*I-sigma*E, sigma*E-gamma*I, gamma*I]

def SIRD (t, y,  **kwargs):

   N, beta,  gamma, delta =\
       kwargs['N'], kwargs['beta'], kwargs['gamma'], kwargs['delta']

   S, I, R, D  = y[0]/N, y[1], y[2], y[3]

   return [-beta*S*I, beta*S*I-(gamma+delta) * I, gamma*I, delta * I]

