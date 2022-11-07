import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0, 4, 0.01) ;

sine_one = np.sin(time*np.pi*3)
plot.scatter(time * 365, sine_one, label='first Sine', s=1)

sine_two = np.sin(time*np.pi*2)
plot.scatter(time * 365, sine_two, label='Second Sine', s=1)

sine_sum = sine_one + sine_two
plot.plot(time * 365 , sine_sum, label='Summed Sines')

plot.legend()
plot.show()