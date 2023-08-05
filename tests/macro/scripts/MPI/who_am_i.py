# coding: utf-8
from mpi4py import MPI

# we need to declare these variables somehow,
# since we are calling mpi subroutines
size = -1
rank = -1
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print('I process ', rank, ', among ', size, ' processes')

