# pyducers
Transducer library for python, inspired by clojure

## map
### syntax

This behaves the same way as in the standard library.
```python
map(f, coll)
```

`map` optionally receives multiple collections. In that case it applies `f` function for the zip of the collections.
```python
map(f, coll1, coll2, ...)
```

Supplying only an `f` function returns a transducer
```python
map(f)
```

### examples

```python
>>> def add(*args):
...     return sum(args)
...
>>> def square(n):
...     return n*n
...
>>> def inc(n):
...     return n+1
...
>>> from pyducers import map, transduce
>>> list(map(inc, [1, 2, 3]))
[2, 3, 4]
>>> list(map(add, [1, 2], [1, 2]))
[2, 4]
>>> transduce(map(square), add, [1, 2, 3])
14
>>> 1*1 + 2*2 + 3*3
14
```

## filter
### syntax
This behaves the same way as in the standard library:
```python
filter(f, coll)
```

Passing only `f` to filter returns the transducer
```python
filter(f)
```
### examples
```python
>>> def add(*args):
...     return sum(args)
...
>>> def evenp(num):
...     return num % 2 == 0
...
>>> from pyducers import filter, transduce
>>>
>>> list(filter(evenp, [1, 2, 3, 4]))
[2, 4]
>>> transduce(filter(evenp), add, [1, 2, 3, 4], 0)
6
```

## compose

`compose` function creates a function composition from the provided function. The functions are applied from right to left to the input
Note: when using `transducer` on the composition, the composed transducers are applied in the opposite order: from left to right.

### syntax
```python
compose(f, g, ...)
```

### examples
```python
>>> def add(*args):
...     return sum(args)
...
>>> def square(n):
...     return n*n
...
>>> def inc(n):
...     return n+1
...
>>> def two_times(n):
...     return 2*n
...
>>> def evenp(num):
...     return num % 2 == 0
...
>>> from pyducers import compose, transduce, map, filter
>>> compose(square, inc)(1)
4
>>> compose(inc, square)(1)
2
>>> compose(inc, square, two_times)(1)
5
>>> compose(two_times, square, inc)(1)
8
>>> transduce(compose(map(square), filter(evenp)), add, [1, 2, 3, 4], 0)
20
```

## transduce
`tranduce` reduces over a collection with the tranduced reduce function. Initial value can be optionally supplied.
### syntax
If `initial_value` is not provided, it will be generated by calling `reduce_function without arguments`: `reduce_function()`
```
transduce(transducer, reduce_function, coll, initial_value=None)
```
### examples
```python
>>> def add(*args):
...     return sum(args)
...
>>> def evenp(num):
...     return num % 2 == 0
...
>>> from pyducers import compose, transduce, map, filter
>>> transduce(filter(evenp), add, [1, 2, 3, 4], 0)
6
```

## sequence
`sequence` collects the result of the transducer into a collection.

### syntax

Without transducer, `sequence` simply transforms collection into a list.
```python
sequence(coll, f=None)
```

### examples
```python
>>> def evenp(num):
...     return num % 2 == 0
...
>>> from pyducers import filter, sequence
>>> sequence([1, 2])
[1, 2]
>>> sequence([1, 2, 3, 4], filter(evenp))
[2, 4]
```
