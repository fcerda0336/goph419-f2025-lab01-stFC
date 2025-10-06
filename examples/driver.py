# examples/driver.py

import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt

# Add src folder to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import your functions
from goph419lab01.functions import sqrt, arcsin, launch_angle_range

# Create figures folder if it doesn't exist
figures_path = os.path.join(os.path.dirname(__file__), '../figures')
os.makedirs(figures_path, exist_ok=True)

def main():
    # -----------------------------
    # Deliverable 1: sqrt(x)
    # -----------------------------
    while True:
        try:
            x = float(input("Enter a positive number 0.0 <= x <= 2.5 for sqrt: "))
            if x < 0.0 or x > 2.5:
                raise ValueError("Input out of range.")
            y_sqrt = sqrt(x)
            print(f"sqrt({x}) ≈ {y_sqrt:.8f}\n")
            break
        except ValueError as e:
            print(e)
            print("Please choose another number within the valid range.\n")

    # -----------------------------
    # Deliverable 2: arcsin(x)
    # -----------------------------
    while True:
        try:
            x_asin = float(input("Enter a number 0.0 <= x <= 1.0 for arcsin: "))
            if x_asin < 0.0 or x_asin > 1.0:
                raise ValueError("Input out of range.")
            y_asin = arcsin(x_asin)
            print(f"arcsin({x_asin}) ≈ {y_asin:.8f} radians ≈ {math.degrees(y_asin):.4f} degrees\n")
            break
        except ValueError as e:
            print(e)
            print("Please choose another number within the valid range.\n")

    # -----------------------------
    # Deliverable 3 & 4: launch_angle_range
    # -----------------------------
    while True:
        try:
            ve_v0 = float(input("Enter escape velocity ratio ve/v0: "))
            alpha = float(input("Enter maximum altitude fraction alpha: "))
            tol_alpha = float(input("Enter tolerance tol_alpha: "))
            phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
            print(f"Minimum launch angle: {math.degrees(phi_range[0]):.4f} deg")
            print(f"Maximum launch angle: {math.degrees(phi_range[1]):.4f} deg\n")
            break
        except ValueError as e:
            print(f"Error in computing launch angles: {e}")
            print("Please choose valid parameters.\n")

    # -----------------------------
    # Deliverable 5: Plot launch angles vs alpha
    # -----------------------------
    ve_v0_fixed = 2.0
    alpha_values = np.linspace(0.01, 0.3, 50)
    min_angles = []
    max_angles = []

    for alpha_i in alpha_values:
        phi_min, phi_max = launch_angle_range(ve_v0_fixed, alpha_i, tol_alpha=0.04)
        min_angles.append(math.degrees(phi_min))
        max_angles.append(math.degrees(phi_max))

    plt.figure()
    plt.plot(alpha_values, min_angles, label='Minimum launch angle')
    plt.plot(alpha_values, max_angles, label='Maximum launch angle')
    plt.xlabel('Alpha (fraction of Earth radius)')
    plt.ylabel('Launch angle (deg)')
    plt.title(f'Launch angles vs Alpha (ve/v0={ve_v0_fixed})')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(figures_path, 'launch_angle_vs_alpha.png'))
    print("Figure saved as figures/launch_angle_vs_alpha.png\n")

    # -----------------------------
    # Deliverable 6: Plot launch angles vs ve/v0
    # -----------------------------
    alpha_fixed = 0.25
    ve_v0_values = np.linspace(1.5, 2.2, 50)
    min_angles_v = []
    max_angles_v = []

    for ve_v0_i in ve_v0_values:
        phi_min, phi_max = launch_angle_range(ve_v0_i, alpha_fixed, tol_alpha=0.04)
        min_angles_v.append(math.degrees(phi_min))
        max_angles_v.append(math.degrees(phi_max))

    plt.figure()
    plt.plot(ve_v0_values, min_angles_v, label='Minimum launch angle')
    plt.plot(ve_v0_values, max_angles_v, label='Maximum launch angle')
    plt.xlabel('ve/v0')
    plt.ylabel('Launch angle (deg)')
    plt.title(f'Launch angles vs ve/v0 (alpha={alpha_fixed})')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(figures_path, 'launch_angle_vs_vev0.png'))
    print("Figure saved as figures/launch_angle_vs_vev0.png\n")

    # -----------------------------
    # Deliverable 7: Error propagation example
    # -----------------------------
    ve_v0_err = 0.05
    alpha_err = 0.02
    ve_v0_val = 2.0
    alpha_val = 0.25

    # Example calculation of error in sin(phi0)
    sin_phi0 = alpha_val / ve_v0_val
    d_sin_phi0_d_alpha = 1 / ve_v0_val
    d_sin_phi0_d_vev0 = -alpha_val / (ve_v0_val**2)

    delta_sin_phi0 = math.sqrt((d_sin_phi0_d_alpha * alpha_err)**2 +
                               (d_sin_phi0_d_vev0 * ve_v0_err)**2)
    print(f"Estimated error in sin(phi0): Δ(sin φ0) ≈ {delta_sin_phi0:.5f}")

if __name__ == "__main__":
    main()