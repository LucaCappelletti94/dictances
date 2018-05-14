from dictances.__version__ import __version__
import re

def test_version():
    pattern = re.compile("\d+\.\d+\.\d+")
    assert pattern.match(__version__)