import matplotlib.pyplot as plt
from  PyCov19.optimizer import Learner 
from common_utils import get_country_data 
from cov_utils import get_population
import argparse
import pandas as pd
import matplotlib.pyplot as plt 


if __name__ == "__main__":

   parser = argparse.ArgumentParser()
   parser.add_argument('-i','--input-file',help='Input file',default='../data/covid-19-global.csv')
   parser.add_argument('-p','--population-file',help='Input file',default='../data/world_population.csv')
   parser.add_argument('-c','--country-name',help='Country name',default='Italy')
   parser.add_argument('-m','--epd-model',help='Epidemiologcal model',default='SIR')
   parser.add_argument('-b','--beta-model',help='Beta model',default='exp')

   args = parser.parse_args()

   dF = pd.read_csv(args.input_file)

   df = get_country_data (dF, args.country_name)

   df['removed'] = df['recovered'] + df['deaths']
   df['infected'] = df['confirmed'] - df['removed']
   df.index = df['date'].to_list()

   data = df[['infected','removed']].copy()
   data = data [data['infected'] > 25]

   days = [int(i) for i in range (0, data.shape[0])]  

   I0,R0  = data.iloc[0]['infected'], data.iloc[0]['removed']

   L = Learner (args.epd_model,beta_model=args.beta_model)

   kwargs = {'N': 6.0E07,'I0': I0, 'R0': R0}
   starting_point = 0.05,0.48,0.01,0.07,1
   bounds = [(0.01, 1.0),(0.1, 1.0), (0.01, 1.0), (0.01, 1.0), (0, 100)]

   L.initialize  (starting_point, bounds,**kwargs)

   optm = L.fit(data)

   params = ["%.6f" % x for x in L.params]

   y = L.predict (15)

   print("params [gamma,beta_0,alpha,mu,tl]:",params,"loss=","%.3f" % optm.fun)
   print(optm)

   plt.plot(y.t, y.y[1],c='b')
   plt.plot (days, data['infected'].to_list(),'o',c='b')
   plt.plot(y.t, y.y[2],c='r')
   plt.plot (days, data['removed'].to_list(),'o',c='r')

   plt.yscale('log')
   plt.show()


