import heapq
from typing import List


def huffman(array: List, n_symbols: int) -> List:
    """
    Huffman codes provides lossless compression of input data, based on the
    frequencies of their occurence

    https://en.wikipedia.org/wiki/Huffman_coding

    Parameters
    ----------
    array : list
        array of the weight of symbols
    n_symbols: int
        number of symbols
    Returns
    -------
    list
        sorted array of huffman encoded input
    """
    h = []
    for symbol in array:
        heapq.heappush(h, [symbol, [""]])

    for _ in range(n_symbols - 1):
        left = heapq.heappop(h)
        right = heapq.heappop(h)
        left[1] = [i + "0" for i in left[1]]
        right[1] = [i + "1" for i in right[1]]
        new = [left[0] + right[0], left[1] + right[1]]
        heapq.heappush(h, new)

    encoding = heapq.heappop(h)
    return sorted(encoding[1], key=len)
