"""
The goal of this script is to compare the ambiguity resolution function to a 
guess of a distance employing a global solver directly for the distance d
For this, do the following:
    1. Definitions and imports
    2. Simulate data
    3. Solve the estimation problem 
    4. Compare results from both methods

"""

"""
    1. Definitions and imports -----------------------------------------------
"""



# i) Imports


import Support_funs_AR as sf
import numpy as np
import Ambiguity_resolution as AR
import time

from scipy.optimize import basinhopping


# ii) Basic definitions

n_obs=10
n_trials=1000

weights=np.ones([1])
wavelengths=np.linspace(0.01,0.05,n_obs)
phase_variances=np.ones([n_obs])*0.01


# iii) Objective function

def residuals(observations, weights,distances,wavelengths):
    
    observations_pred, _=sf.Generate_data(weights,distances,wavelengths)
    phi_pred=np.angle(observations_pred)
    phi_diff=np.angle(np.conj(observations)*observations_pred)
    
    return phi_diff, phi_pred

def obj_fun(observations, weights,distances,wavelengths):
    phi_residuals,_ = residuals(observations, weights,distances,wavelengths)
    norm_resid=np.linalg.norm(phi_residuals,1)
    return norm_resid


"""
    2. Simulate data ---------------------------------------------------------
"""


# i) Generate the data

d_true=np.zeros([n_trials])
d_estimated_AR=np.zeros([n_trials])
d_estimated_AR_noisy=np.zeros([n_trials])
d_estimated_global=np.zeros([n_trials])

for k in range(n_trials):
       
    distance_true=np.random.uniform(0,10)
    distances=distance_true*np.ones([1])
    
    observations, _=sf.Generate_data(weights,distances,wavelengths)
    observations_noisy, _=sf.Generate_data_noisy(weights,distances,wavelengths,phase_variances)
    
    
    
    
    """
        3. Solve the estimation problem ------------------------------------------
    """
    
    
    # i) Solve the problem with our algorithm
    
    cons=['d_opt<=20']
    optim_opts=sf.Setup_optim_options(n_obs, constraints=cons)
    
    d_AR,N_AR,r_AR=AR.Ambiguity_resolution(observations, wavelengths, phase_variances,optim_opts)
    d_noise,N_noise,r_noise=AR.Ambiguity_resolution(observations_noisy, wavelengths, phase_variances,optim_opts)
    
    
    # ii) Solve the problem with a global algorithm
    
    def f(d):
        f_val=obj_fun(observations,weights,d,wavelengths)
        return f_val
    
    d_global=basinhopping(f,1,niter=10, disp=True).x
    
    d_true[k]=distance_true
    d_estimated_AR[k]=d_AR
    d_estimated_AR_noisy[k]=d_noise
    d_estimated_global[k]=d_global
    


"""
    4. Compare results and ground truth ---------------------------------------
"""



# i) Print out results

time.sleep(0.01)

print('AR failed nr of times for our approach', np.sum(np.abs(d_true-d_estimated_AR)>=0.00001))
print('AR failed nr of times for global approach', np.sum((np.abs(d_true-d_estimated_global)>=0.00001)))






























