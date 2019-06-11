import numpy as np
import matplotlib.pyplot as plt


plt.style.use("./style.mplstyle")

f, axs = plt.subplots(nrows=4, ncols=1, figsize=(5,7),  sharex=True)

boxstyle = dict(boxstyle='round',fc="w", ec="k")

D=1
b=1
color1 = '#3366CC'
color2 = color='#CC6633'
loc_text_x = 0.8
loc_text_y = 0.75
data_q = np.loadtxt('./results/samplers_fig4_q_b1.txt')
axs[0].plot(data_q[:,0],data_q[:,1],color=color1)
axs[0].set_ylabel(r"$q(t)$")
axs[1].plot(data_q[:,0],data_q[:,2],color=color1)
axs[1].set_ylabel(r"$\frac{dq(t)}{dt}$")
t = 0.0917517*b*b/D;
axs[0].axvline(t, color=color2)
axs[1].axvline(t, color=color2)
axs[0].text(loc_text_x,loc_text_y,"b=1", transform=axs[0].transAxes, bbox=boxstyle)
axs[1].text(loc_text_x,loc_text_y,"b=1", transform=axs[1].transAxes, bbox=boxstyle)

data_q = np.loadtxt('./results/samplers_fig4_q_b2.txt')
b = 2
axs[2].plot(data_q[:,0],data_q[:,1],color=color1)
axs[2].set_ylabel(r"$q(t)$")
axs[3].plot(data_q[:,0],data_q[:,2],color=color1)
axs[3].set_ylabel(r"$\frac{dq(t)}{dt}$")
axs[3].set_xlabel(r"$t$")
t = 0.0917517*b*b/D;
axs[2].axvline(t, color=color2)
axs[3].axvline(t, color=color2)
axs[2].text(loc_text_x,loc_text_y,"b=2", transform=axs[2].transAxes, bbox=boxstyle)
axs[3].text(loc_text_x,loc_text_y,"b=2", transform=axs[3].transAxes, bbox=boxstyle)

plt.savefig('./figures/samplers_fig4.pdf')