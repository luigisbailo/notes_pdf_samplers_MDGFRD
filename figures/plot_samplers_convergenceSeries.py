import numpy as np
import matplotlib.pyplot as plt

f, axs = plt.subplots(nrows=4, ncols=2, figsize=(6,8), tight_layout=True)

loc_x = 0.6
loc_y = 0.7

data_qS = np.loadtxt('./results/samplers_convergenceSeries_qS.txt')
bar_width = data_qS[1, 0] - data_qS[0, 0]
ax_q = axs[0,0]
ax_s = axs[0,1]
ax_q.bar(data_qS[:, 0], data_qS[:, 1], bar_width, label=r"$q(t)$", color='#CC6633')
ax_s.bar(data_qS[:, 0], data_qS[:, 2], bar_width, label=r"$S(t)$", color='#CC6633')
ax_q.legend(loc=(loc_x,loc_y))
ax_s.legend(loc=(loc_x,loc_y))
ax_q.set_xlabel('t')
ax_s.set_xlabel('t')
ax_q.set_ylabel(r'$n^*$')
ax_s.set_ylabel(r'$n^*$')

loc_x = 0.25
loc_y = 0.7

data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t1.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = axs[1,0]
ax_P = axs[1,1]
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p(r,t),\thinspace t=\frac{b^2}{D}$", color='#3366CC')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P(r,t),\thinspace t=\frac{b^2}{D}$", color='#3366CC')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_xlabel('r')
ax_P.set_xlabel('r')
ax_p.set_ylabel(r'$m^*$')
ax_P.set_ylabel(r'$m^*$')


data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t10.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = axs[2,0]
ax_P = axs[2,1]
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p(r,t),\thinspace t=\frac{b^2}{10*D}$", color='#3366CC')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P(r,t),\thinspace t=\frac{b^2}{10*D}$", color='#3366CC')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_xlabel('r')
ax_P.set_xlabel('r')
ax_p.set_ylabel(r'$m^*$')
ax_P.set_ylabel(r'$m^*$')


data_pP = np.loadtxt('./results/samplers_convergenceSeries_pP_t100.txt')
bar_width = data_pP[1, 0] - data_pP[0, 0]
ax_p = axs[3,0]
ax_P = axs[3,1]
ax_p.bar(data_pP[:, 0], data_pP[:, 1], bar_width, label=r"$p(r,t),\thinspace t=\frac{b^2}{100*D}$", color='#3366CC')
ax_P.bar(data_pP[:, 0], data_pP[:, 2], bar_width, label=r"$P(r,t),\thinspace t=\frac{b^2}{100*D}$", color='#3366CC')
ax_p.legend(loc=(loc_x,loc_y))
ax_P.legend(loc=(loc_x,loc_y))
ax_p.set_xlabel('r')
ax_P.set_xlabel('r')
ax_p.set_ylabel(r'$m^*$')
ax_P.set_ylabel(r'$m^*$')


# axs[:,:].set_ylim(0,10)
for ax_i in np.arange (axs.shape[0]):
    for ax_j in np.arange(axs.shape[1]):
        axs[ax_i,ax_j].set_ylim(0,30)


plt.savefig('./figures/samplers_convergenceSeries.pdf')