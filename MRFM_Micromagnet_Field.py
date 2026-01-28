import numpy as np
import matplotlib.pyplot as plt


def micromagnet_field(x, y, M_0, R_s):    
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(x, y)
    B_m = (4*np.pi/3) * M_0                  
    B_amp =       B_m * R_s**3 / r**3
    dBdr  = - 3 * B_m * R_s**3 / r**4
    B_transverse = (3/2) * B_amp * np.sin(2*theta)
    B_axial      = (1/2) * B_amp * (3*np.cos(2*theta) + 1)
    B_transverse = np.where(x**2+y**2>R_s**2, B_transverse, 0)
    B_axial      = np.where(x**2+y**2>R_s**2, B_axial, 0)
    grad_B = dBdr * (1/2) * (3*np.cos(2*theta)+1) * np.cos(theta) + (B_amp/r) * 3 * np.sin(2*theta) * np.sin(theta)
    return B_transverse, B_axial, grad_B

def gradient(x, y, z, M_0, R_s):
    r = np.sqrt(x**2 + y**2 + z**2)
    xy = np.sqrt(x**2 + y**2)
    theta = np.arctan2(xy, z)
    B_m = (4*np.pi/3) * M_0                  
    B_amp =       B_m * R_s**3 / r**3
    dBdr  = - 3 * B_m * R_s**3 / r**4
    grad_B = dBdr * (1/2) * (3*np.cos(2*theta)+1) * np.cos(theta) + (B_amp/r) * 3 * np.sin(2*theta) * np.sin(theta)
    return grad_B
    
def resonance_slice(x, y, B_x, B_y, B_rf, omega_rf, B_0, T1, T2):
    g_L = 2                                        # Lande g-factor for elementary fermions 
    e = 1.602e-19                                  # C
    m_e = 9.1e-31                                  # kg
    gamma = g_L*e / (2*m_e)                        # rad / Ts           (For Hz/T, divide by 2 pi)
    
    B_total_y = B_y + B_0
    B_total = np.sqrt(B_x**2 + B_total_y**2)
    B_resonant = omega_rf / gamma
    delta_omega = np.sqrt(1 + gamma**2 * B_rf**2 * T1 * T2) / T2
    delta_B = delta_omega / gamma
    B_lower = B_resonant - delta_B
    B_upper = B_resonant + delta_B
    
    CS = plt.contour(x, y, B_total, levels=[B_lower, B_resonant, B_upper], 
                    colors=['yellow', 'yellow', 'yellow'], linewidths=[0, 0, 0],
                    linestyles=['--', '--', '--'])
    
    lower_contours = CS.allsegs[0]
    upper_contours = CS.allsegs[2]
    for i, contour in enumerate(lower_contours):
        x_lower = contour[:, 0]
        y_lower = contour[:, 1]
    for i, contour in enumerate(upper_contours):
        x_upper = contour[:, 0]
        y_upper = contour[:, 1]
    return x_lower, -y_lower, x_upper, -y_upper
    
def check_res_region(x,y,z, r_lower, z_lower, r_upper, z_upper):
    r = np.sqrt(x**2 + y**2)
    if z < np.min(z_lower): return 0
    if (z < np.min(z_upper)):
        r_min = 0
        r_max = np.max(r_lower[z_lower<z])
    else:
        r_min = r_upper[z_upper == np.min(z_upper[z_upper>z])]; r_min = r_min[r_min>0][0]
        r_max = r_lower[z_lower == np.min(z_lower[z_lower>z])]; r_max = r_max[r_max>0][0]
    if (r <= r_max) & (r >= r_min): return 1
    else:                           return 0