from collections import deque
from itertools import count

# Construction of deque is located outside the function
# to avoid reconstructing the deque each time the function
# is called. Mainly to reduce overhead consumption since
# the 0-length deque is only used to iterate through the
# iterator.
consumeall = deque(maxlen=0).extend


def ilen(item):
    """
    Input length counter.
    Takes in an input iterator object and zips it with a count iterator,
    then iterates through the entire length of the input using the
    0-length deque.extend method. Count iterator set as second zip
    argument to avoid over-counting. Final use of next() is to
    account for Python's 0-based indexing.

    Example:
    with open(input_path) as f:
        print(ilen(f))
    """
    cnt = count()
    consumeall(zip(item, cnt))
    return next(cnt)
