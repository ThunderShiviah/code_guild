
def get_(dct, k, default):
    """ If key in dict return associated value.
Else return default value."""
    try:
        return(dct[k])
    except KeyError:
        return default
