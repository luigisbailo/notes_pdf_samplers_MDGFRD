import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use("./style.mplstyle")

fig = plt.figure(figsize=(5,7))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1], hspace=0.25 )
gs0 = gridspec.GridSpecFromSubplotSpec(nrows=4, ncols=1, hspace=0.15, subplot_spec=gs[0])
gs1 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=2, wspace=0.15, subplot_spec=gs[1])


boxstyle = dict(boxstyle='round',fc="w", ec="k")
color1 = '#446280'
color2 ='#CC6633'
loc_text_x = 0.815
loc_text_y = 0.65
D=1

data_p = np.loadtxt('./results/samplers_convexP_b1t100.txt')
b = 1
t = b*b/D/100
axs_p_b1t100 =  fig.add_subplot(gs0[0])
axs_dp_b1t100 = fig.add_subplot(gs0[1])
axs_p_b1t100.plot(data_p[:,0],data_p[:,1],color=color1)
axs_p_b1t100.set_ylabel(r"$g_\Omega(r,t)$")
axs_dp_b1t100.plot(data_p[:,0],data_p[:,2],color=color1)
axs_dp_b1t100.set_ylabel(r"$\frac{\partial g_\Omega(r,t)}{\partial r}$")
r = np.sqrt(t*D)*2
axs_p_b1t100.axvline(r, linestyle='--', color=color2)
axs_dp_b1t100.axvline(r, linestyle='--', color=color2)
text = r"$t=\frac{b^2}{100\thinspace Dt}$"
axs_p_b1t100.text(loc_text_x,loc_text_y, text, transform=axs_p_b1t100.transAxes, bbox=boxstyle)
axs_dp_b1t100.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t100.transAxes, bbox=boxstyle)
axs_p_b1t100.set_xticklabels([])
axs_dp_b1t100.set_xticklabels([])

data_p = np.loadtxt('./results/samplers_convexP_b1t1.txt')
b = 1
t = b*b/D
loc_text_x = 0.87

axs_p_b1t1 =fig.add_subplot(gs0[2])
axs_dp_b1t1 = fig.add_subplot(gs0[3])
axs_p_b1t1.plot(data_p[:,0],data_p[:,1], color=color1)
axs_p_b1t1.set_ylabel(r"$g_\Omega(r,t)$")
axs_dp_b1t1.plot(data_p[:,0],data_p[:,2], color=color1)
axs_dp_b1t1.set_ylabel(r"$\frac{\partial g_\Omega(r,t)}{\partial r}$")
axs_dp_b1t1.set_xlabel(r"$r$")
r = 0.646*b
axs_p_b1t1.axvline(r, linestyle='--', color=color2)
axs_dp_b1t1.axvline(r, linestyle='--', color=color2)
text = r"$t=\frac{b^2}{Dt}$"
axs_dp_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t1.transAxes, bbox=boxstyle)
axs_p_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_p_b1t1.transAxes, bbox=boxstyle)
axs_p_b1t1.set_xticklabels([])

data_q_b1 = np.loadtxt('./results/samplers_convexP_b1all.txt')
b=1
text_loc_x = 0.75
text_loc_y = 0.1
axs_q_b1 = fig.add_subplot(gs1[0])
axs_q_b1.axvline(0.063*b*b/D, color='grey',linestyle='--')
axs_q_b1.axvline(0.234*b*b/D, color='grey',linestyle='--')
axs_q_b1.plot(data_q_b1[:int(len(data_q_b1)/2), 0], data_q_b1[:int(len(data_q_b1)/2), 1], color=color1)
axs_q_b1.plot(data_q_b1[:int(len(data_q_b1)/2):2, 0], data_q_b1[:int(len(data_q_b1)/2):2, 2], 'x', color=color2,markersize=3)
axs_q_b1.set_xlabel('t')
axs_q_b1.set_ylabel('r')
axs_q_b1.text(text_loc_x,text_loc_y,s=r"$b=1$",transform=axs_q_b1.transAxes,bbox=boxstyle)

b=10
text_loc_x = 0.7
data_q_b10 = np.loadtxt('./results/samplers_convexP_b10all.txt')
axs_q_b10 = fig.add_subplot(gs1[1])
axs_q_b10.axvline(0.063*b*b/D,color='grey',linestyle='--')
axs_q_b10.axvline(0.234*b*b/D,color='grey',linestyle='--')
axs_q_b10.plot(data_q_b10[:int(len(data_q_b10)/2), 0], data_q_b10[:int(len(data_q_b10)/2), 1], color=color1)
axs_q_b10.plot(data_q_b10[:int(len(data_q_b10)/2):2, 0], data_q_b10[:int(len(data_q_b10)/2):2, 2], 'x', color=color2,markersize=3)
axs_q_b10.set_xlabel('t')
axs_q_b10.text(text_loc_x,text_loc_y,s=r"$b=10$",transform=axs_q_b10.transAxes,bbox=boxstyle)

plt.savefig('../figures/samplers_convexP.pdf')


