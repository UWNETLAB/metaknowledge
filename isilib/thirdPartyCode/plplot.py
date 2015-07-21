import matplotlib.pyplot as plt
from math import *

# function h=plplot(x, xmin, alpha)
# PLPLOT visualizes a power-law distributional model with empirical data.
#    Source: http://www.santafe.edu/~aaronc/powerlaws/
#
#    PLPLOT  REQUIRES  the use of the free library: matplotlib
#
#    PLPLOT(x, xmin, alpha) plots (on log axes) the data contained in x 
#    and a power-law distribution of the form p(x) ~ x^-alpha for 
#    x >= xmin. For additional customization, PLPLOT returns a pair of 
#    handles, one to the empirical and one to the fitted data series. By 
#    default, the empirical data is plotted as 'bo' and the fitted form is
#    plotted as 'k--'. PLPLOT automatically detects whether x is composed 
#    of real or integer values, and applies the appropriate plotting 
#    method. For discrete data, if min(x) > 50, PLFIT uses the continuous 
#    approximation, which is a reliable in this regime.
#
#    Example:
#       xmin  = 47;
#       alpha = 2.71;
#       x = [500,150,90,81,75,75,70,65,60,58,49,47,40]
#       h = plplot(x,xmin,alpha);
#
#    For more information, try 'type plplot'
#
#    See also PLFIT, PLVAR, PLPVA

# Version 1.0   (2008 February)
# Ported to python by Joel Ornstein(2011 July)
# (joel_ornstein@hmc.edu)

# Copyright (C) 2008-2011 Aaron Clauset (Santa Fe Institute)
# Distributed under GPL 2.0
# http://www.gnu.org/copyleft/gpl.html
# PLFIT comes with ABSOLUTELY NO WARRANTY
# 
# The 'zeta' helper function is modified from the open-source library 'mpmath'
#   mpmath: a Python library for arbitrary-precision floating-point arithmetic
#   http://code.google.com/p/mpmath/
#   version 0.17 (February 2011) by Fredrik Johansson and others
# 
# No Notes
#

def plplot(x,xmin,alpha):
        # select method (discrete or continuous) for fitting
    if     reduce(lambda X,Y:X==True and floor(Y)==float(Y),x,True): f_dattype = 'INTS'
    elif reduce(lambda X,Y:X==True and (type(Y)==int or type(Y)==float or type(Y)==long),x,True):    f_dattype = 'REAL'
    else:                 f_dattype = 'UNKN'
    
    if f_dattype=='INTS' and min(x) > 1000 and len(x)>100:
        f_dattype = 'REAL'
    plt.close()
    plt.ion()
    h=[[],[]]
    # estimate xmin and alpha, accordingly
    if f_dattype== 'REAL':
        n = len(x)
        c1 = sorted(x)
        c2 = map(lambda X:X/float(n),range(n,0,-1))
        q = sorted(filter(lambda X:X>=xmin,x))
        cf = map(lambda X:pow(float(X)/xmin,1.-alpha),q)
        cf = map(lambda X:X*float(c2[c1.index(q[0])]),cf)

        h[0]=plt.loglog(c1, c2, 'bo',markersize=8,markerfacecolor=[1,1,1],markeredgecolor=[0,0,1])
        h[1]=plt.loglog(q, cf, 'k--',linewidth=2)
        
        xr1 = pow(10,floor(log(min(x),10)))
        xr2 = pow(10,ceil(log(min(x),10)))
        yr1 = pow(10,floor(log(1./n,10)))
        yr2 = 1
        

        plt.axhspan(ymin=yr1,ymax=yr2,xmin=xr1,xmax=xr2)
        plt.ylabel('Pr(X >= x)',fontsize=16);
        plt.xlabel('x',fontsize=16)
        plt.draw()
        
    elif f_dattype== 'INTS':
        n = len(x)
        q = sorted(unique(x))
        c=[]
        for Q in q:
            c.append(len(filter(lambda X: floor(X)==Q,x))/float(n))
        c1 = q+[q[-1]+1]
        c2 = map(lambda Z: 1.-Z,reduce(lambda X,Y: X+[Y+X[-1]],c,[0]))
        c2 = filter(lambda X:float(X)>=pow(10,-10.),c2)
        c1 = c1[0:len(c2)]
        cf = map(lambda X:pow(X,-alpha)/(float(zeta(alpha)) - sum(map(lambda Y:pow(Y,-alpha),range(1,xmin)))),range(xmin,q[-1]+1))
        cf1 = range(xmin,q[-1]+2)
        cf2 = map(lambda Z: 1.-Z,reduce(lambda X,Y: X+[Y+X[-1]],cf,[0]))
        cf2 = map(lambda X: X*float(c2[c1.index(xmin)]),cf2)

        h[0]=plt.loglog(c1, c2, 'bo',markersize=8,markerfacecolor=[1,1,1],markeredgecolor=[0,0,1])
        h[1]=plt.loglog(cf1, cf2, 'k--',linewidth=2)
        
        xr1 = pow(10,floor(log(min(x),10)))
        xr2 = pow(10,ceil(log(min(x),10)))
        yr1 = pow(10,floor(log(1./n,10)))
        yr2 = 1


        plt.axhspan(ymin=yr1,ymax=yr2,xmin=xr1,xmax=xr2)
        plt.ylabel('Pr(X >= x)',fontsize=16);
        plt.xlabel('x',fontsize=16)
        plt.draw()
                 
          

    return h

# helper functions (unique and zeta)


def unique(seq): 
    # not order preserving 
    set = {} 
    map(set.__setitem__, seq, []) 
    return set.keys()

def _polyval(coeffs, x):
    p = coeffs[0]
    for c in coeffs[1:]:
        p = c + x*p
    return p

_zeta_int = [\
-0.5,
0.0,
1.6449340668482264365,1.2020569031595942854,1.0823232337111381915,
1.0369277551433699263,1.0173430619844491397,1.0083492773819228268,
1.0040773561979443394,1.0020083928260822144,1.0009945751278180853,
1.0004941886041194646,1.0002460865533080483,1.0001227133475784891,
1.0000612481350587048,1.0000305882363070205,1.0000152822594086519,
1.0000076371976378998,1.0000038172932649998,1.0000019082127165539,
1.0000009539620338728,1.0000004769329867878,1.0000002384505027277,
1.0000001192199259653,1.0000000596081890513,1.0000000298035035147,
1.0000000149015548284]

_zeta_P = [-3.50000000087575873, -0.701274355654678147,
-0.0672313458590012612, -0.00398731457954257841,
-0.000160948723019303141, -4.67633010038383371e-6,
-1.02078104417700585e-7, -1.68030037095896287e-9,
-1.85231868742346722e-11][::-1]

_zeta_Q = [1.00000000000000000, -0.936552848762465319,
-0.0588835413263763741, -0.00441498861482948666,
-0.000143416758067432622, -5.10691659585090782e-6,
-9.58813053268913799e-8, -1.72963791443181972e-9,
-1.83527919681474132e-11][::-1]

_zeta_1 = [3.03768838606128127e-10, -1.21924525236601262e-8,
2.01201845887608893e-7, -1.53917240683468381e-6,
-5.09890411005967954e-7, 0.000122464707271619326,
-0.000905721539353130232, -0.00239315326074843037,
0.084239750013159168, 0.418938517907442414, 0.500000001921884009]

_zeta_0 = [-3.46092485016748794e-10, -6.42610089468292485e-9,
1.76409071536679773e-7, -1.47141263991560698e-6, -6.38880222546167613e-7,
0.000122641099800668209, -0.000905894913516772796, -0.00239303348507992713,
0.0842396947501199816, 0.418938533204660256, 0.500000000000000052]

def zeta(s):
    """
    Riemann zeta function, real argument
    """
    if not isinstance(s, (float, int)):
        try:
            s = float(s)
        except (ValueError, TypeError):
            try:
                s = complex(s)
                if not s.imag:
                    return complex(zeta(s.real))
            except (ValueError, TypeError):
                pass
            raise NotImplementedError
    if s == 1:
        raise ValueError("zeta(1) pole")
    if s >= 27:
        return 1.0 + 2.0**(-s) + 3.0**(-s)
    n = int(s)
    if n == s:
        if n >= 0:
            return _zeta_int[n]
        if not (n % 2):
            return 0.0
    if s <= 0.0:
        return 0
    if s <= 2.0:
        if s <= 1.0:
            return _polyval(_zeta_0,s)/(s-1)
        return _polyval(_zeta_1,s)/(s-1)
    z = _polyval(_zeta_P,s) / _polyval(_zeta_Q,s)
    return 1.0 + 2.0**(-s) + 3.0**(-s) + 4.0**(-s)*z



    
