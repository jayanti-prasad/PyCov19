# PyCov19 - A python package to process Covid-19 data

## Requirments :
-  Scicpy : 1.4.1 + 
-  Numpy : 1.4.1 +


## Instllation 

 > `conda  create --name pycov_env python==3.6`
 > `conda activate pycov_env` 
 > `pip install PyCov19==1.0.1`


## Uses :
 > `python`

 >>> from  PyCov19.epidemiology import Epidemology
 >>> help(Epidemology)

 >>> E = Epidemology ('SIR','exp')
 >>> E.initilization (N=1000,I0=10,R0=0)
 >>> s = E.evolve (160,[0.1,0.24,0.1,0.0,1000])
 >>> type(s.y)
 <class 'numpy.ndarray'>

## For SIR model  
  (t, S(t)) ==  (E.t, s.y[0])
  (t, I(t)) ==  (E.t, s.y[1])
  (t, R(t)) ==  (E.t, s.y[2])

  



