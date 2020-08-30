import pyducers
import functools
import time


ITERATIONS = 1000000


def oddp(num):
    return num % 2 == 0


def measure_time(description):
    def wrap_with_time(f):
        def inner():
            t = time.process_time()
            retval = f()
            elapsed_time = time.process_time() - t
            print("time: {:.3f}\tresult {}\talgorithm: {}".format(elapsed_time,
                                                                  retval,
                                                                  description))
            return retval
        return inner
    return wrap_with_time


@measure_time("transduce with filter")
def transduce_with_filter():
    return pyducers.transduce(pyducers.filter(oddp),
                              lambda x, y: x+y, range(ITERATIONS), 0)


@measure_time("with for loop")
def with_for_loop():
    total = 0
    for i in range(ITERATIONS):
        if oddp(i):
            total += i
    return total


@measure_time("builtin reduce with prefiltered list")
def builtin_reduce_with_prefiltered_list():
    return functools.reduce(lambda x, y: x+y,
                            filter(oddp, range(ITERATIONS)), 0)


transduce_with_filter()
with_for_loop()
builtin_reduce_with_prefiltered_list()
