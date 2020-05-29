import numpy as np
from scipy.integrate import solve_ivp
from PyCov19.beta_models import exp, tanh 
from PyCov19.epd_models import SIR, SIRD, SEIR 

class Epidemology:

   """
   This is a wraper program which is used to solve compartmental models
   (SIR, SIRD and SEIR) for time varying contact rate beta, parameterized
   by a set of four parameters - beta_0, alpha, mu and tl.
   For more detail see the paper : 
     https://www.medrxiv.org/content/10.1101/2020.05.22.20110171v1 

   Example : 
     E = Epidemology ('SIR','exp')

     E.initilization (N=1000,I0=10,R0=0)
     #s = E.evolve (size,[gamma,beta_0,alpha,mu,tl])
     s = E.evolve (160,[0.1,0.24,0.1,0.0,1000])


     outputs: 
        s.t = t 
        s.y[0] = S(t)
        s.y[1] = I(t)
        s.y[2] = R(t)
    
   """

   def __init__(self, epd_model, beta_model=None):

      self.epd_model = epd_model
      self.model = eval (epd_model)
      self.beta_model = beta_model 


   def initilization (self, **kwargs):

      try:
         self.N = kwargs['N']
         I0 = kwargs['I0']
         R0 = kwargs['R0']
 
         if self.epd_model == 'SIR':
             S0 = self.N - I0 -  R0
             self.Y0 = [S0, I0, R0]

         if self.epd_model == 'SIRD':
             D0 = kwargs['D0']
             S0 = self.N - D0 - I0 - R0
             self.Y0 = [S0, I0, R0, D0]
 
         if self.epd_model == 'SEIR':
             E0 = kwargs['E0']
             S0 =  self.N - I0 - R0 - E0  
             self.Y0 = [S0, E0, I0, R0]
    
      except:
         print("You must give valid initial conditions")  
         print(kwargs)
         return 

   def func (self, t, y, *args):

       P = {'N': self.N,  'gamma': args[0]}
       start = 1

       if self.epd_model == 'SIRD':
           P ['delta'] = args[1]
           start += 1
        
       if self.epd_model == 'SEIR':
           P['sigma'] = args[0]
           P['gamma'] = args[1]
           start += 1
       
       if self.beta_model :
          [beta_0, alpha, mu, tl] = [args[i] for i in range(start, len(args))]
          P['beta'] = eval(self.beta_model) (t, beta_0=beta_0, alpha=alpha,mu=mu, tl=tl)
       else :
          P['beta'] = args[start]
  
       return self.model (t, y, **P)


   def evolve (self, size, args):

      self.t = np.arange(0, size, 1)
      
      sol = solve_ivp(self.func,  [0, size], tuple(self.Y0),\
         t_eval = self.t,vectorized=True, args=args)
 
      return sol 
 
