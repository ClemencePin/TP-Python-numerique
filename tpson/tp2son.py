import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio,display
from scipy.io import wavfile

f = 440 #hertz
temps = np.linspace(0,1,1000)
tab = np.sin(2*np.pi*f*temps)

plt.plot(temps,tab)
plt.show()
display(Audio(tab,f))