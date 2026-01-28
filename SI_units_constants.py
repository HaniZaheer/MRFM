import numpy as np

nano = 1e-9; micro = 1e-6; milli = 1e-3; centi = 1e-2; kilo = 1e+3; Mega = 1e+6; Giga = 1e+9

c = 3e+8                                       # m / s
h = 6.62607015e-34                             # J / Hz
hbar = h / (2 * np.pi)                         # J / Hz
e = 1.602e-19                                  # C
m_e = 9.1e-31                                  # kg
k_B = 1.38e-23                                 # J / K
epsilon_0 = 8.85e-12                           # C s^2 / (kg m^3)
mu_0 = 1.26e-6                                 # N A^-2 
alpha = e**2 / (4*np.pi*epsilon_0 * hbar * c) 
G_N = 6.6743e-11                               # Newton's Grav const (m^3 / (kg s^2))
M_Pl = np.sqrt(hbar * c / G_N)                 # kg
mu_B = e * hbar / (2 * m_e)                    # J/T
g_L = 2                                        # Lande g-factor for elementary fermions 
gamma = g_L*e / (2*m_e)                        # rad / Ts           (For Hz/T, divide by 2 pi)

eV = 1.602e-19                                 # J

meter = 1
sec = 1
kg = 1

minute = 60 * sec
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 365 * day
gram = 1e-3 * kg

Hz = 1
Kelvin = 1
Tesla = 1
Gauss = 1e-4                                   # T
Watts = 1