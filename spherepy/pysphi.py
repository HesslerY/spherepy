# Copyright (C) 2015  Randy Direen <spherepy@direentech.com>
#
# This file is part of SpherePy.
#
# SpherePy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SpherePy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SpherePy.  If not, see <http://www.gnu.org/licenses/>


"""***************************************************************************

                   pysphi: Low Level Routines 

Randy Direen
2/11/2015

These routines are used in the process of calculating the scalar 
spherical harmonic coefficients from spherical pattern information.
For c versions, see csphi.c in src folder.

Credits:
The algorithms within this package have been implemented, in part, using the 
documentation within  the NIST Interagency/Internal Report (NISTIR) - 3955.
The majority or the code, however, has been developed using 
Ronald C. Wittmann's unpublished notes.

***************************************************************************"""

#---------------------------------------------------------------------Built-ins
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

#---------------------------------------------------------------------3rd Party
import numpy as np

# TODO: Change all xrange instances to range
# and do a 'from six.moves import range' here
from six.moves import xrange  # @UnresolvedImport

#==============================================================================
# Low Level Routines
#==============================================================================

def ynnm(n, m):
    """Initial value for recursion formula""" 
    a = 1.0 / np.sqrt(4.0 * np.pi)
    pm = np.abs(m)

    out = 0.0

    if(n < pm):
        out = 0.0
    elif(n == 0):
        out = a
    else:
        out = a
        for k in xrange(1, n + 1):
            out *= np.sqrt((2.0 * k + 1.0) / 8.0 / k)

        if(n != pm):
            for k in xrange(n - 1, pm - 1, -1):
                out *= np.sqrt((n + k + 1.0) / (n - k))
    return out

def ynunm(n, m, L):
    """Fourier coefficients for spherical harmonics"""

    out = np.zeros(L, dtype=np.float64)
    tmp1 = 0 
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0       
    if(np.abs(m) <= n):
        out[n] = ynnm(n, m)
        k = n - 2
        if(k >= 0):
            tmp1 = (n - k - 1.0) * (n + k + 2.0)
            tmp2 = (n - k - 2.0) * (n + k + 3.0) - 4.0 * m ** 2
            tmp4 = ((n - k) * (n + k + 1.0))
            out[k] = (tmp1 + tmp2) * out[k + 2] / tmp4

            for k in xrange(n - 4, -1, -2):
                tmp1 = (n - k - 1.0) * (n + k + 2.0)
                tmp2 = (n - k - 2.0) * (n + k + 3.0) - 4.0 * m ** 2
                tmp3 = (n - k - 3.0) * (n + k + 4.0);
                tmp4 = ((n - k) * (n + k + 1.0))
                out[k] = ((tmp1 + tmp2) * out[k + 2] - tmp3 * out[k + 4]) / tmp4
    return out    
    

def smallest_prime_factor(Q):
    """Find the smallest number factorable by the small primes 2, 3, 4, and 7 
    that is larger than the argument Q"""

    A = Q;
    while(A != 1):
        if(np.mod(A, 2) == 0):
            A = A / 2
        elif(np.mod(A, 3) == 0):
            A = A / 3
        elif(np.mod(A, 5) == 0):
            A = A / 5
        elif(np.mod(A, 7) == 0):
            A = A / 7;
        else:
            A = Q + 1;
            Q = A;

    return Q

def s_data(nrows_fdata, Nmax, Q):
    """ I am going to assume we will always have even data. This is pretty 
    safe because it means that we have measured both poles of the sphere and 
    have data that has been continued.

        nrows_fdata:  Number of rows in fdata.
        Nmax:         The largest number of n values desired.
        Q:            A value greater than nrows_fdata + Nmax. This can be
                      selected to be factorable into small primes to 
                      increase the speed of the fft (probably not that big 
                      of a deal today).

    """

    if np.mod(nrows_fdata, 2) == 1:
        raise Exception("nrows_fdata must be even.")
    
    L1 = nrows_fdata

    s = np.zeros(Q, dtype=np.complex128)
    MM = int(L1 / 2)

    for nu in xrange(-MM, MM + Nmax + 1):
        if np.mod(nu, 2) == 1:
            s[nu - MM] = -1j / nu

    return s

def hkm_fc(fdata, Nmax, m, s):
    """ Assume fdata has even rows"""

    f = fdata[:, m]
    L1 = f.size
    MM = int(L1 / 2)
    Q = s.size

    ff = np.zeros(Q, dtype=np.complex128)
    for n in xrange(MM, L1):
        ff[n] = f[n - MM]

    for n in xrange(0, MM):
        ff[n] = f[n + MM]

    # For larger problems, this speeds things up pretty good.
    F = np.fft.fft(ff)
    S = np.fft.fft(s)
    out = 4 * np.pi * np.fft.ifft(F * S)

    return out[0:Nmax + 1]

def bnm_vec_fc(fdata, Nmax, m):

    nrows = fdata.shape[0]
    Q = smallest_prime_factor(nrows + Nmax)
    s = s_data(nrows, Nmax, Q)
    h = hkm_fc(fdata, Nmax, m, s)

    absm = np.abs(m)

    out = np.zeros(Nmax - absm + 1, dtype=np.complex128)

    for n in xrange(absm, Nmax + 1):

        ynm = ynunm(n, m, n + 1)

        out[n - absm] = 1j ** (-m) * h[0] * ynm[0]

        if n != 0:
            out[n - absm] += 1j ** (-m) * 2 * np.sum(h[1:n + 1] * ynm[1:n + 1])
 
    return out

def fc_to_sc(gcoef, Nmax, Mmax):
    
    c = bnm_vec_fc(gcoef, Nmax, 0)
    
    for m in xrange(1, Mmax + 1):
        a = bnm_vec_fc(gcoef, Nmax, -m)  
        c = np.concatenate([c, a]) 
        a = bnm_vec_fc(gcoef, Nmax, m)  
        c = np.concatenate([c, a])

    return c

def mindx(m, nmax, mmax):
    """index to the first n value for a give m within the spherical 
    coefficients vector. Used by sc_to_fc"""

    ind = 0
    NN = nmax + 1

    if np.abs(m) > mmax:
        raise Exception("|m| cannot be larger than mmax")

    if (m != 0):
        ind = NN
        ii = 1
        for i in xrange(1, np.abs(m)):
            ind = ind + 2 * (NN - i)
            ii = i + 1

        if m > 0:
            ind = ind + NN - ii

    return ind

def fcvec_m_sc(vec, m, nmax, nrows):
    
    F = np.zeros(int(nrows), dtype=np.complex128)
    K = nmax + 1 

    for n in xrange(np.abs(m), K):
        
        ynm = ynunm(n, m, K)

        F[0:nmax + 1] += vec[n - np.abs(m)] * ynm.T

    F[0:K] = F[0:K] * 1j ** m

    mm = (-1) ** m
    if np.mod(nrows, 2) == 0:
        H = int(nrows / 2 - 1)
    else:
        H = int((nrows - 1) / 2)

    for k in xrange(0, H):
        F[-(k + 1)] = mm * F[k + 1]

    return F

def sc_to_fc(spvec, nmax, mmax, nrows, ncols):
    """assume Ncols is even"""

    fdata = np.zeros([int(nrows), ncols], dtype=np.complex128)

    for k in xrange(0, int(ncols / 2)):
        if k < mmax:
            kk = k
            ind = mindx(kk, nmax, mmax)
            vec = spvec[ind:ind + nmax - np.abs(kk) + 1]
            fdata[:, kk] = fcvec_m_sc(vec, kk, nmax, nrows)

            kk = -(k + 1)
            ind = mindx(kk, nmax, mmax)
            vec = spvec[ind:ind + nmax - np.abs(kk) + 1]
            fdata[:, kk] = fcvec_m_sc(vec, kk, nmax, nrows)

        if k == mmax:
            kk = k
            ind = mindx(kk, nmax, mmax)
            vec = spvec[ind:ind + nmax - np.abs(kk) + 1]
            fdata[:, kk] = fcvec_m_sc(vec, kk, nmax, nrows)

    return fdata   





   
