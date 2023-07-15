# Grid_independent_test_on_One_dimensional_wave_equation
We have done numerical calculations and provided a code for solving 1-D wave equation using the upwind-finite scheme and checking grid independent test on it by varying Grid size(N) and Courant number(λ)by finding maximum error and iteration in each case.
The parameters used in the calculations are as follows: the speed of sound (C) is 1, the distance of the domain (D) is 0.5, and the total time (T) is 0.5. The domain is defined by the range between Xmin = 0.5 and Xmax = 1.

We consider different grid sizes (N). For each grid size, we evaluate the numerical solution for various Courant number values (λ) values. The time step size(Δt) is determined using the formula cΔt/Δx=λ, where Δx is the grid spacing

The result of the calculation provides insights into the number of iterations required, and time step size and also helps us to find the mean and max error for each case, based on the chosen Courant number and grid size. The analysis helps us to assess the grid independence and accuracy of the numerical solution as the grid is refined.

