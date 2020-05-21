import numpy as np
from scipy.optimize import minimize
from PyCov19.epidemiology import  Epidemology

  
class Learner(object):
    """
    This is the main optimier class
    """
    def __init__(self, epd_model, beta_model):

        self.epd_model = epd_model   
        self.E = Epidemology('ode_solver', epd_model, beta_model)
  
        self.params = None   

    def initialize  (self,starting_point, bounds,**kwargs):
 
        self.E.set_init (N=kwargs['N'],Y0=kwargs['Y0'])

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
        epd_model = self.epd_model.__name__           

        X = list(point)
        solution = self.E.evolve(self.data.shape[0], X)

        y_true = self.data.to_numpy()
        y_pred = solution.y[1:,:].transpose() 

        y_mean = y_true.mean (axis=0)
        weight = 1.0 - y_mean / np.sum(y_mean)

        res = weight *  (y_pred - y_true)

        rmsd = np.sqrt(np.mean(res**2)) 
        
        return rmsd 
        

    def predict (self, num_days):
        return  self.E.evolve (self.data.shape[0] + num_days, self.params)
         

