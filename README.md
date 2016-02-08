# python-fp-utils

_More natural Functional Programming in Python._

Python has some built-in functions like `map`, `reduce` and `filter` to enable some basic Functional Programming.

`python-fp_utils` provides the `Collection` wrapper class to make that more natural without trying to go beyond that (check things like e.g. [PyMonad](https://bitbucket.org/jason_delaat/pymonad/), [fn.py](https://github.com/kachayev/fn.py), etc to move forward in the FP path).

`Collection` receives a sequence. Operations will change that sequence and wrap the result in another `Collection` object to allow chaining.

#### Example:

The following code will take `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, it will select only the even numbers, multiply them by 10, and show them in reverse order:

```
>>> sorted(map(lambda x: x*10, filter(lambda x: x%2==0, range(0, 11))), reverse=True)
[100, 80, 60, 40, 20, 0]
```

Although that is concise and clear, it is not natural enough. What `Collection` provides is a wrapper that allows chaining of the different steps, which is easier to read and more:

```
>>> from fp_utils import Collection
>>> print Collection(range(0, 11)) \
...     .filter(lambda x: x%2==0) \
...     .map(lambda x: x*10) \
...     .comment("Sort descending") \
...     .apply(lambda list: sorted(list, reverse=True)) \
...     .getValue()
[100, 80, 60, 40, 20, 0]
```

#### Features:

`apply(func)`: applies `func` to the collection as a whole

`filter(func)`: filters the collection items using `func`

`reduce(func, initial)`: performs a reduce operation on collection items using `func`

`map(func)`: performs a map operation on the collection items using `func`

`flatMap(func)`: same as `map(func)` but it flattens the result one level

`parallelMap(func, [maxConcurrency])`: same as `map(func)` but performing it in parallel according to an optional `maxConcurrency` value (note: in Python 2 lambdas are not picklable so they cannot be used here)

`forEach(func)`: applies `func` (effect) to each collection item (the original collection is returned unmodified to preserve chaining)

`comment(text)`: only useful to document the code

`getValue()`: returns the wrapped collection value

