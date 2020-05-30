# PyCov19 - A python package to process Covid-19 data

## Requirments :
-  Scicpy : 1.4.1 + 
-  Numpy : 1.4.1 +


## Instllation 

### With pip 

 `> conda  create --name pycov_env python==3.6`

 `> conda activate pycov_env` 

 `> pip install -i https://test.pypi.org/simple/ PyCov19==1.0.1`

### Without pip 

  `cd PATHTOPYCOV`

  `export PYTHONPATH=PATHTOPYCOC:$PYTHONPATH`

  `cd examples`   


## Uses 1 : Models:
 `> python`

 `>>> from  PyCov19.epidemiology import Epidemology`

 `>>> help(Epidemology)`

 `>>> E = Epidemology ('SIR','exp')`

 `>>> E.initilization (N=1000,I0=10,R0=0)`

 `>>> s = E.evolve (160,[0.1,0.24,0.1,0.0,1000])`

 `>>> type(s.y)`

 `<class 'numpy.ndarray'>`

### For SIR model  

  (t, S(t)) ==  (E.t, s.y[0])

  (t, I(t)) ==  (E.t, s.y[1])

  (t, R(t)) ==  (E.t, s.y[2])

## Use 2 : Optimization   

  - see [Example](https://github.com/jayanti-prasad/PyCov19/blob/master/examples/example.py)

