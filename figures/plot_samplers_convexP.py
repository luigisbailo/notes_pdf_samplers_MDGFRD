import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./style.mplstyle")

f, axs = plt.subplots(nrows=4, ncols=1, figsize=(5,5), sharex=True)
# f.subplots_adjust(hspace=0.05)

boxstyle = dict(boxstyle='round',fc="w", ec="k")

color1 = '#3366CC'
color2 ='dimgrey'
loc_text_x = 0.8
loc_text_y = 0.65
D=1

data_p = np.loadtxt('./results/samplers_convexP_b1t100.txt')
b = 1
t = b*b/D/100
axs_p_b1t100 = axs[0]
axs_dp_b1t100 = axs[1]
axs_p_b1t100.plot(data_p[:,0],data_p[:,1],color=color1)
axs_p_b1t100.set_ylabel(r"$p(r,t)$")
axs_dp_b1t100.plot(data_p[:,0],data_p[:,2],color=color1)
axs_dp_b1t100.set_ylabel(r"$\frac{dp(r,t)}{dr}$")
r = np.sqrt(t*D)*2
axs_p_b1t100.axvline(r, linestyle='--', color=color2)
axs_dp_b1t100.axvline(r, linestyle='--', color=color2)

text = r"$t=\frac{b^2}{100\thinspace Dt}$"
axs_p_b1t100.text(loc_text_x,loc_text_y, text, transform=axs_p_b1t100.transAxes, bbox=boxstyle)
axs_dp_b1t100.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t100.transAxes, bbox=boxstyle)


data_p = np.loadtxt('./results/samplers_convexP_b1t1.txt')
b = 1
t = b*b/D
axs_p_b1t1 = axs[2]
axs_dp_b1t1 = axs[3]
axs_p_b1t1.plot(data_p[:,0],data_p[:,1], color=color1)
axs_p_b1t1.set_ylabel(r"$p(r,t)$")
axs_dp_b1t1.plot(data_p[:,0],data_p[:,2], color=color1)
axs_dp_b1t1.set_ylabel(r"$\frac{dp(r,t)}{dr}$")
axs_dp_b1t1.set_xlabel(r"$r$")
r = 0.646*b
axs_p_b1t1.axvline(r, linestyle='--', color=color2)
axs_dp_b1t1.axvline(r, linestyle='--', color=color2)
text = r"$t=\frac{b^2}{Dt}$"

axs_dp_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t1.transAxes, bbox=boxstyle)
loc_text_x = 0.05
axs_p_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_p_b1t1.transAxes, bbox=boxstyle)


# plt.tight_layout()

plt.savefig('./figures/samplers_convexP.pdf')


