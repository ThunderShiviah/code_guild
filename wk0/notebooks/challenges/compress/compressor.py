    
def groupby_char(lst):
    """Returns a list of strings containing identical characters.
    
    Takes a list of characters produced by running split on a string. Groups runs (in order sequences) of identical characters into string elements in the list.
    
    Parameters
    ---------
    Input:
    lst: list
    A list of single character strings.
    
    Output:
    grouped: list
    A list of strings containing grouped characters."""

    new_lst = []

    count = 1

    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            count += 1        
        else:
            new_lst.append([lst[i],count])
            count = 1
            
    new_lst.append((lst[-1],count))


    grouped = [char*count for [char, count] in new_lst]

    return grouped

def compress_group(string):
    """Returns a compressed two character string containing a character and a number.
    
    Takes in a string of identical characters and returns the compressed string consisting of the character and the length of the original string.
    
    Example
    -------
    "AAA"-->"A3"

    Parameters:
    -----------
    Input:
    string: str
    A string of identical characters.
    
    Output:
    ------
    compressed_str: str
    A compressed string of length two containing a character and a number.
    """
    

    return str(string[0]) + str(len(string))


def compress(string):
    """Returns a compressed representation of a string.
    
    Compresses the string by mapping each run of identical characters to a 
    single character and a count. 
    
    Ex.
    --
    compress('AAABBCDDD')--> 'A3B2C1D3'.
    
    Only compresses string if the compression is shorter than the original string.

    Ex.
    --
    compress('A')--> 'A' # not 'A1'.

    Parameters
    ----------

    Input:
    string: str
    The string to compress

    Output:
    compressed: str
    The compressed representation of the string.
    """

    try:
        split_str = [char for char in string] # Create list of single characters.
        grouped = groupby_char(split_str) # Group characters if characters are identical.
        compressed = ''.join( # Compress each element of the grouped list and join to a string.
                [compress_group(elem) for elem in grouped])

        if len(compressed) < len(string): # Only return compressed if compressed is actually shorter.
            return compressed
        else:
            return string

    except IndexError: # If our input string is empty, return an empty string.
        return ""

    except TypeError: # If we get something that's not compressible (including NoneType) return None.
        return None

