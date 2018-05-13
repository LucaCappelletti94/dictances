from distances import nth_variation
from utils import create_cases

def test_nth_variation():
    a, b = create_cases()
    assert (
        nth_variation(a,b,0),
        nth_variation(a,b,1),
        nth_variation(a,b,2),
        nth_variation(a,b,3),
        nth_variation(a,b,4)
    ) == (
        178,
        1.80865306195869,
        0.02414940510773,
        0.00036023819549,
        5.71352726e-06
    )