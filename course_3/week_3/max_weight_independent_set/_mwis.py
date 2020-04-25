from typing import List


def mwis(array: List) -> List:
    """
    Find the nodes, which forms a maximum-weight independent set of an undirected graph
    https://en.wikipedia.org/wiki/Independent_set_(graph_theory)

    TODO: 1 of 48 test cases is failing; this needs more debugging

    Parameters
    ----------
    array : list
        array of the weights of the nodes

    Returns
    -------
    list
        nodes, which are part of the maximum-weight independent set
    """
    S = []

    n = len(array)
    weights = [0, array[0]]

    for i in range(2, n + 1):
        weights.append(max(weights[i - 1], weights[i - 2] + array[i - 1]))

    i = n

    while i > 1:
        if weights[i - 1] >= weights[i - 2] + array[i - 1]:
            i -= 1
        else:
            S.append(i - 1)
            i -= 2

    return S
