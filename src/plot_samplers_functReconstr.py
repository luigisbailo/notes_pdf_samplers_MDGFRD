import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



f = plt.figure(figsize=(5,7))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3], hspace=0.25 )
gs0 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=1, hspace=0.1, subplot_spec=gs[0])
gs1 = gridspec.GridSpecFromSubplotSpec(nrows=3, ncols=1,  subplot_spec=gs[1])

plt.style.use("./style.mplstyle")

loc_x = 0.6
loc_y = 0.7
boxstyle = dict(boxstyle='round',fc="w", ec="k")
color1 = '#3366CC'
color2 = '#CC6633'
ylim = [0,0.06]
ax_q = f.add_subplot(gs0[0])


data = np.loadtxt('./results/samplers_funcReconstr_q.txt')
bar_width = data[1, 0] - data[0, 0]
# ax_q = axs[0]
ax_q.bar(data[:, 0], data[:, 1], bar_width, color=color2)
ax_q.plot(data[:, 0], data[:, 2], bar_width, color='black', linestyle='--')
ax_q.set_ylim(ylim)

ax_q.set_ylabel(r'$q_\Omega(\tau)$')
ax_q.set_xlabel(r'$\tau$')

loc_text_x = 0.825
loc_text_y = 0.75
ylim = [0,0.05]

ax_p100 = f.add_subplot(gs1[0])
ax_p10 = f.add_subplot(gs1[1])
ax_p1 = f.add_subplot(gs1[2])

data = np.loadtxt('./results/samplers_funcReconstr_pt100.txt')
bar_width = data[1, 0] - data[0, 0]
# ax_p100 = axs[1]
ax_p100.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.plot(data[:, 0], data[:, 2], bar_width, color='black', linestyle='--')
ax_p100.set_ylabel(r'$g_\Omega(r,t)$')
ax_p100.text(loc_text_x,loc_text_y,r"$t=\frac{b^2}{100D}$", transform=ax_p100.transAxes, bbox=boxstyle)
ax_p100.set_xticklabels([])
ax_p100.set_ylim(ylim)

data = np.loadtxt('./results/samplers_funcReconstr_pt10.txt')
bar_width = data[1, 0] - data[0, 0]
# ax_p10 = axs[2]
ax_p10.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p10.plot(data[:, 0], data[:, 2], bar_width, color='black', linestyle='--')
ax_p10.set_ylabel(r'$g_\Omega(r,t)$')
ax_p10.text(loc_text_x,loc_text_y,r"$t=\frac{b^2}{10D}$", transform=ax_p10.transAxes, bbox=boxstyle)
ax_p10.set_xticklabels([])
ax_p10.set_ylim(ylim)

data = np.loadtxt('./results/samplers_funcReconstr_pt1.txt')
bar_width = data[1, 0] - data[0, 0]
# ax_p1 = axs[3]
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p1.plot(data[:, 0], data[:, 2], bar_width, color='black', linestyle='--')
ax_p1.set_ylabel(r'$g_\Omega(r,t)$')
ax_p1.set_xlabel(r'$r$')
ax_p1.text(loc_text_x,loc_text_y,r"$t=\frac{b^2}{D}$", transform=ax_p1.transAxes, bbox=boxstyle)
ax_p1.set_ylim(ylim)

plt.savefig('../figures/samplers_funcReconstr.pdf')
