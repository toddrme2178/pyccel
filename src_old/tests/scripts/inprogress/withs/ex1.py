# coding: utf-8


from pyccel.stdlib.parallel.openmp import omp_get_thread_num

#$ header class StopIteration(public, hide)
#$ header method __init__(StopIteration)
#$ header method __del__(StopIteration)
class StopIteration(object):

    def __init__(self):
        pass

    def __del__(self):
        pass

#$ header class Range(public, iterable, openmp)
#$ header method __init__(Range, int, int, int, bool, int, str [:], str [:], str [:], str [:], str [:], int, str [:])
#$ header method __del__(Range)
#$ header method __iter__(Range)
#$ header method __next__(Range)
class Range(object):

    def __init__(self, start, stop, step, nowait=True, collapse=None,
                 private=['i', 'idx'], firstprivate=None, lastprivate=None,
                 reduction=['+', 'x'], schedule='static', ordered=True, linear=None):

        self.start = start
        self.stop  = stop
        self.step  = step

        self._ordered      = ordered
        self._private      = private
        self._firstprivate = firstprivate
        self._lastprivate  = lastprivate
        self._linear       = linear
        self._reduction    = reduction
        self._schedule     = schedule
        self._collapse     = collapse
        self._nowait       = nowait

        self.i = start

    def __del__(self):
        print('> free')

    def __iter__(self):
        self.i = 0

    def __next__(self):
        if (self.i < self.stop):
            i = self.i
            self.i = self.i + 1
        else:
            raise StopIteration()

#$ header class Parallel(public, with, openmp)
#$ header method __init__(Parallel, str, str, str [:], str [:], str [:], str [:], str, str [:], str)
#$ header method __del__(Parallel)
#$ header method __enter__(Parallel)
#$ header method __exit__(Parallel, str, str, str)
class Parallel(object):

    def __init__(self, num_threads=None, if_test=None,
                 private=['idx'], firstprivate=None, shared=None,
                 reduction=None, default='shared',
                 copyin=None, proc_bind=None):

        self._num_threads  = num_threads
        self._if_test      = if_test
        self._private      = private
        self._firstprivate = firstprivate
        self._shared       = shared
        self._reduction    = reduction
        self._default      = default
        self._copyin       = copyin
        self._proc_bind    = proc_bind

    def __del__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, type, value, tb):
        pass

x = 0.0

para    = Parallel()
indices = Range(-2,5,1)

with para:
    idx = omp_get_thread_num()

    for i in indices:
        x += 2 * i

print('x = ', x)
