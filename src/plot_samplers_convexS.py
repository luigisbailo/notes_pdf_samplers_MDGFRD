import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use("./style.mplstyle")

fig = plt.figure(figsize=(5,7))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1], hspace=0.25 )
gs0 = gridspec.GridSpecFromSubplotSpec(nrows=4, ncols=1, hspace=0.15, subplot_spec=gs[0])
gs1 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs[1])

boxstyle = dict(boxstyle='round',fc="w", ec="k")

D=1
b=1
color1 = '#3366CC'
color2 ='#CC6633'
loc_text_x = 0.85
loc_text_y = 0.7

axs_b1q = fig.add_subplot(gs0[0])
axs_b1dq = fig.add_subplot(gs0[1])
axs_b2q = fig.add_subplot(gs0[2])
axs_b2dq = fig.add_subplot(gs0[3])


data_q = np.loadtxt('./results/samplers_convexS_b1.txt')
axs_b1q.plot(data_q[:,0],data_q[:,1],color=color1)
axs_b1q.set_ylabel(r"$q_\Omega(\tau)$")
axs_b1dq.plot(data_q[:,0],data_q[:,2],color=color1)
axs_b1dq.set_ylabel(r"$\frac{dq_\Omega(\tau)}{d\tau}$")
t = 0.0917517*b*b/D
axs_b1q.axvline(t, linestyle='--', color=color2)
axs_b1dq.axvline(t, linestyle='--', color=color2)
axs_b1q.text(loc_text_x,loc_text_y,r"$b=1$", transform=axs_b1q.transAxes, bbox=boxstyle)
axs_b1dq.text(loc_text_x,loc_text_y,r"$b=1$", transform=axs_b1dq.transAxes, bbox=boxstyle)
axs_b1dq.set_xticklabels([])
axs_b1q.set_xticklabels([])

data_q = np.loadtxt('./results/samplers_convexS_b2.txt')
b = 2
axs_b2q.plot(data_q[:,0],data_q[:,1],color=color1)
axs_b2q.set_ylabel(r"$q_\Omega(\tau)$")
axs_b2dq.plot(data_q[:,0],data_q[:,2],color=color1)
axs_b2dq.set_ylabel(r"$\frac{dq_\Omega(\tau)}{d\tau}$")
t = 0.0917517*b*b/D
axs_b2q.axvline(t, linestyle='--', color=color2)
axs_b2dq.axvline(t, linestyle='--', color=color2)
axs_b2q.text(loc_text_x,loc_text_y,r"$b=2$", transform=axs_b2q.transAxes, bbox=boxstyle)
axs_b2dq.text(loc_text_x,loc_text_y,r"$b=2$", transform=axs_b2dq.transAxes, bbox=boxstyle)
axs_b2dq.set_xlabel(r"$\tau$")
axs_b2q.set_xticklabels([])

data_q = np.loadtxt('./results/samplers_convexS_all.txt')
b=1
text_loc_x = 0.75
text_loc_y = 0.1
axs_q = fig.add_subplot(gs1[0])
axs_q.plot(data_q[:int(len(data_q)/2), 0], data_q[:int(len(data_q)/2), 1], color='#3366CC')
axs_q.plot(data_q[:int(len(data_q)/2):2, 0], data_q[:int(len(data_q)/2):2, 2], 'x', color='#CC6633',markersize=3)
axs_q.set_xlabel('b')
axs_q.set_ylabel(r"$\tau$")
# axs_q.text(text_loc_x,text_loc_y,s=r"$b=1$",transform=axs_q.transAxes,bbox=boxstyle)


plt.savefig('../figures/samplers_convexS.pdf')