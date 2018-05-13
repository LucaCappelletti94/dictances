from distances import MAE
from utils import create_cases

def test_MAE():
    a, b = create_cases()
    assert MAE(a,b) == 0.01016097225819