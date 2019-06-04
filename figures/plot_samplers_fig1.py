import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./results/samplers_fig1.txt')

plt.plot (data[:,0],data[:,1], label=r"$t=\frac{b^2}{100D}$")
# pl.plot (data[:,0],data[:,2], 'bx')
# pl.plot (data[:,0],data[:,3],'g', label=r'$t=\frac{b^2}{10D}$' )
# pl.plot (data[:,0],data[:,4], 'gx')

plt.xlabel ("r")
plt.ylabel ('p(r)')
plt.legend (loc=1)
plt.savefig ('./figures/samplers_fig1.pdf')
