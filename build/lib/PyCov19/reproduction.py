from PyCov19.beta_models import  exp, tanh

def reproduction_number (beta_model, epd_model, **kwargs):

   # must have the following 
   # model, beta_0, alpha, mu, tau, tl 
   
   for k in kwargs:
      try:
         kwargs[k] = float(kwargs[k])
      except:
         pass 

   beta = eval(beta_model) (kwargs['num_days'], **kwargs)

   if epd_model == 'SIR':
      R  = beta/ kwargs['gamma'] 

   if epd_model == 'SIRD':
      R  = beta/ (kwargs ['gamma'] + kwargs ['delta']) 

   return R 


