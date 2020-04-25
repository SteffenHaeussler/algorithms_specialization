from typing import List, Sequence, Tuple


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def knapsack(items: Sequence[Tuple], max_weight: int) -> Tuple[int, Tuple]:
    """
    Solves the knapsack problem via recursion and memoization

    https://en.wikipedia.org/wiki/Knapsack_problem

    implementation via dynamic programming:
    https://github.com/SteffenHaeussler/discrete_optimization/tree/master/knapsack

    Parameters
    ----------
    items : List
        tuple of (value, weight)
    max_weight: int
        maximum weight for packed items

    Returns
    -------
    tuple
        maximum value, packed items
    """

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    @Memoize
    def bestvalue(i, j):
        if i == 0:
            return 0

        value, weight = items[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    j = max_weight
    result = []
    for i in range(len(items), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(items[i - 1])
            j -= items[i - 1][1]
    result.reverse()

    return bestvalue(len(items), max_weight), result
