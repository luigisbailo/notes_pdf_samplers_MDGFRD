import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./style.mplstyle")

fig = plt.figure(figsize=(5,3))
data = np.loadtxt('./results/samplers_comparisonPfree.txt')
boxstyle = dict(boxstyle='round',fc="w", ec="k")

plt.plot (data[:,0],data[:,1], color='#CC6633', label=r"$g_{\Omega}(r,t),\quad t=\frac{b^2}{100D}$")
plt.plot (data[::20,0],data[::20,2], 'x', color='#CC6633', label=r"$p_{free}(r,t),\quad t=\frac{b^2}{100D}$" )
plt.plot (data[:,0],data[:,3], color='#3366CC', label=r"$g_{\Omega}(r,t),\quad t=\frac{b^2}{10D}$")
plt.plot (data[::20,0],data[::20,4], 'x', color='#3366CC', label=r"$p_{free}(r,t),\quad t=\frac{b^2}{10D}$" )

plt.xlabel ("r")
plt.ylabel ('p(r)')
plt.legend (loc=1,)
plt.tight_layout()
plt.savefig ('../figures/samplers_comparisonPfree.pdf')
