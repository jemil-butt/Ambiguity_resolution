def Ambiguity_resolution(observations, wavelengths, phase_variances,optim_opts):

    """ 
    The goal of this function is to solve the simple ambiguity resolution problem 
    in which a sequence of (potentially noisy) measurements with different wavelengths
    has been acquired. It is assumed that all these measurements have been made to
    the same surface S in distance d to the measuring instrument and the distance
    d is to be extracted from the observations. This is done via formulating the
    optimal estimation of d and associated number N of full wavecycles as a mixed
    integer linear program emulating an l1 norm minimization on the phase residuals.
    
    For this, do the following:
        1. Definitions and imports
        2. Assemble required matrices
        3. Perform optimization
        4. Assemble results
        
    INPUTS
    The inputs consist in three vectors, all of which have length equal to the number
    n_obs of observations. The vector "observations" contains the observed complex
    values whereas the sequence of n_obs wavelengths used to perform the 
    observations is stored in the m-dim vector "wavelengths". A vector "phase_
    variances" documents the assumed variances of the phase measurements; in the
    setting of Multiwavelength-EDM they are typically all equal. 
    A dictionary "optim_opts" collects further information pertaining to the 
    optimization - like bounds and convergence criteria.
    
    Name                 Interpretation                             Type
    observations        Observations in the form of complex         c-vector [n_obs]
                        numbers representing phases and amplitudes
                        observed during the measurements
    wavelengths         Wavelengths of the waves used to perform    vector [n_obs]
                        the measurements.
    phase_variances     Phase variances of the noise added onto     vector [n_obs]
                        the superposition of backscatter
    optim_options       The options for optimization                dictionary
                        
                        
    OUTPUTS
    The outputs consist in the distance minimizing the l1 norm of residuals as well 
    as the vector N of full wavecycles and the vector of residuals
    
    Name                 Interpretation                             Type
    d                  The optimally estimated distance             real number
    N                  A vector containing estimated full           integer vector [n_obs]
                       wavecycles
    r                  A vector containing unweighted residuals     vector [n_obs]
                          
    """
    
    
    
    """
        1. Definitions and imports -------------------------------------------
    """
    
    
    # i) Import numerical and optimization libraries
    
    import numpy as np
    import cvxpy as cp
    
    
    # ii) Define other quantities
    
    n_obs=len(observations)
    
    
    # iii) Extract qunatities
    
    phi_obs=np.angle(observations)
    max_iter=optim_opts['max_iter']
    constraints=optim_opts['constraints']
    
    
    
    """
        2. Assemble required matrices ----------------------------------------
    """
    
    
    # i) Coefficient matrices
    
    lambda_mat=np.diag(wavelengths)
    lambda_mat_pinv=np.linalg.pinv(lambda_mat)
    lambda_vec_pinv=np.diag(lambda_mat_pinv)
    
    phase_std=np.sqrt(phase_variances)
    phase_std_pinv=np.linalg.pinv(np.diag(phase_std))
    
    
    # ii) Optimization variables
    
    d_opt=cp.Variable(nonneg=True)
    N_opt=cp.Variable(n_obs,integer=True)
    
    
    
    """
        3. Perform optimization ----------------------------------------------
    """
    
    
    # i) Objective function and constraints
    
    objective=cp.Minimize(cp.norm(phase_std_pinv@(2*np.pi*(2*d_opt*lambda_vec_pinv-N_opt)-phi_obs),p=1))
    
    cons=[]
    for cstr in constraints:
        cons=cons+[eval(cstr)]
    
    
    # ii) Solve optimization
    
    Optim_problem=cp.Problem(objective,constraints=cons)
    Optim_solution=Optim_problem.solve(solver='GLPK_MI',max_iters=max_iter, verbose=True)
    
    
    
    """
        4. Assemble results --------------------------------------------------
    """
    
    
    # i) Values of optimization variables
    
    d=d_opt.value
    N=N_opt.value
    
    
    # ii) Residuals
    
    r=2*np.pi*(2*d*lambda_vec_pinv-N)-phi_obs
    
    return d, N, r
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









