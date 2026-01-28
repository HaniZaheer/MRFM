import numpy as np
from SI_units_constants import *

rho_DM = 0.4 * (Giga*eV / centi**3)     # Some papers use 0.3 GeV/cm^3
v_DM = 1e-3 * c                         # Dark matter virial velocity
g_e = 2                                 # Electron g-factor

def tau_c(E_a):
    f_a = E_a / (2*np.pi*hbar)
    return c**2 / (f_a * v_DM**2)
def B_ae(g_ae):
    grad_a = v_DM/c**2 * np.sqrt(2*rho_DM)
    return 2*np.sqrt(hbar*c)/(g_e*e) * grad_a * g_ae
def g_ae(B_ae):
    grad_a = v_DM/c**2 * np.sqrt(2*rho_DM)
    return g_e*e/(2*np.sqrt(hbar*c)) / grad_a * B_ae

def B_Ap(epsilon, m_Ap, L):
    J_eff = np.sqrt(2*rho_DM/mu_0) * c/hbar * epsilon * m_Ap
    return mu_0 * J_eff * L
def epsilon(B_Ap, m_Ap, L):
    J_eff = B_Ap / (mu_0 * L)
    return J_eff / (np.sqrt(2*rho_DM/mu_0) * c/hbar * m_Ap)
def B_agamma(g_agamma, B0, L):
    m_a = 1                        # divided out
    w_a = m_a*c**2/hbar
    a_0 = np.sqrt(2*rho_DM)/w_a
    J_eff = np.sqrt(c**5/hbar) * (g_agamma*m_a*a_0/mu_0) * B0
    return mu_0 * J_eff * L
def g_agamma(B_agamma, B0, L):
    m_a = 1                        # divided out
    w_a = m_a*c**2/hbar
    a_0 = np.sqrt(2*rho_DM)/w_a
    J_eff = B_agamma / (mu_0 * L)
    return J_eff / (np.sqrt(c**5/hbar) * (m_a*a_0/mu_0) * B0)