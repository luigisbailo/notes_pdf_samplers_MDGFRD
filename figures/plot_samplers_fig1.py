import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./results/samplers_fig1.txt')

plt.plot (data[:,0],data[:,1], color='#CC6633', label=r"$g_{\Omega}(r,t|0,0),\quad t=\frac{b^2}{100D}$")
plt.plot (data[::20,0],data[::20,2], 'x', color='#CC6633', label=r"$p_{free}(r,t|0,0),\quad t=\frac{b^2}{100D}$" )
plt.plot (data[:,0],data[:,3], color='#3366CC', label=r"$g_{\Omega}(r,t|0,0),\quad t=\frac{b^2}{100D}$")
plt.plot (data[::20,0],data[::20,4], 'x', color='#3366CC', label=r"$p_{free}(r,t|0,0),\quad t=\frac{b^2}{100D}$" )


plt.xlabel ("r")
plt.ylabel ('p(r)')
plt.legend (loc=1)
plt.savefig ('./figures/samplers_fig1.pdf')
