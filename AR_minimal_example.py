"""
The goal of this script is to illustrate the ambiguity resolution function and
demonstrate its preformance on a simple example
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


# ii) Basic definitions

n_obs=10
distance_true=5

weights=np.ones([1])
distances=distance_true*np.ones([1])
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

print(' The ground truth distance is d = {}'.format(distance_true))
print(' The estimated distance is d = {}'.format(d))
print(' The noisily estimated distance is d = {}'.format(d_noise))
































