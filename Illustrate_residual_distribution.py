""" 
The goal of this script is to illustrate the distribution of phase residuals
for different values assumed d when the number of observations converges to infinity.
Different cases will be investigated: i) Equidistribution of residuals , ii)
different forms of non-equidistributed residuals.
We assume that the measurements are performed in a mixed pixel setting with two
participating surfaces.

For this, do the following:
    1. Definitions and imports
    2. Generate residuals for different cases
    3. Plots and illustrations
"""



"""
    1. Definitions and imports ------------------------------------------------
"""


# i) Import packages

import numpy as np
import matplotlib.pyplot as plt
import Support_funs_AR as sf


# ii) Set up basic dimensions

n_obs=400              # Number of observations
n_r_count=50           # Number of rows in matrix of rational numbers
n_irrational=1000         # Number of irrational cases tested
n_rational=n_r_count**2


wavelengths=np.linspace(0.01,0.05,n_obs)
weights=np.array([2,1])
sum_w=np.sum(weights)
   

# iii) Set up matrix of rationals 

R=np.zeros([n_r_count,n_r_count])
for k in range(n_r_count):
    for l in range(n_r_count):
        R[k,l]=(k+1)/(l+1)


  
"""  
    2. Generate residuals for different cases ---------------------------------
"""  


# i) Equidistributed case

Delta_d_irrational=np.random.uniform(0.02,1,[n_irrational,2])
mean_norm_irrational=np.zeros([n_irrational,1])

for k in range(n_irrational):
    resid_temp,_ =sf.Generate_data(weights, Delta_d_irrational[k,:],wavelengths)
    norm_phi_resid=np.linalg.norm(np.angle(resid_temp),ord=1)
    mean_norm_irrational[k]=(1/n_obs)*norm_phi_resid

    
# ii) Rational cases

Delta_d_rational=(np.vstack((np.ones([n_rational]),np.ravel(R)))).T
mean_norm_rational=np.zeros([n_rational,1])

for k in range(n_rational):
    resid_temp,_=sf.Generate_data(weights, Delta_d_rational[k,:],wavelengths)
    norm_phi_resid=np.linalg.norm(np.angle(resid_temp),ord=1)
    mean_norm_rational[k]=(1/n_obs)*norm_phi_resid
    

# iii) Rational limit cases: one of the delta =0

Delta_d_01=[0,1]
Delta_d_10=[1,0]

resid_01,_=sf.Generate_data(weights, Delta_d_01,wavelengths)
mean_norm_limit_01=(1/n_obs)*np.linalg.norm(np.angle(resid_01),ord=1)

resid_10,_=sf.Generate_data(weights, Delta_d_10 ,wavelengths)
mean_norm_limit_10=(1/n_obs)*np.linalg.norm(np.angle(resid_10),ord=1)
    

    
"""
    3. Plots and illustrations -----------------------------------------------
"""



# i) Calculate Delta d quotients

Quotients_irrational=Delta_d_irrational[:,0]/Delta_d_irrational[:,1]
Quotients_rational=Delta_d_rational[:,0]/Delta_d_rational[:,1]


# ii) Figure 1: Phase residuals case overview

plt.rcParams["font.size"]='15'

w,h=plt.figaspect(0.35)
fig1 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
f1_ax=fig1.add_subplot

plt.scatter(Quotients_rational,mean_norm_rational,s=150, c='black',marker='.',label='Rational dependence')
plt.scatter(Quotients_irrational,mean_norm_irrational, s=150,c='black',marker='+',label='Rational independence')

plt.scatter(0,mean_norm_limit_01,s=150, c='black',marker='*',label='Limit cases')
plt.scatter(0,mean_norm_limit_10,s=150, c='black',marker='*')
plt.hlines(np.pi/2,-1,30,colors='0.75',linestyle='dashed')

plt.xlabel('Ratio $\Delta d_1 / \Delta d_2$')
plt.ylabel('$\|\|\\hat{\phi}(d)-\phi^{obs}\|\|_1$')
plt.title('Norm of phase residuals')
plt.legend(loc='lower right')
plt.xlim(-1,15)
plt.ylim(0,2)

# iii) Calculate some phase residuals

resid_1,_=sf.Generate_data(weights, Delta_d_irrational[0,:],wavelengths)
resid_2,_=sf.Generate_data(weights, Delta_d_irrational[1,:],wavelengths)
resid_3,_=sf.Generate_data(weights, Delta_d_rational[1,:],wavelengths)
resid_4,_=sf.Generate_data(weights, Delta_d_rational[2,:],wavelengths)
resid_5=resid_01
resid_6=resid_10





# iv) Figure 2: Complex esidual distribution



w,h=plt.figaspect(0.6)
fig2 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
gs2 = fig2.add_gridspec(2, 3)


f2_ax1 = fig2.add_subplot(gs2[0,0])
f2_ax1.scatter(np.real(resid_1),np.imag(resid_1),c='black',marker='.',label='Rational independence')
f2_ax1.set_title('Rational independence')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax1.axis('off')


f2_ax2 = fig2.add_subplot(gs2[0,1])
f2_ax2.scatter(np.real(resid_2),np.imag(resid_2),c='black',marker='.',label='Rational independence')
f2_ax2.set_title('Rational independence')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax2.axis('off')


f2_ax3 = fig2.add_subplot(gs2[0,2])
f2_ax3.scatter(np.real(resid_3),np.imag(resid_3),c='black',marker='.',label='Rational dependence')
f2_ax3.set_title('Dependence: $\Delta d_1 / \Delta d_2=2$')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax3.axis('off')


f2_ax4 = fig2.add_subplot(gs2[1,0])
f2_ax4.scatter(np.real(resid_4),np.imag(resid_4),c='black',marker='.',label='Rational dependence')
f2_ax4.set_title('Dependence: $\Delta d_1 / \Delta d_2=3$')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax4.axis('off')


f2_ax5 = fig2.add_subplot(gs2[1,1])
f2_ax5.scatter(np.real(resid_5),np.imag(resid_5),c='black',marker='.',label='Limit case')
f2_ax5.set_title('Limit case $\Delta d_1 =0$')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax5.axis('off')

f2_ax6 = fig2.add_subplot(gs2[1,2])
f2_ax6.scatter(np.real(resid_6),np.imag(resid_6),c='black',marker='.',label='Limit case')
f2_ax6.set_title('Limit case $\Delta d_2 =0$')
plt.ylim((-sum_w,sum_w))
plt.xlim((-sum_w,sum_w))
plt.vlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
plt.hlines(0,-sum_w,sum_w,colors='0.75',linestyle='dashed')
#f2_ax6.axis('off')




# v) Figure 3: Phase residual distribution

resid_1_norm=resid_1/np.abs(resid_1)
resid_2_norm=resid_2/np.abs(resid_2)
resid_3_norm=resid_3/np.abs(resid_3)
resid_4_norm=resid_4/np.abs(resid_4)
resid_5_norm=resid_5/np.abs(resid_5)
resid_6_norm=resid_6/np.abs(resid_6)


w,h=plt.figaspect(0.6)
fig3 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
gs3 = fig3.add_gridspec(2, 3)


f3_ax1 = fig3.add_subplot(gs3[0,0])
f3_ax1.scatter(np.real(resid_1_norm),np.imag(resid_1_norm),c='black',marker='.',label='Rational independence')
f3_ax1.set_title('Rational independence')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax1.axis('off')


f3_ax2 = fig3.add_subplot(gs3[0,1])
f3_ax2.scatter(np.real(resid_2_norm),np.imag(resid_2_norm),c='black',marker='.',label='Rational independence')
f3_ax2.set_title('Rational independence')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax2.axis('off')


f3_ax3 = fig3.add_subplot(gs3[0,2])
f3_ax3.scatter(np.real(resid_3_norm),np.imag(resid_3_norm),c='black',marker='.',label='Rational dependence')
f3_ax3.set_title('Rational dependence')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax3.axis('off')


f3_ax4 = fig3.add_subplot(gs3[1,0])
f3_ax4.scatter(np.real(resid_4_norm),np.imag(resid_4_norm),c='black',marker='.',label='Rational dependence')
f3_ax4.set_title('Rational dependence')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax4.axis('off')


f3_ax5 = fig3.add_subplot(gs3[1,1])
f3_ax5.scatter(np.real(resid_5_norm),np.imag(resid_5_norm),c='black',marker='.',label='Limit case')
f3_ax5.set_title('Limit case')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax5.axis('off')

f3_ax6 = fig3.add_subplot(gs3[1,2])
f3_ax6.scatter(np.real(resid_6_norm),np.imag(resid_6_norm),c='black',marker='.',label='Limit case')
f3_ax6.set_title('Limit case')
plt.ylim((-1,1))
plt.xlim((-1,1))
plt.vlines(0,-1,1,colors='0.75',linestyle='dashed')
plt.hlines(0,-1,1,colors='0.75',linestyle='dashed')
#f2_ax6.axis('off')



# vi) Empirical distribution of phases

resid_phi_1=np.histogram(np.angle(resid_1_norm),density=True)
resid_phi_2=np.histogram(np.angle(resid_2_norm),density=True)
resid_phi_3=np.histogram(np.angle(resid_3_norm),density=True)
resid_phi_4=np.histogram(np.angle(resid_4_norm),density=True)
resid_phi_5=np.histogram(np.angle(resid_5_norm),density=True)
resid_phi_6=np.histogram(np.angle(resid_6_norm),density=True)


w,h=plt.figaspect(0.6)
fig4 = plt.figure(dpi=400,constrained_layout=True,figsize=(w,h))
gs4 = fig4.add_gridspec(2, 3)


f4_ax1 = fig4.add_subplot(gs4[0,0])
f4_ax1.scatter(resid_phi_1[1][1:],resid_phi_1[0],c='black',marker='.',label='Rational independence')
f4_ax1.set_title('Rational independence')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))


f4_ax2 = fig4.add_subplot(gs4[0,1])
f4_ax2.scatter(resid_phi_2[1][1:],resid_phi_2[0],c='black',marker='.',label='Rational independence')
f4_ax2.set_title('Rational independence')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))

f4_ax3 = fig4.add_subplot(gs4[0,2])
f4_ax3.scatter(resid_phi_3[1][1:],resid_phi_3[0],c='black',marker='.',label='Rational dependence')
f4_ax3.set_title('Rational dependence')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))


f4_ax4 = fig4.add_subplot(gs4[1,0])
f4_ax4.scatter(resid_phi_4[1][1:],resid_phi_4[0],c='black',marker='.',label='Rational dependence')
f4_ax4.set_title('Rational dependence')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))


f4_ax5 = fig4.add_subplot(gs4[1,1])
f4_ax5.scatter(resid_phi_5[1][1:],resid_phi_5[0],c='black',marker='.',label='Limit case')
f4_ax5.set_title('Limit case')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))


f4_ax6 = fig4.add_subplot(gs4[1,2])
f4_ax6.scatter(resid_phi_6[1][1:],resid_phi_6[0],c='black',marker='.',label='Limit case')
f4_ax6.set_title('Limit case')
plt.ylim((0,1))
plt.xlim((-np.pi,np.pi))

