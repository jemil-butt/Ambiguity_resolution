"""
This file provides several support functions that are available after import.
The functions are:
    Generate_data: Generates a sequence of complex valued observations
    Generate_data_noisy : Generates a sequence of complex valued observations
        which have been impacted by phase noise
    Setup_optim_options: Generate a dictionary of optimization options
"""




def Generate_data(weights,distances,wavelengths):
    """
    The goal of this function is to calculate a sequence of complex numbers 
    representing measurements to surfaces S_1, ... , S_n whose backscattering
    intensities and distances to the instrument are recorded in the n-dim 
    vectors "weights" and "distances". The measurements are assumed to 
    occur simultaneously to all surfaces jointly leading to one complex number
    per wavelength representing the superposition of all backscattered waves. 
    
    For this, do the following:
        1. Imports and definitions
        2. Initialize data structures
        3. Calculate observations

    INPUTS
    The inputs consist in two n-dim vectors detailing the intensities of the 
    waves backscattered by the srufaces S_1, ... ,S_n and the distances to the
    measuring instrument. The sequence of m wavelengths used to perform the 
    observations is stored in the m-dim vector "wavelengths".
    
    Name                 Interpretation                             Type
    weights             Instensities for the backscattered          Vector [n]
                        waves after interacting with S_1, 
                        ... , S_n. Used for complex addition.
    distances           Distances between scatterers and            Vector [n]
                        instrument. Used for phase calculation.
    wavelengths         Wavelengths of the waves used to perform    Vector [m]
                        the measurements.
                        
                        
    OUTPUTS
    The outputs consist in the sequence of complex numbers representing the 
    observed phases and intensities.
    
    Name                 Interpretation                             Type
    measurements       The synthetic measurements                   c-vector [m]
    backscatter        The synthetic measurements prior to          c-matrix [n,m]
                       superposition


    """
    
    
    
    """
        1. Imports and definitions -------------------------------------------
    """
    
    
    # i) Import packages
    
    import numpy as np
    
    
    # ii) Extract dimensions
    
    n=len(weights)
    m=len(wavelengths)
        
    
    
    """
        2. Initialize data structures -----------------------------------------
    """
    
    
    # i) Measuremens and the matrix C of complex numbers repreenting backscatter
    
    measurements=np.zeros([m],dtype=np.complex)
    backscatter=np.zeros([n,m],dtype=np.complex)
    
    
    
    
    """    
        3. Calculate observations --------------------------------------------
    """
    
    
    # i) Fill the matrix of individual backscatters signals
    
    for k in range(n):
        for l in range(m):
            backscatter[k,l]=weights[k]*np.exp(1j*4*np.pi*distances[k]/wavelengths[l])
    
    
    # ii) Fill the vector of measurements with superpositions of backscattered
    # signals
    
    for l in range(m):
        measurements[l]=np.sum(backscatter[:,l])
    
     
    return measurements,backscatter
    
    
    
    
    
    
def Generate_data_noisy(weights,distances,wavelengths,phase_variances):
    """
    The goal of this function is to calculate a sequence of complex numbers 
    representing measurements to surfaces S_1, ... , S_n whose backscattering
    intensities and distances to the instrument are recorded in the n-dim 
    vectors "weights" and "distances". The measurements are assumed to 
    occur simultaneously to all surfaces jointly leading to one complex number
    per wavelength representing the superposition of all backscattered waves.
    Phase noise with differing variances as prescribed in the vector "phase_ 
    variances" is added onto the measurements
    
    For this, do the following:
        1. Imports and definitions
        2. Initialize data structures
        3. Calculate observations

    INPUTS
    The inputs consist in two n-dim vectors detailing the intensities of the 
    waves backscattered by the srufaces S_1, ... ,S_n and the distances to the
    measuring instrument. The sequence of m wavelengths used to perform the 
    observations is stored in the m-dim vector "wavelengths".
    
    Name                 Interpretation                             Type
    weights             Instensities for the backscattered          Vector [n]
                        waves after interacting with S_1, 
                        ... , S_n. Used for complex addition.
    distances           Distances between scatterers and            Vector [n]
                        instrument. Used for phase calculation.
    wavelengths         Wavelengths of the waves used to perform    Vector [m]
                        the measurements.
    phase_variances     Phase variances of the noise to be added    Vector [m]
                        onto the superposition of backscatter
                        
                        
    OUTPUTS
    The outputs consist in the sequence of complex numbers representing the 
    observed phases and intensities.
    
    Name                 Interpretation                             Type
    measurements       The synthetic, noisy measurements            c-vector [m]
    backscatter        The synthetic measurements prior to          c-matrix [n,m]
                       superposition


    """
    
    
    
    """
        1. Imports and definitions -------------------------------------------
    """
    
    
    # i) Import packages
    
    import numpy as np
    
    
    # ii) Extract dimensions
    
    n=len(weights)
    m=len(wavelengths)
        
    
    
    """
        2. Initialize data structures -----------------------------------------
    """
    
    
    # i) Measuremens and the matrix C of complex numbers repreenting backscatter
    
    measurements=np.zeros([m],dtype=np.complex)
    backscatter=np.zeros([n,m],dtype=np.complex)
    
    
    
    
    """    
        3. Calculate observations --------------------------------------------
    """
    
    
    # i) Fill the matrix of individual backscatters signals
    
    for k in range(n):
        for l in range(m):
            backscatter[k,l]=weights[k]*np.exp(1j*4*np.pi*distances[k]/wavelengths[l])
    
    
    # ii) Fill the vector of measurements with superpositions of backscattered
    # signals and add noise

    
    for l in range(m):
        measurements[l]=np.sum(backscatter[:,l])*np.exp(1j*np.random.normal(0,np.sqrt(phase_variances[l])))
    
     
    return measurements,backscatter
    
    
    
    
    
    
    
def Setup_optim_options(n_obs, max_iter=300, **constraints):
    """
    The goal of this function is to set up the options dictionary optim_options
    for the optimization to be carried out during ambiguity resolution or
    unmixing. It can be called without any input arguments to generate the
    options necessary to perform unbounded estimation with standard values 
    regarding convergence and nr of iterations.
    
    For this, do the following:
        1. Imports and definitions
        2. Initialize and read data
        3. Assemble and return dictionary

    INPUTS
    The inputs consist in several properties that are passed to the solver 
    afterwards.
    
    Name                 Interpretation                             Type
    n_obs               Dimension of the problem, i.e. number       positive integer
                        of observations
    max_iter            Number of iterations not exceeded           positive integer
                        during optimization
    constraints         List containing expressions for the bounds
                        e.g. ['d_opt>=10']
                        
                        
    OUTPUTS
    The outputs consist in the dictionary optim_options containing additional
    information and options for the optimization carried during estimation in
    other functions.
    
    Name                 Interpretation                             Type
    optim_options       The options for optimization               dictionary


    """
    
    
    
    """
        1. Imports and definitions ------------------------------------------
    """
    
    
    # i) Import packages
    
    import numpy as np

    
    
    """
        2. Initialize and read data ------------------------------------------
    """
    
    
    # i) Create string list of constraints
    
    cons=['d_opt>=0']
    
    for k in range(n_obs):
        cons=cons+['N_opt[{}]>=0'.format(k)]
    
    for key,value in constraints.items():
        cons=cons+value    
    
    
    
    
    """    
         3. Assemble and return dictionary -----------------------------------
    """
    
    
    # i) Assemble optim_options
    
    optim_options={}
    optim_options['max_iter']=max_iter
    optim_options['constraints']=cons
    
     
    return optim_options
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    