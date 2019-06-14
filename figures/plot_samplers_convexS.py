import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./style.mplstyle")

f, axs = plt.subplots(nrows=6, ncols=1, figsize=(5,7.5),  sharex=True)

boxstyle = dict(boxstyle='round',fc="w", ec="k")

D=1
b=1
color1 = '#3366CC'
color2 ='dimgrey'
loc_text_x = 0.85
loc_text_y = 0.55

axs_b1q = axs[0]
axs_b1dq = axs[1]
axs_b2q = axs[2]
axs_b2dq = axs[3]
axs_b3q = axs[4]
axs_b3dq = axs[5]

data_q = np.loadtxt('./results/samplers_convexS_b1.txt')
axs_b1q.plot(data_q[:,0],data_q[:,1],color=color1)
axs_b1q.set_ylabel(r"$q(t)$")
axs_b1dq.plot(data_q[:,0],data_q[:,2],color=color1)
axs_b1dq.set_ylabel(r"$\frac{dq(t)}{dt}$")
t = 0.0917517*b*b/D
axs_b1q.axvline(t, linestyle='--', color=color2)
axs_b1dq.axvline(t, linestyle='--', color=color2)
axs_b1q.text(loc_text_x,loc_text_y,r"$b=1$", transform=axs_b1q.transAxes, bbox=boxstyle)
axs_b1dq.text(loc_text_x,loc_text_y,r"$b=1$", transform=axs_b1dq.transAxes, bbox=boxstyle)

data_q = np.loadtxt('./results/samplers_convexS_b2.txt')
b = 2
axs_b2q.plot(data_q[:,0],data_q[:,1],color=color1)
axs_b2q.set_ylabel(r"$q(t)$")
axs_b2dq.plot(data_q[:,0],data_q[:,2],color=color1)
axs_b2dq.set_ylabel(r"$\frac{dq(t)}{dt}$")
t = 0.0917517*b*b/D
axs_b2q.axvline(t, linestyle='--', color=color2)
axs_b2dq.axvline(t, linestyle='--', color=color2)
axs_b2q.text(loc_text_x,loc_text_y,r"$b=2$", transform=axs_b2q.transAxes, bbox=boxstyle)
axs_b2dq.text(loc_text_x,loc_text_y,r"$b=2$", transform=axs_b2dq.transAxes, bbox=boxstyle)

data_q = np.loadtxt('./results/samplers_convexS_b3.txt')
b = 3
axs_b3q.plot(data_q[:,0],data_q[:,1],color=color1)
axs_b3q.set_ylabel(r"$q(t)$")
axs_b3dq.plot(data_q[:,0],data_q[:,2],color=color1)
axs_b3dq.set_ylabel(r"$\frac{dq(t)}{dt}$")
axs_b3dq.set_xlabel(r"$t$")
t = 0.0917517*b*b/D
loc_text_x = 0.05
axs_b3q.axvline(t, linestyle='--', color=color2)
axs_b3dq.axvline(t, linestyle='--', color=color2)
axs_b3q.text(loc_text_x,loc_text_y,r"$b=3$", transform=axs_b3q.transAxes, bbox=boxstyle)
axs_b3dq.text(loc_text_x,loc_text_y,r"$b=3$", transform=axs_b3dq.transAxes, bbox=boxstyle)

plt.savefig('./figures/samplers_convexS.pdf')