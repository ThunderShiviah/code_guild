
from compress.compressor import *

def compress_test():
    assert compress('AAABBCDDD') == 'A3B2C1D3'
    assert compress('A') == 'A'
    assert compress('') == ''
    assert compress('AABBCC') == 'AABBCC' # compressing doesn't shorten string so just return string.
    assert compress(None) == None

def groupby_char_test():
    assert groupby_char(["A", "A", "A", "B", "B"]) == ["AAA", "BB"]

def compress_group_test():
    assert compress_group("AAA") == "A3"
    assert compress_group("A") == "A1"
