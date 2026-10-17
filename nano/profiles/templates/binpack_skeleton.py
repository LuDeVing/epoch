"""An online bin-packing rule. Items of size in (0, 1] arrive one at a time; each is placed at once
into an open bin or into a new one, and never moves. The harness calls choose_bin for every item.
Standard library only."""


def choose_bin(item: float, bins: list[float], capacity: float) -> int:
    """Return the index of an open bin the item fits in (bins[i] + item <= capacity), or -1 to open a new bin.

    item      the size of the arriving item, in (0, capacity]
    bins      the current fill of each open bin, in the order they were opened (a copy; do not rely on changing it)
    capacity  the size of every bin (1.0 on the benchmark)
    """
    raise NotImplementedError
