import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temp=ctrl.Antecedent(np.arange(30,101,1),'temp')
load=ctrl.Antecedent(np.arange(0,101,1),'load')
fan=ctrl.Consequent(np.arange(0,101,1),'fan')

temp['cool']=fuzz.trimf(temp.universe,[30,30,55])
temp['warm']=fuzz.trimf(temp.universe,[45,65,85])
temp['hot']=fuzz.trimf(temp.universe,[75,100,100])

load['low']=fuzz.trimf(load.universe,[0,0,40])
load['medium']=fuzz.trimf(load.universe,[20,50,80])
load['high']=fuzz.trimf(load.universe,[60,100,100])

fan['low']=fuzz.trimf(fan.universe,[0,0,40])
fan['medium']=fuzz.trimf(fan.universe,[20,50,80])
fan['high']=fuzz.trimf(fan.universe,[60,100,100])

rules=[
    ctrl.Rule(temp['cool']&load['low'],fan['low']),
    ctrl.Rule(temp['cool']&load['medium'],fan['low']),
    ctrl.Rule(temp['cool']&load['high'],fan['medium']),
    ctrl.Rule(temp['warm']&load['low'],fan['low']),
    ctrl.Rule(temp['warm']&load['medium'],fan['medium']),
    ctrl.Rule(temp['warm']&load['high'],fan['high']),
    ctrl.Rule(temp['hot']&load['low'],fan['medium']),
    ctrl.Rule(temp['hot']&load['medium'],fan['high']),
    ctrl.Rule(temp['hot']&load['high'],fan['high']),
]

sim=ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))
sim.input['temp']=78
sim.input['load']=85
sim.compute()

sim.print_state()
print(f"\n\tFan speed for {78}°C temp & {85}% load: {sim.output['fan']:.2f}%")

temp.view(sim=sim)
load.view(sim=sim)
fan.view(sim=sim)
plt.show()