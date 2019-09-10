import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use("./style.mplstyle")

fig = plt.figure(figsize=(5,7))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3], hspace=0.25 )
gs0 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=2, wspace=0.1, subplot_spec=gs[0])
gs1 = gridspec.GridSpecFromSubplotSpec(nrows=3, ncols=2, hspace=0.1, wspace=0.1, subplot_spec=gs[1])

boxstyle = dict(boxstyle='round',fc="w", ec="k")
color1 = '#446280'
color2 = '#CC6633'
yticks = [0,5,10]
ylim = [0,12]

loc_x = 0.15
loc_y = 0.75
data = np.loadtxt('./results/samplers_convergenceNewton_q.txt')
bar_width = data[1, 0] - data[0, 0]
ax_q1 = fig.add_subplot(gs0[0])
ax_q100 = fig.add_subplot(gs0[1])
ax_q1.bar(data[:, 0], data[:, 1], bar_width, color=color2)
ax_q100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color2)
ax_q1.text(loc_x,loc_y,r"$b=1$",transform=ax_q1.transAxes, bbox=boxstyle)
ax_q100.text(loc_x,loc_y,r"$b=100$",transform=ax_q100.transAxes, bbox=boxstyle)
ax_q1.set_ylabel(r'$i^*$')
ax_q100.set_yticklabels([])
ax_q100.set_ylim(ylim)
ax_q1.set_ylim(ylim)
ax_q1.set_xlabel(r'$\xi$')
ax_q100.set_xlabel(r'$\xi$')
ax_q1.set_yticks(yticks)
ax_q100.set_yticks(yticks)


loc_x = 0.1
data = np.loadtxt('./results/samplers_convergenceNewton_pt1.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = fig.add_subplot(gs1[2,0])
ax_p100 = fig.add_subplot(gs1[2,1])
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1$," " " r"$t=\frac{b^2}{Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100,$" " " r"$t=\frac{b^2}{Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')
ax_p100.set_yticklabels([])
ax_p100.set_ylim(ylim)
ax_p1.set_ylim(ylim)
ax_p1.set_xlabel(r'$\xi$')
ax_p100.set_xlabel(r'$\xi$')


data = np.loadtxt('./results/samplers_convergenceNewton_pt10.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = fig.add_subplot(gs1[1,0])
ax_p100 =fig.add_subplot(gs1[1,1])
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1,$" " " r"$t=\frac{b^2}{10Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100,$" " " r"$t=\frac{b^2}{10Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')
ax_p1.set_xticklabels([])
ax_p100.set_xticklabels([])
ax_p100.set_yticklabels([])
ax_p100.set_ylim(ylim)
ax_p1.set_ylim(ylim)

data = np.loadtxt('./results/samplers_convergenceNewton_pt100.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = fig.add_subplot(gs1[0,0])
ax_p100 =fig.add_subplot(gs1[0,1])
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1,$" " " r"$t=\frac{b^2}{100Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100,$" " " r"$t=\frac{b^2}{100Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')
ax_p1.set_xticklabels([])
ax_p100.set_xticklabels([])
ax_p100.set_yticklabels([])
ax_p100.set_ylim(ylim)
ax_p1.set_ylim(ylim)


plt.savefig('../figures/samplers_convergenceNewton.pdf')

