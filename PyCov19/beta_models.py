import numpy as np
import matplotlib.pyplot as plt 

def polynom (t, **kargs):
   # Loli-2020, 0.0 < alpha < 1    

   if t < kargs['tl'] :
      beta_t = kargs['beta_0'] 
   else :
      beta_t = kargs['beta_0'] * (1.0 - kargs['alpha'] * kargs['mu'] * (t-kargs['tl'])/t)
   return beta_t


def exp(t, **kargs):
   # Fanelli-2020

   if t  < kargs['tl']  :
      beta_t = kargs['beta_0']
   else :
      beta_t = kargs['beta_0'] *  ((1.0 -  kargs['alpha']) \
         * np.exp (-kargs['mu'] * (t - kargs['tl']) ) \
         + kargs['alpha'])
   return beta_t


def tanh (t, **kargs):
   # Goswami-2020
   if t  < kargs['tl'] :
      beta_t = kargs['beta_0']
   else :
      beta_t = kargs['beta_0'] * (1.0 -  kargs['alpha'] \
         * np.tanh (kargs['mu'] *  (t- kargs['tl'])))
   return beta_t


if __name__ == "__main__":

   t = np.linspace (1,100,100)

   y_line = [polynom (a, beta_0= 0.14,alpha=0.75,mu=0.75,tl=10) for a in t]
   y_exp  = [exp (a, beta_0= 0.14,alpha=0.15,mu=0.1,tl=10) for a in t]
   y_tanh = [tanh (a, beta_0= 0.14,alpha=0.85,mu=0.1,tl=10) for a in t]

   plt.plot(t, y_line,label='polynom')
   plt.plot(t, y_exp, label='exp')
   plt.plot(t, y_tanh, label='tanh')
   plt.legend()

   plt.show()


