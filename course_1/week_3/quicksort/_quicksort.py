import numpy as np


def quicksort(arr, start=None, end=None, FLAG_PIVOT=None):
    """
    Quicksort wrapper

    Parameters
    ----------
    arr : list
        array of distinct integers
    start : int
        left index of endpoint
    end : int
        right index of endpoint
    FLAG_PIVOT : str
        Flag for selected pivot element ['First', 'Last', 'Median']

    Returns
    -------
    arr
        sorted array of distinct integers
    int
        number of swaps
    """
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    if FLAG_PIVOT is None:
        FLAG_PIVOT = "First"

    cnt = _quicksort(arr, start, end, FLAG_PIVOT)

    return arr, cnt


def _quicksort(arr, start, end, FLAG_PIVOT):
    """
    Quicksort wrapper

    Parameters
    ----------
    arr : list
        array of distinct integers
    start : int
        left index of endpoint
    end : int
        right index of endpoint
    FLAG_PIVOT : str
        Flag for selected pivot element ['First', 'Last', 'Median']

    Returns
    -------
    int
        number of swaps
    """
    cnt = 0
    if start < end:

        pos = _choosepivot(arr, start, end, FLAG_PIVOT)
        arr[pos], arr[start] = arr[start], arr[pos]

        new_pos, cnt = _partition(arr, start, end)

        cnt += _quicksort(arr, start, new_pos - 1, FLAG_PIVOT)
        cnt += _quicksort(arr, new_pos + 1, end, FLAG_PIVOT)

    return cnt


def _choosepivot(arr, start, end, FLAG_PIVOT):
    """
    Choose pivot element for quicksort

    Parameters
    ----------
    arr : list
        array of distinct integers
    start : int
        left endpoints
    end : int
        right endpoint
    FLAG_PIVOT : str
        Flag for selected pivot element ['First', 'Last', 'Median']

    Returns
    -------
    int
        index of pivot element
    """
    if FLAG_PIVOT == "Last":
        return end

    elif FLAG_PIVOT == "Median":
        n = len(arr[start : end + 1]) - 1
        median = start + n // 2
        index = np.argsort([arr[start], arr[median], arr[end]])[1]

        if index == 0:
            return start
        elif index == 1:
            return median
        elif index == 2:
            return end

    else:
        return start


def _partition(arr, start, end):
    """
    Choose pivot element for quicksort

    Parameters
    ----------
    arr : list
        array of distinct integers
    start : int
        left index of endpoint
    end : int
        right index of endpoint

    Returns
    -------
    int
        index of pivot element
    int
        count of swaps
    """
    pivot = arr[start]
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1, end - start
