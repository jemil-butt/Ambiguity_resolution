"""
The goal of this script is to illustrate the ambiguity resolution function and
demonstrate its preformance when the observations originate from a mixed pixel
For this, do the following:
    1. Definitions and imports
    2. Simulate data
    3. Solve the estimation problem 
    4. Compare results and ground truth

"""

"""
    1. Definitions and imports -----------------------------------------------
"""



# i) Imports


import Support_funs_AR as sf
import numpy as np
import Ambiguity_resolution as AR
import time

import matplotlib.pyplot as plt


# ii) Basic definitions

n_obs=10

weights=np.array([2,1])
distances=np.array([1,2])
wavelengths=np.linspace(0.01,0.05,n_obs)

phase_variances=np.ones([n_obs])*0.01



"""
    2. Simulate data ---------------------------------------------------------
"""


# i) Generate the data

observations, _=sf.Generate_data(weights,distances,wavelengths)
observations_noisy, _=sf.Generate_data_noisy(weights,distances,wavelengths,phase_variances)




"""
    3. Solve the estimation problem ------------------------------------------
"""


# i) Solve the problem

cons=['d_opt<=20']
optim_opts=sf.Setup_optim_options(n_obs, constraints=cons)

d,N,r=AR.Ambiguity_resolution(observations, wavelengths, phase_variances,optim_opts)
d_noise,N_noise,r_noise=AR.Ambiguity_resolution(observations, wavelengths, phase_variances,optim_opts)



"""
    4. Compare results and ground truth ---------------------------------------
"""



# i) Print out results

time.sleep(0.1)

print(' The ground truth distances are d = {}'.format(distances))
print(' The estimated distance is d = {}'.format(d))
print(' The noisily estimated distance is d = {}'.format(d_noise))


# ii) Calculate complex residuals (no noise, noise, arbitrary distance)

r_complex=np.exp(1j*r)
r_complex_noise=np.exp(1j*r_noise)

d_arbitrary=np.abs(np.random.normal(0,1))
observations_arbitrary,_=sf.Generate_data(np.ones([1]),d_arbitrary*np.ones([1]),wavelengths)

r_arbitrary=np.angle(np.conj(observations)*observations_arbitrary)
r_complex_arbitrary=np.exp(1j*r_arbitrary)
                     
# iii) Illustrate residuals

plt.rcParams["font.size"]='10'

w,h=plt.figaspect(0.6)
fig1 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
gs1 = fig1.add_gridspec(1, 3)


f1_ax1 = fig1.add_subplot(gs1[0,0])
f1_ax1.scatter(np.real(r_complex),np.imag(r_complex),c='black',marker='.')
f1_ax1.set_title('Residuals no noise')
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')

f1_ax2 = fig1.add_subplot(gs1[0,1])
f1_ax2.scatter(np.real(r_complex_noise),np.imag(r_complex_noise),c='black',marker='.')
f1_ax2.set_title('Residuals noisy case')
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')

f1_ax3 = fig1.add_subplot(gs1[0,2])
f1_ax3.scatter(np.real(r_complex_arbitrary),np.imag(r_complex_arbitrary),c='black',marker='.')
f1_ax3.set_title('Residuals arbitrary d')
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')



















