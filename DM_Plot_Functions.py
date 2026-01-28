import numpy as np
from SI_units_constants import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
from Axion import B_ae

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
    
def plot_gae(m_lim, y_lim): # Note: Data taken from Ciaran O'hare's AxionLimits: https://cajohare.github.io/AxionLimits/
    fig, ax = plt.subplots(1, 1)
    
    ##################################################################### QCD Axion
    # Mass-coupling relation
    def g_x(C_ae,m_a):
        return 8.943e-11*C_ae*m_a
    DFSZ_u = 1.0/3.0
    DFSZ_l = 2.0e-5
    # QCD Axion models
    n = 200
    m_QCD = np.logspace(-20,10,n)
    # DFSZ
    cmap = plt.get_cmap('YlOrBr');
    colorlist = cmap([0.3, 0.5])
    col = colorlist[0]
    plt.fill_between(m_QCD,g_x(DFSZ_l,m_QCD),y2=g_x(DFSZ_u,m_QCD),facecolor=col,zorder=0,alpha=0.2)
    plt.plot(m_QCD,g_x(DFSZ_l,m_QCD),'k-',lw=3,zorder=0)
    plt.plot(m_QCD,g_x(DFSZ_u,m_QCD),'k-',lw=3,zorder=0)
    plt.plot(m_QCD,g_x(DFSZ_l,m_QCD),'-',lw=2,zorder=0,color=col)
    plt.plot(m_QCD,g_x(DFSZ_u,m_QCD),'-',lw=2,zorder=0,color=col)
    plt.text(1.5e-5, 3e-17, r'${\bf QCD~Axion}$', fontsize=13, rotation=8, color=col)
    
    ##################################################################### Red Giants arXiv:[2007.03694]
    cmap = plt.get_cmap('Greys')
    colorlist = cmap([0.4, 0.5, 0.6, 0.8, 0.9])
    col = colorlist[0]
    m_RedGiant = [1e-30, 1e4]
    g_RedGiant = [1.3e-13, 1.3e-13]
    plt.fill_between(m_RedGiant, g_RedGiant, y2=1e0, edgecolor=None, facecolor=col, zorder=0.5)
    plt.plot(m_RedGiant, g_RedGiant, color='k', zorder=0.5, lw=1)
    plt.text(2e-5, 3e-13, r'${\bf Red\ giants\ (}\omega{\bf Cen)}$', fontsize=13, color='w', ha='center')
    
    ##################################################################### XENONnT Solar (Solar axions)
    col = colorlist[1]
    m_XENON = [1e-30, 1e3]
    g_XENON = [1.9e-12, 1.9e-12]
    plt.fill_between(m_XENON, g_XENON ,y2=1e0,edgecolor=None,facecolor=col,zorder=0.51)
    plt.plot(m_XENON, g_XENON, color='k',zorder=0.51,lw=1)
    plt.text(2e-5, 4e-12, r'${\bf XENONnT\ (Solar\ axions)}$', fontsize=13, color='w', ha='center')
    
    ##################################################################### Solar Neutrino arXiv:[0807.2926]
    col = colorlist[2]
    m_Neutrino = [1e-30, 7.6]
    g_Neutrino = [2.8e-11, 2.8e-11]
    plt.fill_between(m_Neutrino, g_Neutrino,y2=1e0,edgecolor=None,facecolor=col,zorder=0.52)
    plt.plot(m_Neutrino, g_Neutrino,color='k',zorder=0.52,lw=1)
    plt.text(2e-5, 5e-11, r'${\bf Solar}\ \nu$', fontsize=13, color='w',ha='center')
    
    ##################################################################### Torsion Pendulum Spin (Dipole-Dipole)
    col=colorlist[3]
    m_Torsion = [1e-30, 1.266930683530601e-06, 1.676491694477114e-06, 2.21845159974992e-06, 2.9356110242872213e-06, 3.8846067621615595e-06, 5.140384598567608e-06, 6.802118062135043e-06, 9.001040533838034e-06, 1.1910809243785043e-05, 1.5761219639941374e-05, 2.0856353204388105e-05, 2.7598591918855336e-05, 3.407920472453255e-05, 4.122777274001811e-05, 4.8531888206079554e-05, 5.560933214388014e-05, 6.394882667615049e-05, 7.500763723010296e-05, 8.462158047617638e-05, 9.32438620461246e-05, 0.00010778076092491845, 0.00012881129908371374, 0.00014817612598787906, 0.000166166530787644, 0.00018872887412421072, 0.00020707351608490889, 0.0002276149021133836, 0.00024657975761250704, 0.0002661547976730642, 0.00028437249815630876, 0.0003061671383862972, 0.0003304725966167985, 0.00035670757381170697, 0.0003831346687013243, 0.00040514186869012746, 0.00042739648033048386, 0.00045598682532047767, 0.00048419448862059144, 0.0005122801608923314, 0.0005374790918815653, 0.0005670164030968797, 0.0005971092745518933]
    g_Torsion = [7.453971333659431e-09, 7.453971333659431e-09, 7.453971333659431e-09, 7.453971333659431e-09, 7.453971333659431e-09, 7.453971333659431e-09, 7.453971333659431e-09, 7.469307503276738e-09, 7.538711678293687e-09, 7.624415392075382e-09, 7.711093427050064e-09, 7.806775511611241e-09, 7.985286863718635e-09, 8.223284228082143e-09, 8.63026879656999e-09, 9.069811477687712e-09, 9.5056619263185e-09, 1.0224201815644511e-08, 1.1256644164499918e-08, 1.2563581376677991e-08, 1.3656047592811208e-08, 1.612335192025396e-08, 2.0773423092981142e-08, 2.67394014589653e-08, 3.409605376624091e-08, 4.4891752887496654e-08, 5.758251081025538e-08, 7.528594085146245e-08, 9.885699846374322e-08, 1.3015770026231019e-07, 1.7423395267248776e-07, 2.369566457912563e-07, 3.3262229964011513e-07, 4.66910703637084e-07, 6.51635278102568e-07, 8.694641671143109e-07, 0.0000011353085187963445, 0.0000016295771523656133, 0.000002298589562983418, 0.0000033110475672423857, 0.0000046749043603002525, 0.000006531544693056722, 0.000008924652256748185]
    plt.fill_between(m_Torsion, g_Torsion, y2=1e0,edgecolor=None,facecolor=col,zorder=1)
    plt.plot(m_Torsion, g_Torsion, 'k-',zorder=1,lw=1)
    plt.text(9e-6, 1e-7, r'${\bf Torsion\ pendulum}$', fontsize=13, color='w', zorder=10, ha='center')
    plt.text(9e-6, 2e-8, r'${\bf (dipole-dipole\ force)}$', fontsize=13, color='w', zorder=9, ha='center')
    
    ##################################################################### Electron g-2
    col=colorlist[4]
    m_gminus2 = [1e-30, 511e3]
    g_gminus2 = [6.6e-6, 6.6e-6]
    plt.fill_between(m_gminus2, g_gminus2, y2=1e0,edgecolor=None,facecolor=col,zorder=1.1)
    plt.plot(m_gminus2, g_gminus2, 'k-',zorder=1.1,lw=1)
    plt.text(9e-6, 1e-5, r'${\bf Electron\ g-2}$', fontsize=15, color='w',zorder=5, ha='center')
    
    ##################################################################### QUAX https://inspirehep.net/literature/1777123
    cmap = plt.get_cmap('OrRd')
    cmap = plt.get_cmap('Greens')
    colorlist = cmap([0.1, 0.4, 1])
    colorlist = cmap([1, 0.4, 0.1])
    col=colorlist[0]
    m_QUAX = [4.136908888749909e-05, 4.136908888749909e-05, 4.1611061061927757e-05, 4.1611061061927757e-05, 4.177316162421358e-05, 4.175286457015867e-05, 4.181378533775264e-05, 4.181378533775264e-05, 4.1935893667447475e-05, 4.1935893667447475e-05, 4.2058358588732e-05, 4.2058358588732e-05, 5.956320923634291e-05, 5.956320923634291e-05, 5.956320923634291e-05]
    g_QUAX = [1.0, 2.0648742907960882e-11, 2.0648742907960882e-11, 1.731003206419415e-11, 1.731003206419415e-11, 2.0447409650077636e-11, 2.0447409650077636e-11, 1.0, 1.0, 1.9469809495012833e-11, 1.9469809495012833e-11, 1.0, 1.0, 5.776996809084501e-10, 1.0]
    plt.fill_between(m_QUAX, g_QUAX, y2=1e0,color=col,alpha=1,zorder=3)
    plt.plot(m_QUAX, g_QUAX, '-',color=col,alpha=1.0,zorder=3,lw=1)
    plt.text(46e-6, 1e-10, r'${\bf QUAX}$', fontsize=15, color=col, rotation = -90)
    
    ##################################################################### UWA
    col=colorlist[1]
    m_UWA = [33.79e-6, 33.79e-6, 33.94e-6, 33.94e-6]
    g_UWA = [1e0, 3.7e-9, 3.7e-9, 1e0]
    plt.fill_between(m_UWA, g_UWA, y2=1e0,color=col,alpha=1,zorder=3)
    plt.plot(m_UWA, g_UWA, '-',color=col,alpha=0.5,zorder=3,lw=1)
    plt.text(2.8e-5, 3e-9, r'${\bf UWA}$', fontsize=15, color=col, rotation = 90)
    
    ##################################################################### Magnon QND
    col=colorlist[2]
    m_QND = [0.00003311570288978592, 0.00003311570288978592, 0.00003313027509898091, 0.00003313027509898091]
    g_QND = [1.0e0, 2.6e-6, 2.6e-6, 1.0e0]
    plt.fill_between(m_QND, g_QND, y2=1e0,color=col,alpha=1,zorder=3.1)
    plt.plot(m_QND, g_QND, '-',color=col,alpha=1.0,zorder=3.1,lw=1)
    plt.text(2.8e-5, 1e-6, r'${\bf QND}$', fontsize=15, color=col, rotation = 90)

    ax.tick_params(axis='both', which='both', direction='in')
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Computer Modern sans serif']
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams.update({'font.size': 15,'font.family':'STIXGeneral'})
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.xlabel(r'$m_{\rm DM}\ [\text{eV}/c^2]$', fontsize = 20)
    plt.ylabel(r'$|g_{aee}|$', fontsize = 20)
    
    x_lim = m_lim
    plt.xlim(x_lim[0], x_lim[1])
    plt.ylim(y_lim[0], y_lim[1])
    
    return fig, ax

def plot_darkphoton(m_lim):
    fig, ax = plt.subplots(1, 1)


    ##################################################################### Haloscopes
    y2 = 1e10

    cmap = plt.get_cmap('Greys')
    colorlist = cmap([0.4, 0.6, 0.8])
    col=colorlist[0]
    dat = np.loadtxt('limit_data/DarkPhoton/DP_Combined_Stellar.txt')
    
    col=colorlist[1]
    dat = np.loadtxt('limit_data/DarkPhoton/DP_Combined_Laboratory.txt')
    
    col=colorlist[2]
    dat = np.loadtxt('limit_data/DarkPhoton/DM_combined.txt')
    zo =0.3
    plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,alpha=1,zorder=0)
    plt.text(3e-6, 3e-11, r'$\rm DPDM$', color='w')
    
    cmap = plt.get_cmap('Greens')
    colorlist = cmap([1, 0.4, 0.1])
    col=colorlist[0]
    dat = np.loadtxt('limit_data/DarkPhoton/DP_Combined_DarkMatterSearches.txt')
    plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=-1,lw=2.5)
    plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,alpha=1,zorder=-1)
    plt.text(2.7e-5, 8e-14, r'$\rm Haloscopes$', color=col, rotation=90)
    
    col=colorlist[1]
    dat = np.loadtxt('limit_data/DarkPhoton/DP_Combined_AxionSearchesRescaled.txt')
    plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=-1,lw=2.5)
    plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,alpha=1,zorder=-1)
    plt.text(1e-5, 8e-15, r'$\rm Rescaled$', color=col)
    plt.text(1e-5, 4e-15, r'$\rm Axion~Searches$', color=col)

    ax.tick_params(axis='both', which='both', direction='in')
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Computer Modern sans serif']
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams.update({'font.size': 15,'font.family':'STIXGeneral'})
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.xlabel(r'$m_{\rm DM}\ [\text{eV}/c^2]$', fontsize = 20)
    plt.ylabel(r'$\epsilon$', fontsize = 20)
    
    x_lim = m_lim
    y_lim = [1e-15, 1e-10]
    plt.xlim(x_lim[0], x_lim[1])
    plt.ylim(y_lim[0], y_lim[1])
    
    return fig, ax
