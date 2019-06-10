import numpy as np
import matplotlib.pyplot as plt

f, axs = plt.subplots(nrows=1, ncols=2, figsize=(6,2), tight_layout=True)

text_loc_x = 0.8
text_loc_y = 0.1

D=1
b=1
data_b1 = np.loadtxt('./results/samplers_fig3_b1.txt')
axs[0].axvline(0.063*b*b/D,color='grey')
axs[0].axvline(0.234*b*b/D,color='grey')

axs[0].plot(data_b1[:,0],data_b1[:,1], color='#3366CC')
axs[0].plot(data_b1[::2,0],data_b1[::2,2], 'x', color='#CC6633')
axs[0].set_xlabel('t')
axs[0].set_ylabel('r')
axs[0].text(text_loc_x,text_loc_y,s=r"$b=1$",transform=axs[0].transAxes)

b=10
data_b10 = np.loadtxt('./results/samplers_fig3_b10.txt')
axs[1].axvline(0.063*b*b/D,color='grey')
axs[1].axvline(0.234*b*b/D,color='grey')

axs[1].plot(data_b10[:,0],data_b10[:,1], color='#3366CC')
axs[1].plot(data_b10[::2,0],data_b10[::2,2], 'x', color='#CC6633')
axs[1].set_xlabel('t')
axs[1].set_ylabel('r')
axs[1].text(text_loc_x,text_loc_y,s=r"$b=10$",transform=axs[1].transAxes)



plt.savefig('./figures/samplers_fig3.pdf')