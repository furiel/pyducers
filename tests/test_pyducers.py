from pyducers import filter, transduce


def test_filter():
    def oddp(num):
        return num % 2 == 0

    assert 6 == transduce(filter(oddp), lambda x, y: x+y, [1, 2, 3, 4], 0)
