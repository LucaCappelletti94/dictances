from dictances import nth_variation

from utils import close, create_cases


def test_nth_variation():
    a, b = create_cases()
    assert (
        close(nth_variation(a, b, 0), 178) and close(nth_variation(a, b, 1), 1.80865306195869) and close(nth_variation(
            a, b, 2), 0.02414940510773) and close(nth_variation(a, b, 3), 0.00036023819549) and close(nth_variation(a, b, 4), 5.71352726e-06))
