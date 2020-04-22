from typing import List, Union


def sort_and_count(A: List) -> Union[List, int]:
    """
    Sorts an array and counts the number of inversions

    Parameters
    ----------
    A : list
        array of distinct integers

    Returns
    -------
    list
        sorted array of the same integers
    int
        number of split inversions of A
    """

    if len(A) == 1:
        return A, 0
    else:
        n = len(A) // 2
        B, x = sort_and_count(A[:n])
        C, y = sort_and_count(A[n:])

        D, z = merge_and_countsplit(B, C)
    return D, (x + y + z)


def merge_and_countsplit(B: List, C: List) -> Union[List, int]:
    """
    Sorts an array and counts the number of inversions

    Parameters
    ----------
    B : list
        sorted array
    C : list
        sorted array

    Returns
    -------
    list
        sorted array
    int
        number of split inversions
    """
    i, j = 0, 0
    cnt = 0

    D = []

    n_b = len(B)
    n_c = len(C)

    for _ in range(n_b + n_c):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        elif C[j] < B[i]:
            D.append(C[j])
            j += 1
            cnt += n_b - i

        if i == n_b:
            D = D + C[j:]
            break

        elif j == n_c:
            D = D + B[i:]
            break

    return D, cnt
