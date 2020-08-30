from pyducers import filter, map, transduce, compose, sequence


def add(*args):
    return sum(args)


def square(n):
    return n*n


def two_times(n):
    return 2*n


def evenp(num):
    return num % 2 == 0


def assert_iter_eq(iter1, iter2):
    assert list(iter1) == list(iter2)


def test_filter():
    assert 6 == transduce(filter(evenp), add, [1, 2, 3, 4], 0)


def test_map():
    assert_iter_eq([2, 4, 6], map(two_times, [1, 2, 3]))
    assert_iter_eq([2, 3, 4], map(add, [1, 1, 1],
                                  [1, 0, 0], [0, 2, 0], [0, 0, 3]))

    assert 1*1 + 2*2 + 3*3 == transduce(map(square), add, [1, 2, 3], 0)


def test_compose():
    def inc(num):
        return num + 1

    assert 4 == compose(square, inc)(1)
    assert 2 == compose(inc, square)(1)

    assert 5 == compose(inc, square, two_times)(1)
    assert 8 == compose(two_times, square, inc)(1)

    assert 2*2 + 4*4 == transduce(compose(map(square), filter(evenp)),
                                  add, [1, 2, 3, 4], 0)


def test_tranduce_compose_order():
    assert 20 == transduce(compose(map(two_times), filter(evenp)), add,
                           [1, 2, 3, 4], 0)
    assert 12 == transduce(compose(filter(evenp), map(two_times)), add,
                           [1, 2, 3, 4], 0)


def test_sequence():
    assert [1, 2] == sequence([1, 2])
    assert_iter_eq([2, 4], sequence([1, 2, 3, 4], filter(evenp)))


def test_transduce_default_value():
    def identity(x):
        return x

    assert 6 == transduce(map(identity), add, [1, 2, 3])
    assert 0 == transduce(filter(evenp), add, [1])
    assert 6 == transduce(filter(evenp), add, [1, 2, 3, 4])
