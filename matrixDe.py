from util import Util
from mpi4py import MPI

if MPI.COMM_WORLD.Get_rank() == 0:
	Util.controller()
else :
	Util.worker()



