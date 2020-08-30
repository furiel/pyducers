from pyducers import filter, map, transduce


def assert_iter_eq(iter1, iter2):
    assert list(iter1) == list(iter2)


def test_filter():
    def oddp(num):
        return num % 2 == 0

    assert 6 == transduce(filter(oddp), lambda x, y: x+y, [1, 2, 3, 4], 0)


def test_map():
    assert_iter_eq([2, 4, 6], map(lambda x: 2*x, [1, 2, 3]))
    assert_iter_eq([2, 3, 4], map(lambda *x: sum(x),
                                  [1, 1, 1], [1, 0, 0], [0, 2, 0], [0, 0, 3]))
