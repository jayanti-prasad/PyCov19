import pandas as pd

def get_tcoeff(epd_model, dF):

   """
   Tranmission coefficients beta, gamma and delta 
   can be directly computed from the time series data.
   Here we do not need reference to any compartmental model.
   """

   df = dF.copy()
   dfc = pd.DataFrame(columns=['date','beta','gamma','delta'])
  
   df['infected'] = df['confirmed'] \
      - df['recovered'] - df['deaths']

   I = df['infected']
   R = df['recovered']
   D = df['deaths']

   dI = I.diff(periods=1).iloc[1:]
   dR = R.diff(periods=1).iloc[1:]
   dD = D.diff(periods=1).iloc[1:]
  
   dfc['beta']  = (dI + dR + dD ) / I

   if epd_model == 'SIR':
      dfc['gamma'] = (dR+dD) / I

   if epd_model == 'SIRD':
      dfc['gamma'] = dR / I
   
   dfc['delta'] = dD / I

   dfc['date'] = df['date'].to_list()
   dfc.index = df['date'].to_list()

   return dfc 


