"""Online bin packing: the packing rule.

Items arrive one at a time; each must be placed at once, in an open bin or in a new one, and never
moved. The harness calls choose_bin for every item of an instance, in order. Bins are never closed.

    choose_bin(item, bins, capacity) -> int
        item      size of the arriving item, 0 < item <= capacity
        bins      current fill of every open bin, in the order the bins were opened (a copy)
        capacity  the size of every bin
        returns   the index of an open bin the item fits in, or -1 to open a new bin

Baseline: first fit, the first open bin with room.
"""

EPS = 1e-9


def choose_bin(item: float, bins: list[float], capacity: float) -> int:
    for i, fill in enumerate(bins):
        if fill + item <= capacity + EPS:
            return i
    return -1
