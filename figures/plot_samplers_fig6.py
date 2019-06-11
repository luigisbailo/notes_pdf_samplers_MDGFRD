import numpy as np
import matplotlib.pyplot as plt

f, axs = plt.subplots(nrows=4, ncols=2, figsize=(6,8), tight_layout=True, sharex=True, sharey=True)

loc_x = 0.7
loc_y = 0.7
boxstyle = dict(boxstyle='round',fc="w", ec="k")
color1 = '#3366CC'
color2 = '#CC6633'


data = np.loadtxt('./results/samplers_fig6_q.txt')
bar_width = data[1, 0] - data[0, 0]
ax_q1 = axs[0,0]
ax_q100 = axs[0,1]
ax_q1.bar(data[:, 0], data[:, 1], bar_width, color=color2)
ax_q100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color2)
ax_q1.text(loc_x,loc_y,r"$b=1$",transform=ax_q1.transAxes, bbox=boxstyle)
ax_q100.text(loc_x,loc_y,r"$b=100$",transform=ax_q100.transAxes, bbox=boxstyle)
ax_q1.set_ylabel(r'$i^*$')


data = np.loadtxt('./results/samplers_fig6_pt1.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = axs[3,0]
ax_p100 = axs[3,1]
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1$" "\n" r"$t=\frac{b^2}{Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100$" "\n" r"$t=\frac{b^2}{Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')


data = np.loadtxt('./results/samplers_fig6_pt10.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = axs[2,0]
ax_p100 = axs[2,1]
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1$" "\n" r"$t=\frac{b^2}{10Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100$" "\n" r"$t=\frac{b^2}{10Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')


data = np.loadtxt('./results/samplers_fig6_pt100.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = axs[1,0]
ax_p100 = axs[1,1]
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.bar(data[:, 0], data[:, 2], bar_width, label=r"$b=100$", color=color1)
text = r"$b=1$" "\n" r"$t=\frac{b^2}{100Dt}$"
ax_p1.text(loc_x,loc_y,text,transform=ax_p1.transAxes, bbox=boxstyle)
text = r"$b=100$" "\n" r"$t=\frac{b^2}{100Dt}$"
ax_p100.text(loc_x,loc_y,text,transform=ax_p100.transAxes, bbox=boxstyle)
ax_p1.set_ylabel(r'$j^*$')


for ax_i in np.arange (axs.shape[0]):
    for ax_j in np.arange(axs.shape[1]):
        axs[ax_i,ax_j].set_ylim(0,15)


axs[3,0].set_xlabel(r"$\xi$")
axs[3,1].set_xlabel(r"$\xi$")


plt.tight_layout()

plt.savefig('./figures/samplers_fig6.pdf')

