import matplotlib.pyplot as plt 
from  PyCov19.epidemiology import Epidemology  
import argparse  

if __name__ == "__main__":

   parser = argparse.ArgumentParser()
   parser.add_argument('-m','--epd-model',help='Epidemiologcal model',default='SIR')
   parser.add_argument('-b','--beta-model',help='Beta model',default='exp')

   args = parser.parse_args()
 
   E = Epidemology (args.epd_model,args.beta_model)

   if args.epd_model == 'SIR':
      E.initilization (N=1000,I0=10,R0=0)
      #s = E.evolve (size,[gamma,beta_0,alpha,mu,tl=1000]
      s = E.evolve (160, [0.1,0.24,0.0,0.0,1000])
      plt.title('SIR Model')
      plt.plot(s.t, s.y[0],c='b',label='Suceptible')
      plt.plot(s.t, s.y[1],c='r',label='Infected')
      plt.plot(s.t, s.y[2],c='g',label='Recovered')
 
   if args.epd_model == 'SIRD':
      E.initilization (N=1000,I0=10,R0=0,D0=1)
      #s = E.evolve (size,[gamma,delta,beta_0,alpha,mu,tl=1000]
      s = E.evolve (160, [0.1,0.01,0.24,0.0,0.0,1000])

      plt.title('SIRD Model')
      plt.plot(s.t, s.y[0],c='b',label='Suceptible')
      plt.plot(s.t, s.y[1],c='r',label='Infected')
      plt.plot(s.t, s.y[2],c='g',label='Recovered')
      plt.plot(s.t, s.y[3],c='K',label='DEAD')


   
   if args.epd_model == 'SEIR':
      E.initilization (N=1000,E0=10,I0=1,R0=0)
      s = E.evolve (160,[0.1,0.05,0.4,0.0,0.0,1000])
      #s = E.evolve (size=160, gamma=0.1,sigma=0.05, beta_0=0.4,alpha=0.0,mu=0.0,tl=1000)

      plt.title('SEIR Model')
      plt.plot(s.t, s.y[0],c='b',label='Suceptible')
      plt.plot(s.t, s.y[1],c='r',label='Exposed')
      plt.plot(s.t, s.y[2],c='g',label='Infected')
      plt.plot(s.t, s.y[3],c='K',label='Recovered')

   plt.legend()

   plt.show ()

