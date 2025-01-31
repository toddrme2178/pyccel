# coding: utf-8
from mpi4py import MPI
from numpy import zeros

# we need to declare these variables somehow,
# since we are calling mpi subroutines
size_ = -1
rank = -1
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size_ = comm.Get_size()

n = 10
x = zeros(n,'double')

if rank == 0:
    x[:] = 1.0

source = 0

if rank == source:
    x[1] = 2.0
    comm.Send(x[1], 1, tag=1234)
    print("> processor ", rank, " sent x(1) = ", x)
# ...

