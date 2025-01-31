# coding: utf-8

from numpy import zeros

nx = 1024

vecA = zeros(nx)
vecB = zeros(nx)
vecC = zeros(nx)

# Initialization of vectors
for i in range(0, nx):
    vecA[i] = 1.0/(nx-i+1)
    vecB[i] = vecA[i]**2

#$ acc parallel
#$ acc loop
for i in range(0, nx):
    vecC[i] = vecA[i] * vecB[i]
#$ acc end loop
#$ acc end parallel

# Compute the check value
c_sum = 0.0
for i in range(0, nx):
    c_sum += vecC[i]

print(' Reduction sum: ', c_sum)
