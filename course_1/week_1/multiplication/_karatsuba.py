def multiplication(x: int, y: int) -> int:
    """
    Multiplication of two integer via recursion

    https://en.wikipedia.org/wiki/Karatsuba_algorithm


    Parameters
    ----------
    x : int
        positive integer
    y : int
        positive integer

    Returns
    -------
    int
        result of the multiplication.
    """
    if (x < 10) or (y < 10):
        return x * y

    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    x1, x2 = divmod(x, 10 ** (m2))
    y1, y2 = divmod(y, 10 ** (m2))

    z0 = multiplication(x2, y2)
    z1 = multiplication((x1 + x2), (y1 + y2))
    z2 = multiplication(x1, y1)

    return (z2 * 10 ** (m2 * 2)) + ((z1 - z2 - z0) * 10 ** m2) + (z0)
