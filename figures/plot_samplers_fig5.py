import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./style.mplstyle")

f, axs = plt.subplots(nrows=6, ncols=1, figsize=(5,9), sharex=True)
f.subplots_adjust(hspace=0.05)

boxstyle = dict(boxstyle='round',fc="w", ec="k")

color1 = '#3366CC'
color2 = color='#CC6633'
loc_text_x = 0.8
loc_text_y = 0.6
D=1

data_p = np.loadtxt('./results/samplers_fig5_p_b1t100.txt')
b = 1
t = b*b/D/100
axs_p_b1t100 = axs[0]
axs_dp_b1t100 = axs[1]
axs_p_b1t100.plot(data_p[:,0],data_p[:,1],color=color1)
axs_p_b1t100.set_ylabel(r"$p(r)$")
axs_dp_b1t100.plot(data_p[:,0],data_p[:,2],color=color1)
axs_dp_b1t100.set_ylabel(r"$\frac{dp(r,t)}{dr}$")
r = np.sqrt(t*D)*2
axs_p_b1t100.axvline(r, color=color2)
axs_dp_b1t100.axvline(r, color=color2)

text = r"$b=1$" "\n" r"$t=\frac{b^2}{100Dt}$"
axs_p_b1t100.text(loc_text_x,loc_text_y, text, transform=axs_p_b1t100.transAxes, bbox=boxstyle)
axs_dp_b1t100.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t100.transAxes, bbox=boxstyle)



data_p = np.loadtxt('./results/samplers_fig5_p_b1t10.txt')
loc_text_x = 0.05

b = 1
t = b*b/D/10
t0=0.063
t1=0.234
R0=2*np.sqrt(t0*b*b)
R1=0.646*b
beta = (R0*np.exp(np.power(t0,0.5)+np.power(t1,0.5))-R1*np.exp(np.power(t0,0.5)+np.power(t1,0.5))) \
       /(np.exp(np.power(t0,0.5))-np.exp(np.power(t1,0.5)))
gamma = -(R0*(np.exp(np.power(t1,0.5))-1)*np.exp(np.power(t0,0.5))-R1*(np.exp(np.power(t0,0.5))-1)*np.exp(np.power(t1,0.5))) \
        /(np.exp(np.power(t0,0.5))-np.exp(np.power(t1,0.5)))
r=beta*(1-np.exp(-np.power(t*D/b/b,0.5)))+gamma
axs_p_b1t10 = axs[2]
axs_dp_b1t10 = axs[3]
axs_p_b1t10.plot(data_p[:,0],data_p[:,1],color=color1)
axs_p_b1t10.set_ylabel(r"$p(r,t)$")
axs_dp_b1t10.plot(data_p[:,0],data_p[:,2],color=color1)

axs_dp_b1t10.set_ylabel(r"$\frac{dp(r,t)}{dr}$")
axs_p_b1t10.axvline(r, color=color2)
axs_dp_b1t10.axvline(r, color=color2)
text = r"$b=1$" "\n" r"$t=\frac{b^2}{10Dt}$"

axs_p_b1t10.text(loc_text_x,loc_text_y,text, transform=axs_p_b1t10.transAxes, bbox=boxstyle)
loc_text_y = 0.15
axs_dp_b1t10.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t10.transAxes, bbox=boxstyle)



data_p = np.loadtxt('./results/samplers_fig5_p_b1t1.txt')
b = 1
t = b*b/D
axs_p_b1t1 = axs[4]
axs_dp_b1t1 = axs[5]
axs_p_b1t1.plot(data_p[:,0],data_p[:,1], color=color1)
axs_p_b1t1.set_ylabel(r"$p(r,t)$")
axs_dp_b1t1.plot(data_p[:,0],data_p[:,2], color=color1)
axs_dp_b1t1.set_ylabel(r"$\frac{dp(r,t)}{dr}$")
axs_dp_b1t1.set_xlabel(r"$r$")
r = 0.646*b
axs_p_b1t1.axvline(r, color=color2)
axs_dp_b1t1.axvline(r, color=color2)
text = r"$b=1$" "\n" r"$t=\frac{b^2}{Dt}$"
axs_dp_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_dp_b1t1.transAxes, bbox=boxstyle)
loc_text_y = 0.6
axs_p_b1t1.text(loc_text_x,loc_text_y,text, transform=axs_p_b1t1.transAxes, bbox=boxstyle)


plt.tight_layout()

plt.savefig('./figures/samplers_fig5.pdf')


