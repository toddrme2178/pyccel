from mpi4py import MPI

rank = -1
#we must initialize rank
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

root = 0

if rank == 0:
    value = 1000
else:
    value = rank

sum_value = 0

sum_value = comm.allreduce (value, MPI.SUM)

print('I, process ', root,', have the global sum value ', sum_value)


