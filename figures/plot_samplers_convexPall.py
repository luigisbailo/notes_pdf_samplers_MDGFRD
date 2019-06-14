import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./style.mplstyle")

f, axs = plt.subplots(nrows=1, ncols=2, figsize=(5,2))

boxstyle = dict(boxstyle='round',fc="w", ec="k")
f.subplots_adjust(wspace=0.25)


D=1

data_q_b1 = np.loadtxt('./results/samplers_fig3_b1.txt')
b=1
text_loc_x = 0.75
text_loc_y = 0.1
axs_q_b1 = axs[0]
axs_q_b1.axvline(0.063*b*b/D, color='grey',linestyle='--')
axs_q_b1.axvline(0.234*b*b/D, color='grey',linestyle='--')
axs_q_b1.plot(data_q_b1[:int(len(data_q_b1)/2), 0], data_q_b1[:int(len(data_q_b1)/2), 1], color='#3366CC')
axs_q_b1.plot(data_q_b1[:int(len(data_q_b1)/2):2, 0], data_q_b1[:int(len(data_q_b1)/2):2, 2], 'x', color='#CC6633',markersize=3)
axs_q_b1.set_xlabel('t')
axs_q_b1.set_ylabel('r')
axs_q_b1.text(text_loc_x,text_loc_y,s=r"$b=1$",transform=axs[0].transAxes,bbox=boxstyle)

b=10
text_loc_x = 0.7
data_q_b10 = np.loadtxt('./results/samplers_fig3_b10.txt')
axs[1].axvline(0.063*b*b/D,color='grey',linestyle='--')
axs[1].axvline(0.234*b*b/D,color='grey',linestyle='--')
axs[1].plot(data_q_b10[:int(len(data_q_b10)/2), 0], data_q_b10[:int(len(data_q_b10)/2), 1], color='#3366CC')
axs[1].plot(data_q_b10[:int(len(data_q_b10)/2):2, 0], data_q_b10[:int(len(data_q_b10)/2):2, 2], 'x', color='#CC6633',markersize=3)
axs[1].set_xlabel('t')
axs[1].text(text_loc_x,text_loc_y,s=r"$b=10$",transform=axs[1].transAxes,bbox=boxstyle)


axs[0].set_ylim(0,1)
axs[1].set_ylim(0,10)

plt.savefig('./figures/samplers_convexPall.pdf')