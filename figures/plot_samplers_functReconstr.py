import numpy as np
import matplotlib.pyplot as plt

f, axs = plt.subplots(nrows=4, ncols=1, figsize=(6,8), tight_layout=True)

loc_x = 0.7
loc_y = 0.7
boxstyle = dict(boxstyle='round',fc="w", ec="k")
color1 = '#3366CC'
color2 = '#CC6633'


data = np.loadtxt('./results/samplers_funcReconstr_q.txt')
bar_width = data[1, 0] - data[0, 0]
ax_q = axs[0]
ax_q.bar(data[:, 0], data[:, 1], bar_width, color=color2)
ax_q.set_ylabel(r'$q(t)$')

data = np.loadtxt('./results/samplers_funcReconstr_pt100.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p100 = axs[1]
ax_p100.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p100.set_ylabel(r'$p(r,t)$')

data = np.loadtxt('./results/samplers_funcReconstr_pt10.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p10 = axs[2]
ax_p10.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p10.set_ylabel(r'$p(r,t)$')

data = np.loadtxt('./results/samplers_funcReconstr_pt1.txt')
bar_width = data[1, 0] - data[0, 0]
ax_p1 = axs[3]
ax_p1.bar(data[:, 0], data[:, 1], bar_width, color=color1)
ax_p1.set_ylabel(r'$p(r,t)$')


plt.savefig('./figures/samplers_funcReconstr.pdf')
