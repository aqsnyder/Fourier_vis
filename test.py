import numpy as np
import matplotlib.pyplot as plot

orbitperiod = .36
lumorbitperiod = 3.25
synodicperiod = 1/abs((1/orbitperiod)-(1/lumorbitperiod))
highesthigh = 3112
lowesthigh = 2709
highestlow = 2023
lowestlow = 1665
halfofhighrange = abs(highesthigh-highestlow)/2
halfoflowrange = abs(highestlow-lowestlow)/2
lowmean = (highestlow+lowestlow)/2

time = np.arange(0, 2, 0.01) ;

sine_one = np.sin(time*np.pi*2 / orbitperiod)*halfoflowrange+lowmean
plot.plot(time * 365, sine_one, label='first Sine')

sine_two = np.sin(time*np.pi*2 / synodicperiod)*halfofhighrange+halfofhighrange
plot.plot(time * 365, sine_two, label='Second Sine')

sine_sum = sine_one + sine_two
plot.plot(time * 365 , sine_sum, label='Summed Sines')
plot.legend(); plot.show()