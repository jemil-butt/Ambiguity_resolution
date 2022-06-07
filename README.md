# Ambiguity_resolution

Python code implementing optimal resolution of ambiguities occuring when performing phase-based distance measurements with multiple wavelengths. This repository provides basic functions and minimal working examples related to solving ambuguity resolution via mixed integer programming.

Code and figures are meant as supplementaries the paper "Phase ambiguity resolution and mixed pixel detection in EDM with multiple modulation wavelengths" by Jemil Butt and David Salido Monzu. The repository consists of a single folder containing different scripts and functions:

Ambiguity_resolution.py  :  Basic function for reformulating ambiguity resolution as a mixed integer linear program and solving it.
Support_funs_AR.py  :  Basic collection of supporting functions for simulating obervations, residuals, ...

AR_minimal_example.py  :  Minimal working example for ambiguity resolution
MP_minimal_example.py  :  Minimal working example for mixed pixel resolution

Compare_global_to_MILP.py  :  Compare Mixed integer linear programming to basinhopping approach

Illustrate_superposition.py  :  Illustrate the effects of mixing different waves associated to surfaces in different distances
Illustrate_residual_distribution.py  :  Illustrate the residuals for different (wrongly) assumed surface distances
Illustrate_dependency_on_distance.py  :  Illustrate the objective function as a function of distance to showcase its irregularity.



The code is provided with the sole intent being helpful for purposes of education and teaching and we hope, it will be found to be useful. Although we took care to provide clean and well-documented programs, no guarantees as with respect to its correctness can be given and we are aware of a number of numerical instabilities and fail-cases. The code makes use of the open source projects "cvxpy" and "cvxopt" for formulating optimization programs, "glpk" for solving mixed integer linear programs, "scipy.optimize" for benchmarking against black box optimization algorithms, and "numpy" . The associated packages are assumed to be installed.
