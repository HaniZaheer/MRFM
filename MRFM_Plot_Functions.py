import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm
import matplotlib as mpl
from matplotlib import rcParams

from MRFM_Micromagnet_Field import micromagnet_field, gradient

h = 6.62607015e-34                             # J / Hz
hbar = h / (2 * np.pi)                         # J / Hz
eV = 1.602e-19                                 # J

def plot_micromagnet(R_s):
    x_sphere = np.linspace(-R_s, R_s, 100)
    plt.plot(x_sphere, np.sqrt(R_s**2 - x_sphere**2), 'r')
    plt.plot(x_sphere, -np.sqrt(R_s**2 - x_sphere**2), 'r')

def plot_gradient(x, y, grad_B, size):
    im = plt.imshow(grad_B, 
               extent=[-size, size, -size, size],
               cmap='RdBu_r',  # Diverging colormap for positive/negative values
               norm=SymLogNorm(linthresh=1e-4,  # Threshold for linear scale near zero
                               linscale=0.5,    # Relative size of linear region
                               vmin=-1e-2, 
                               vmax=1e-1),
               origin='lower')

    plt.colorbar(im, label=r'$\frac{\partial B^{\rm dipole}_z}{\partial z}\ (T/m)$', pad=0.15)
    levels = [1e-3, 1e-2, 1e-1]
    FS = plt.contour(x, y, np.abs(grad_B), levels=levels, 
                    colors='white', linewidths=1.5, linestyles=':')

def plot_resonance_slice(x, y, B_x, B_y, B_rf, omega_rf, B_0, T1, T2):
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
    
    plt.contour(x, y, B_total, levels=[B_lower, B_resonant, B_upper], 
                    colors=['yellow', 'yellow', 'yellow'], linewidths=[1, 0.5, 1],
                    linestyles=['--', '--', '--'])
    
    plt.contourf(x, y, B_total, levels=[B_lower, B_upper],
             colors=['yellow', 'yellow'], alpha=0.4, hatches=['', '////'])


def axion_magnetic_field_axis(ax_y, g_lim):
    ax_y.set_ylim(B_ae(g_lim[0]), B_ae(g_lim[1]))
    ax_y.set_yscale('log')
    ax_y.set_ylabel(r'$B_a~[\rm T]$', fontsize = 20)
    ax_y.tick_params(direction="in")
def frequency_axis(ax_x, m_lim):
    f_lim = np.array(m_lim) * eV/(2*np.pi*hbar)
    ax_x.set_xlim(f_lim[0], f_lim[1])
    ax_x.set_xscale('log')
    ax_x.set_xlabel(r'$f_{\rm DM}~[\rm Hz]$', fontsize = 20, labelpad=10)
    ax_x.tick_params(axis='both', which='both', direction='in')