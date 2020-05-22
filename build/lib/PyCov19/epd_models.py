import numpy as np
from scipy.integrate import solve_ivp

def SIR (t, y, *args):
   N, beta, gamma = args[0], args[1], args[2]
   S, I, R  = y[0]/N, y[1], y[2]

   return [-beta*S*I, beta*S*I-gamma*I, gamma*I]


def SEIR (t, y, *args):
   """
   Succeptable-Exposed-Infected-Recovered model.
   One extra parameter sigma and 
   One extra initial condition for exposed - E0
   """
   N, beta, gamma, sigma =\
      args[0], args[1], args[2], args[3]

   S, E, I, R  = y[0]/N, y[1], y[2], y[3]

   return [-beta*S*I, beta*S*I-sigma*E, sigma*E-gamma*I, gamma*I]

def SIRD (t, y,  *args):

   N, beta,  gamma, delta =\
     args[0], args[1], args[2], args[3]

   S, I, R, D  = y[0]/N, y[1], y[2], y[3]

   return [-beta*S*I, beta*S*I-(gamma+delta) * I, gamma*I, delta * I]


def SEIARD (t, y,  N, beta, sigma, gamma, delta, p):
   """
   Reference : https://arxiv.org/pdf/2004.08288.pdf
   Deafult parameters :

   N, beta, sigma, gamma, delta, p =\
   1000, 0.46, 0.14, 0.01, 0.01, 0.8

   E0, I0, A0, RI0, RA0, D0 =\
   10, 10, 0, 0, 0, 0

   t = np.arange(0, 160, 1)

   """
   S, E, I, A, RI, RA, D =\
     y[0], y[1], y[2], y[3], y[4], y[5], y[6]

   f = (I-A) / (N-D)
 
   dSdt = -beta * S * f
   dEdt =  beta * S * f  - sigma * E
   dIdt = p * sigma * E - (delta + gamma ) * I
   dAdt = (1.0 -p ) * sigma * E - gamma * A
   dRidt = gamma * I
   dRadt = gamma * A
   dDdt  = delta * I

   return  [dSdt, dEdt, dIdt, dAdt, dRidt, dRadt,  dDdt]

