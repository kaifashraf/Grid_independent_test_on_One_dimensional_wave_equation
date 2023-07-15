# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:17:29 2023

@author: MD AHZAM
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    a = 1.0  # Speed of sound
    tmax = 0.5  # Half of the distance of the time
    xmin = 0.0  # Lower boundary condition
    xmax = 1.0  # Upper boundary condition
    n = input("Enter grid resolutions (separated by commas): ").split(",")  # Grid resolutions to test
    n = [int(x) for x in n]  # Convert grid resolutions to integers
    lamda = [0.25, 0.5, 0.75, 1.0]  # Courant numbers to test

    for n_val in n:
        plt.figure()  # Create a new figure for each grid resolution
        for lamda_val in lamda:
            delx = (xmax - xmin) / n_val
            delt = (lamda_val * delx) / a
            m = int(tmax / delt)

            x = np.zeros(n_val + 1)
            u_new = np.zeros(n_val + 1)
            u_old = np.zeros(n_val + 1)
            Location = np.zeros(n_val + 1)
            Exact = np.zeros(n_val + 1)
            errors = []

            for i in range(n_val + 1):
                x[i] = xmin + (i * delx)

            for i in range(n_val + 1):
                if x[i] <= 0.25:
                    u_new[i] = 1.0
                else:
                    u_new[i] = 0.0
                u_old[i] = u_new[i]

            for j in range(m):
                for i in range(1, n_val):
                    u_new[i] = u_old[i] - (lamda_val * (u_old[i] - u_old[i - 1]))  # Upwind scheme
                for i in range(1, n_val):
                    u_old[i] = u_new[i]

                for i in range(n_val + 1):
                    Location[i] = x[i] - a * j * delt

                for i in range(n_val + 1):
                    if Location[i] <= 0.25:
                        Exact[i] = 1.0
                    else:
                        Exact[i] = 0.0
                error = np.abs(u_new - Exact)
                errors.append(error)

            # Error analysis for the current grid resolution and Courant number
            mean_error = np.mean(errors)
            max_error = np.max(errors)

            print(f"Grid Resolution: {n_val}, Courant Number: {lamda_val}")
            print(f"Mean Error: {mean_error}")
            print(f"Max Error: {max_error}")
            np.savetxt(f'Upwind_scheme_x_{n}_{lamda_val}.txt', x, delimiter=',', fmt='%4.2f')
            np.savetxt(f'Upwind_scheme_u_new_{n}_{lamda_val}.txt', u_new, delimiter=',', fmt='%4.2f')
            np.savetxt(f'Upwind_scheme_EXACT_{n}_{lamda_val}.txt', Exact, delimiter=',', fmt='%4.2f')

            # Plot the results for each combination of n_val and lamda_val
            plt.plot(x, u_new, label=f'LAMDA={lamda_val}')

        plt.xlabel('GRID')
        plt.ylabel('U(x,t)')
        plt.legend()
        # Save the plot for each grid resolution
        plt.savefig(f'Upwind_SCHEME_{n_val}.png')
        plt.show()

main()
