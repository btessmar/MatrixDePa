import os
from itertools import product, islice

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
        return Util.det([[float(M[x][y])-float(M[x][0])*(float(M[0][y])/float(M[0][0])) for x,y in islice(it,dim-1)] for i in xrange(dim-1)],prod)