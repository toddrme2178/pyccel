from mpi4py import MPI

# we must initialize rank and size
rank = -1
size = -1

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Send messages around in a ring
source = (rank - 1) % size
dest   = (rank + 1) % size

# Create message to be sent, initialize receive buffer, choose some tag
msg = rank + 1000
val = -1
tag = 1234

val = comm.Sendrecv( msg, dest, sendtag=tag, source=source, recvtag=tag )

print( 'I, process ', rank, ', have received value ', val, ' from process ', source )
