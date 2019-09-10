import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


plt.style.use("./style.mplstyle")

fig = plt.figure(figsize=(5,7))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3], hspace=0.25 )
gs0 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=2, wspace=0.1, subplot_spec=gs[0])
gs1 = gridspec.GridSpecFromSubplotSpec(nrows=3, ncols=2, hspace=0.1, wspace=0.1, subplot_spec=gs[1])

loc_x = 0.1
loc_y = 0.75
boxstyle = dict(boxstyle='round',fc="w", ec="k")
yticks = [0,10,20,30]
ylim = [0,37]


data_qS = np.loadtxt('./results/samplers_convergenceSeries_qS.txt')
bar_width = data_qS[1, 0] - data_qS[0, 0]
ax_q = fig.add_subplot(gs0[0])
ax_s = fig.add_subplot(gs0[1])
ax_q.bar(data_qS[:, 0], data_qS[:, 1], bar_width, label=r"$q(t)$", color='#CC6633')
ax_s.bar(data_qS[:, 0], data_qS[:, 2], bar_width, label=r"$S(t)$", color='#CC6633')
ax_q.legend(loc=(loc_x,loc_y))
ax_s.legend(loc=(loc_x,loc_y))
ax_q.set_xlabel(r'$t$')
ax_s.set_xlabel(r'$t$')
ax_q.set_ylabel(r'$n^*$')
ax_q.set_yticks(yticks)
ax_s.set_yticks(yticks)
ax_q.set_ylim(ylim)
ax_s.set_ylim(ylim)
ax_s.set_yticklabels([])


loc_y = 0.67
data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t1.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = fig.add_subplot(gs1[0,0])
ax_P =fig.add_subplot(gs1[0,1])
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p_\Omega(r,t),\thinspace t=\frac{b^2}{D}$", color='#446280')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P_\Omega(r,t),\thinspace t=\frac{b^2}{D}$", color='#446280')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_ylabel(r'$m^*$')
ax_p.set_xticklabels([])
ax_P.set_xticklabels([])
ax_P.set_yticklabels([])
ax_P.set_ylim(ylim)
ax_p.set_ylim(ylim)
ax_p.set_yticks(yticks)
ax_P.set_yticks(yticks)

data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t10.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = fig.add_subplot(gs1[1,0])
ax_P =fig.add_subplot(gs1[1,1])
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p_\Omega(r,t),\thinspace t=\frac{b^2}{10*D}$", color='#446280')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P_\Omega(r,t),\thinspace t=\frac{b^2}{10*D}$", color='#446280')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_xlabel('r')
ax_P.set_xlabel('r')
ax_p.set_ylabel(r'$m^*$')
ax_p.set_xticklabels([])
ax_P.set_xticklabels([])
ax_P.set_yticklabels([])
ax_P.set_ylim(ylim)
ax_p.set_ylim(ylim)
ax_p.set_yticks(yticks)
ax_P.set_yticks(yticks)

data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t100.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = fig.add_subplot(gs1[2,0])
ax_P = fig.add_subplot(gs1[2,1])
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p_\Omega(r,t),\thinspace t=\frac{b^2}{100*D}$", color='#446280')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P_\Omega(r,t),\thinspace t=\frac{b^2}{100*D}$", color='#446280')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_ylabel(r'$j^*$')
ax_P.set_yticklabels([])
ax_P.set_ylim(ylim)
ax_p.set_ylim(ylim)
ax_p.set_xlabel(r'$r$')
ax_P.set_xlabel(r'$r$')
ax_p.set_yticks(yticks)
ax_P.set_yticks(yticks)

plt.savefig('../figures/samplers_convergenceSeries.pdf')
