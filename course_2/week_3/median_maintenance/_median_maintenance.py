import heapq
from typing import List


def median_maintenance(array: List) -> List:
    """
    Calculates the upper half of a stream of incoming numbers in logarithmic time


    Parameters
    ----------
    array : list
        array of integers

    Returns
    -------
    median_queue
        upper half values of the input array
    """
    h_low = []
    h_high = []

    median_queue = []

    heapq.heappush(h_high, array[0])
    median_queue.append(array[0])

    for i in array[1:]:

        if i < h_high[0]:

            heapq.heappush(h_low, i)

        else:

            heapq.heappush(h_high, i)

        diff = len(h_high) - len(h_low)

        if (diff == 0) or (diff == -1):

            median_queue.append(heapq.nlargest(1, h_low)[0])

        elif diff >= 1:

            balance = heapq.heappop(h_high)
            heapq.heappush(h_low, balance)
            median_queue.append(balance)

        elif diff <= -2:

            heapq._heapify_max(h_low)
            balance = heapq._heappop_max(h_low)
            heapq.heappush(h_high, balance)
            median_queue.append(heapq.nlargest(1, h_low)[0])

    return median_queue
