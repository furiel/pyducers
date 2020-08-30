import functools


def transduce(transducer, reduce_function, coll, initial_value=None):
    return functools.reduce(transducer(reduce_function), coll, initial_value)


def pyducers_filter(f, coll=None):
    if coll:
        return filter(f, coll)

    def transducer(rf):
        def filter_reduce(acc=None, current=None):
            if acc is None:
                return rf()
            if current is None:
                return rf(acc)

            if f(current):
                return rf(acc, current)
            else:
                return acc

        return filter_reduce

    return transducer


def pyducers_map(f, *args):
    def transducer(rf):
        def map_reduce(acc, current):
            return rf(acc, f(current))

        return map_reduce

    if len(args) == 0:
        return transducer

    if len(args) == 1:
        return map(f, args[0])

    return map(lambda x: f(*x), zip(*args))


def compose(*args):
    def compose_two(f, g):
        return lambda *x: f(g(*x))

    return functools.reduce(compose_two, args, lambda x: x)
