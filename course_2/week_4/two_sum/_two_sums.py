def two_sum(array, min_limit=-10000, max_limit=10000):
    """
    Counts how many two evalues in the array can be summed to fit in a certain number range

    This implementation still takes quite long for the test cases.
    TODO: find a better implementation; is a sorted array more useful in this
    kind of special problem?

    Parameters
    ----------
    array : list
        array of integers
    min_limit : int
        lower target limit
    max_limit : int
        upper target limit

    Returns
    -------
    counter
        number of matching pairs in the target range
    """
    counter = 0

    array_hash = {int(n) for n in array}

    for target in range(min_limit, max_limit+1):
        for x in array_hash:
            if (target-x in array_hash) and (2 * x != target):
                counter += 1
                break

        # if any(target-x in array_hash and 2 * x != target for x in array_hash):
            counter += 1

    return counter
