"""
The goal of this script is to illustrate the phenomenon of superposition of 
phasors and the impact it has on the observed phase in case of mixed pixels.

For this, do the following:
    1. Definitions and imports
    2. Generate observations
    3. Plots and illustrations
"""



"""
    1. Definitions and imports ------------------------------------------------
"""


# i) Import packages

import numpy as np
import matplotlib.pyplot as plt
import Support_funs_AR as sf


# ii) General definitions

n_disc=300
weights_1=[2,1]
weights_2=[1,1]
weights_3=[1,2]

wavelength=[0.01]  
wl_mult=1            

distances=(np.vstack((np.ones([n_disc]),np.linspace(1-wl_mult*wavelength[0],1+wl_mult*wavelength[0],n_disc)))).T
Delta_d=np.linspace(-wl_mult*wavelength[0],wl_mult*wavelength[0],n_disc)
Delta_d_normed=np.linspace(-wl_mult,wl_mult,n_disc)


"""
    2. Generate observations --------------------------------------------------
"""


# i) Create data

phase_obs_1=np.zeros([n_disc])
phase_obs_2=np.zeros([n_disc])
phase_obs_3=np.zeros([n_disc])

for k in range(n_disc):
    z_1,_=sf.Generate_data(weights_1,distances[k,:],wavelength)
    z_2,_=sf.Generate_data(weights_2,distances[k,:],wavelength)
    z_3,_=sf.Generate_data(weights_3,distances[k,:],wavelength)
    
    
    phase_obs_1[k]=np.angle(z_1)
    phase_obs_2[k]=np.angle(z_2)
    phase_obs_3[k]=np.angle(z_3)




"""
    3. Plots and illustrations ------------------------------------------------
"""


# i) Illustrate phase change dependent on distance change

w,h=plt.figaspect(0.8)
fig1 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
gs1 = fig1.add_gridspec(3, 1)


f1_ax1 = fig1.add_subplot(gs1[0,0])
f1_ax1.plot(Delta_d_normed,phase_obs_1,c='black',label='Rational independence')
f1_ax1.set_title('Observed phase for $w_1 / w_2 =2$')
# plt.ylim((-np.pi,np.pi))
plt.hlines(0,-wl_mult,wl_mult,colors='0.75',linestyle='dashed')
plt.ylabel('$\phi^{obs}$')
plt.xticks([-1, 0 ,1 ], " ")

f1_ax2 = fig1.add_subplot(gs1[1,0])
f1_ax2.plot(Delta_d_normed,phase_obs_2,c='black',label='Rational independence')
f1_ax2.set_title('Observed phase for $w_1 / w_2 =1$')
# plt.ylim((-np.pi,np.pi))
plt.hlines(0,-wl_mult,wl_mult,colors='0.75',linestyle='dashed')
plt.ylabel('$\phi^{obs}$')
plt.xticks([-1, 0 ,1 ], " ")

f1_ax3 = fig1.add_subplot(gs1[2,0])
f1_ax3.plot(Delta_d_normed,phase_obs_3,c='black',label='Rational independence')
f1_ax3.set_title('Observed phase for $w_1 / w_2 =0.5$')
# plt.ylim((-np.pi,np.pi))
plt.hlines(0,-wl_mult,wl_mult,colors='0.75',linestyle='dashed')
plt.xlabel('$\Delta d / \lambda$ (changes of surface $S_2$)')
plt.ylabel('$\phi^{obs}$')






















