import numpy as np
from scipy.optimize import minimize
from PyCov19.epidemiology import  Epidemology

  
class Learner(object):

    """
    This is the main optimier class which can be used to fit 
    Covid-19 data ('confirmed','recovered','deaths') to a SIR or
    SIRD model with time varying contact rate beta.

    Inputs :
    ======

    L = Learner (epd_model,beta_model)
    L.initialize  (starting_point, bounds,**kwargs)
    optm = L.fit(data)

    Where the input parameters are as follows:
     1) epd_model (str) : SIR or SIRD 
     2) beta_model (str) : exp or tanh 
     3) starting point (tuple) : starting guess for fitting parameters.
        Arguments are positional so you must follow the order 
        gamma, beta_0, alpha, mu, alpha : FOR SIR      
        gamma, delta,  beta_0, alpha, mu, alpha : FOR SIRD      
     4) bounds (list of tuples) : [(p1_min,p1_max), (p2_min, p2_max) ...]
        must follow the order as is given in 3)
     5) kwargs = {'N': population, 'I0': I0, 'R0': R0}  for SIR 
        see example below.
     7) data (pandas data frame) : the columns must match with the initial conditions.
        For example, in case of SIR model:
        Initial conditions : I0, R0
        So the data must have two columns, one for I(t) and another for R(t)
        For the SIRD case : Initial conditions : I0, R0, D0 
        and the data have three columns, for I(t), R(t) and D(t).
     8) We must provide the population of a country for which we want to fit the data.
  

  
     Output:
     ======
        optm.x : parameters 
        optm.fun : loss function 
        you can print the full object for more detail.

        params = L.params 

     Example :
     ========= 
      
        L = Learner ('SIR','exp')
        kwargs = {'N': 6.0E07,'I0': I0, 'R0': R0}
        starting_point = 0.05,0.48,0.01,0.07,1
        bounds = [(0.01, 1.0),(0.1, 1.0), (0.01, 1.0), (0.01, 1.0), (0, 100)]

        L.initialize  (starting_point, bounds,**kwargs)
        optm = L.fit(data)

        params = ["%.6f" % x for x in L.params]

        we can make prediction also 
        ---------------------------- 

        d = L.predict (15)
        L.t = time 
 
       (a)  For SIR 
          d.y[0]  = S
          d.y[1]  = I 
          d.y[2]  = R  
       (b) FOR SIRD  

          d.y[0]  = S
          d.y[1]  = I 
          d.y[2]  = R  
          d.y[3]  = D  

    - Jayanti Prasad, May 29, 2020 
      For more details :  prasad.jayanti@gmail.com 


    """
    def __init__(self, epd_model, beta_model):

        self.epd_model = epd_model   
        self.E = Epidemology(epd_model,beta_model)
  
        self.params = None   

    def initialize  (self,starting_point, bounds,**kwargs):
 
        self.E.initilization(**kwargs)

        self.starting_point = starting_point 

        self.bounds = bounds  
 
    def fit(self, data):
        """
        This is the fitting module and you must chose the parameters carefully. 

        """
        self.data = data  
        options={'disp': None, 'maxcor': 10,\
                'ftol': 1.0e-09,\
                'gtol': 1e-06, 'eps': 1e-08,\
                'maxfun': 2500, 'maxiter': 2500,\
                'iprint': -1, 'maxls': 20}

        optimal = minimize(self.loss, self.starting_point,\
            method='L-BFGS-B', bounds=self.bounds,options=options)

        self.params = list(optimal.x) 

        return optimal 

    def loss (self, point):

        params = list(point)

        solution = self.E.evolve(self.data.shape[0], params)

        y_true = self.data.to_numpy()
        y_pred = solution.y[1:,:].transpose() 

        y_mean = y_true.mean (axis=0)
        weight = 1.0 - y_mean / np.sum(y_mean)

        res = weight *  (y_pred - y_true)

        rmsd = np.sqrt(np.mean(res**2)) 
        
        return rmsd 
        

    def predict (self, num_days):
        return  self.E.evolve (self.data.shape[0] + num_days, self.params)
         
