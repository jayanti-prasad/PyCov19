import numpy as np
from scipy.integrate import solve_ivp

class EpdModels:
   def __init__(self, epd_model, beta_model):
       self.epd_model = epd_model
       self.beta_model = beta_model 

   def model (self, t, y, *args):

       if self.epd_model.__name__=='SIR':
           start = 2
           N, gamma = args[0], args[1]

       if self.epd_model.__name__=='SIRD':
           start = 3
           N, gamma, delta = args[0], args[1], args[2] 

       [beta_0, alpha, mu, tl] = [args[start+i] for i in range(0,4)]

       beta = self.beta_model (t, beta_0=beta_0, alpha=alpha,mu=mu, tl=tl)  
        
       if self.epd_model.__name__=='SIR':
          return self.epd_model (t, y, N, beta, gamma)
       if self.epd_model.__name__=='SIRD':
          return self.epd_model (t, y, N, beta, gamma, delta)


class Epidemology:
    def __init__(self, ode_solver, epd_model, beta_model):
        self.ods_solver = ode_solver 
        self.eps_model  = epd_model 
        self.beta_model = beta_model 
        self.t = None 
        self.E = EpdModels (epd_model, beta_model)

        self.func = self.E.model 

    def set_init (self, **kwargs):
        self.N = kwargs['N']
        self.Y0 = kwargs['Y0'] 
 

    def evolve (self, size, params):
        self.t = np.arange(0, size, 1)
        """
        This is the main evolution mthod.
        > evolve (beta, gamma) : for SIR 
        > evolve (beta, sigma, gamma) : for SEIR 
        """
        params.insert(0, self.N) 
        
        S0 =  [self.N - np.sum (self.Y0)]
        Y0 = tuple (S0 + list(self.Y0))  

        solution = solve_ivp(self.func, [0, size], Y0,\
            t_eval = self.t,vectorized=True, args=params)

        return solution

