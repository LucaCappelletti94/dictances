from distances_utils import sort
def jensen_shannon(a:dict, b:dict):
    """
        Determines the Jensen–Shannon divergence.

        Args:
            other: the zipf to which determine the JS divergence.

        Returns:
            A float number representing the JS divergence
    """
    total = 0
    delta = 0
    big, small = sort(a,b)

    big_get = big.get
    log = math.log

    for key, value in small_data.items():
        ov = big_get(key)
        if ov:
            denominator = (ov + value)/2
            total += value*log(value/denominator) + ov*log(ov/denominator)
            delta -= ov
        else:
            delta += value

    total += (1+delta)*log(2)
    return total/2