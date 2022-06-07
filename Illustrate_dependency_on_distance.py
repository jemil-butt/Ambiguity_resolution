""" 
The goal of this script is to illustrate the phase residuals and their chaotic 
dependence on the choice of estimated distance. This serves to underline the
inability of global optimization routines to arrive at the correct solution.

For this, do the following:
    1. Definitions and imports
    2. Simulate the data
    3. Plots and illustrations
"""




"""
    1. Definitions and imports -----------------------------------------------
"""


# i) Import packages

import numpy as np
import matplotlib.pyplot as plt
import Support_funs_AR as sf


# ii) Set up general quantities

n_obs=10
n_disc=10000

wavelengths=10**(np.linspace(-4,0,n_obs))
weights=[1]

d_true=[1]
d_sample_1=np.linspace(0,2*d_true[0],n_disc)



"""
    2. Simulate the data -----------------------------------------------------
"""


# i) Define objective function

z_true,_=sf.Generate_data(weights, d_true,wavelengths)

def obj_fun(wavelengths,d_est):
    
    z_est,_=sf.Generate_data(weights,[d_est],wavelengths)
    phi_temp=np.angle(z_est)
    phase_resid=phi_temp-np.angle(z_true)
    resid_norm=np.linalg.norm(phase_resid,1)
    
    return resid_norm/n_obs


# ii) Evaluate objective function at sample points 1

obj_sample_1=np.zeros([n_disc])

for k in range(n_disc):
    obj_sample_1[k]=obj_fun(wavelengths,d_sample_1[k])
   
    
# iii) Evaluate objective function at sample points 2

d_sample_2=np.linspace(1.8,2,n_disc)
obj_sample_2=np.zeros([n_disc])

for k in range(n_disc):
    obj_sample_2[k]=obj_fun(wavelengths,d_sample_2[k])
    
    
    
# iv) Evaluate objective function at sample points 3

d_sample_3=np.linspace(0.9,1.1,n_disc)
obj_sample_3=np.zeros([n_disc])

for k in range(n_disc):
    obj_sample_3[k]=obj_fun(wavelengths,d_sample_3[k])


# v) Evaluate objective function at sample points 4

d_sample_4=np.linspace(0.99,1.01,n_disc)
obj_sample_4=np.zeros([n_disc])

for k in range(n_disc):
    obj_sample_4[k]=obj_fun(wavelengths,d_sample_4[k])




"""
    3. Plots and illustrations -----------------------------------------------
"""


# i) Zoomed out global image (sample_points_1)

#plt.rcParams["font.size"]='20'

w,h=plt.figaspect(0.7)
fig1 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))

plt.plot(d_sample_1,obj_sample_1, color='black')
plt.ylim(0,np.pi+1)

plt.xlabel('Estimated distance $d$')
plt.ylabel(' $\|\|\\hat{\phi}(d)-\phi^{obs}\|\|_1$')
plt.title('Objective function value dependence on $d$ ')



# ii) Zoomed in image 1 (Sample points 2)


w,h=plt.figaspect(1)
fig2 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))

plt.plot(d_sample_2,obj_sample_2, color='black')
plt.ylim(0,np.pi+1)

plt.xlabel('Estimated distance $d$')
plt.ylabel(' $\|\|\\hat{\phi}(d)-\phi^{obs}\|\|_1$')
plt.title('Objective function value dependence on $d$ ')


# iii) Zoomed in image 1 (Sample points 3)

w,h=plt.figaspect(1)
fig3 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))

plt.plot(d_sample_3,obj_sample_3, color='black')
plt.ylim(0,np.pi+1)

plt.xlabel('Estimated distance $d$')
plt.ylabel(' $\|\|\\hat{\phi}(d)-\phi^{obs}\|\|_1$')
plt.title('Objective function value dependence on $d$ ')


# iv) Zoomed in image 1 (Sample points 4)

w,h=plt.figaspect(1)
fig4 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))

plt.plot(d_sample_4,obj_sample_4, color='black')
plt.ylim(0,np.pi+1)

plt.xlabel('Estimated distance $d$')
plt.ylabel(' $\|\|\\hat{\phi}(d)-\phi^{obs}\|\|_1$')
plt.title('Objective function value dependence on $d$ ')








































