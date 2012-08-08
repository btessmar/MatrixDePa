import os
from itertools import product, islice
from mpi4py import MPI

class Util(object) :

    @classmethod
    def replace_string(cls, line):

        if line.find("\n") > -1:
		    line = line.rstrip(os.linesep)
        return line

    @classmethod
    def det(cls,M,prod=1):
        dim = len(M)
        if dim == 1:
            return prod * M.pop().pop()
        it = product(xrange(1,dim),repeat=2)
        prod *= float(M[0][0])
        new_matrix = []
        for i in xrange(dim-1):
            matrix_row = []
            for x,y in islice(it,dim-1):
                matrix_row.append(
                    float(M[x][y])-float(M[x][0])*(float(M[0][y])/float(M[0][0]))
                )
            new_matrix.append(matrix_row)
        return Util.det(new_matrix,prod)

    @classmethod
    def controller():
        
        matrix_input = []
        fobj = open("source.csv", "r")
        for line in fobj:
            s = Util.replace_string(line)
            matrix_input.append(s.split(";"))
        fobj.close()

        # Stores a list of stats
        stats_list = []

        process_list = range(1, MPI.COMM_WORLD.Get_size())

        while len(process_list) > 0:
            status = MPI.Status()
            data = MPI.COMM_WORLD.Recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
            if status.tag > 9:
                if status.tag == 15:
                    # Record the data
                    stats_list.append(data[0])
            else:
                if status.tag == 5:
                    # Value für die Verarbeitung übergeben.
                    MPI.COMM_WORLD.Send(matrix_input, dest=status.source)
            process_list = range(1, MPI.COMM_WORLD.Get_size())
        print(stats_list)

    @classmethod
    def worker():

        rank = MPI.COMM_WORLD.Get_rank()
        proc_name = MPI.Get_processor_name()

        # Send ready
        MPI.COMM_WORLD.Send([{'rank':rank, 'name':proc_name}], dest=0, tag=5)
        # Get some data
        matrix_source = MPI.COMM_WORLD.Recv(source=0)
        # Calc determinate
        determinate = Util.det(matrix_source)
        # Send ready
        MPI.COMM_WORLD.Send(determinate, dest=0, tag=15)