#%%cython -a

cimport numpy as np
cimport cython
from cython.parallel import prange, parallel
from libc.math cimport fabs
cimport openmp
from libc.stdio cimport printf

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef double sor(double[:, ::1] sxs, np.intp_t i1, np.intp_t i2) nogil:
    cdef double rich1, rich2, shared, s
    cdef np.intp_t j

    rich1 = 0
    rich2 = 0
    shared = 0
    
    for j in range(sxs.shape[1]):
        if (sxs[i1, j] == 1) and (sxs[i2, j] == 1):
            shared += 1 
        rich1 += sxs[i1, j]
        rich2 += sxs[i2, j]
    
    s = (2*shared) / ((2 * shared) + rich1 + rich2)
    return s
    
# function pointer
ctypedef double (*diss_ptr)(double[:, ::1], np.intp_t, np.intp_t)

@cython.boundscheck(False)
@cython.wraparound(False)
def sample_sitepairs(double[:, ::1] sxs,  double[:, ::1] outdata):
    cdef diss_ptr diss_func
    diss_func = &sor
   
    cdef np.intp_t i, j, n_sites, n_pairs, step, target, used
    
    target = outdata.shape[0]
    n_sites = sxs.shape[0]
    counter = 0    
    step = 0 # just a iterator, indicating the step
            
    # how to parallelise this?
    #with nogil, parallel(num_threads=2):
    #    for <what> in prange(<what>, schedule='dynamic'):
    #        for j in range(i+1, n_sites):
    
    while used < target:
        
        for i in range(n_sites):

            j = i + (step + 1)
            # D = openmp.omp_get_thread_num()
            outdata[used, 0] = i
            outdata[used, 1] = j
            outdata[used, 2] = sor(sxs, i, j)
            
            used += 1
            if used > target:
                break
            
        step += 1