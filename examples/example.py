import pandas  as pd
import matplotlib.pyplot as plt
from data_utils import get_country_data
from cov_utils import get_population
from PyCov19.optimizer import Learner 

dF=pd.read_csv("../data/covid-19-global.csv")
df=get_country_data(dF,'Italy')
df['removed'] = df['deaths'] + df['recovered']
df['infected'] = df['confirmed'] - df['removed']
data = df[['infected','removed']].copy()
data = data [data['infected'] > 25]

df_p=pd.read_csv("../data/world_population.csv")
N=get_population('Italy',df_p)

I0 = data.iloc[0]['infected']
R0 = data.iloc[0]['removed']
Y0={'N':N,'I0':I0,'R0':R0}


starting_point = 0.05,0.48,0.01,0.07,1
bounds = [(0.01, 1.0),(0.1, 1.0), (0.01, 1.0), (0.01, 1.0), (0, 100)]

L = Learner ('SIR','exp')
L.initialize  (starting_point, bounds,**Y0)
optm = L.fit(data)

d = L.predict (15)
days=[int(i) for i in range(0, len(data))]


plt.plot(days, data['infected'],'o',label='data')
plt.plot(d.y[1],label='model')
plt.legend()
plt.show()

