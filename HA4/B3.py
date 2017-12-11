'''
Two steps:
    1. implement MGF1 function
    2. implement "rest of OAEP scheme"...
'''

import hashlib
import math

h_len = 8 #length of hash output in octets

def i2osp(x, x_len):
    """Convert a nonnegative integer to an octet string of a
    specified length.

    Keyword arguments:
    x -- nonnegative integer to be converted
    xLen -- intended length of the resulting octet string

    Returns:
    X -- corresponding octet string of length xLen
    """
    if x >= pow(256, x_len):
        return "integer too large"
    return oct("hello")


def mgf1(mgf_seed, mask_len):
    """
    Take an input string of arbitrary length and output a string of 
    (almost) arbitrary length.

    Keyword arguments:
    mgf_seed -- seed from which mask is generated, an octet string
    mask_len -- intended length in octets of the mask, at most 2^32 hLen
    """
    mask = 0
    if mask_len > pow(2, 32):
        return "mask too long"
    T = oct(0)

    for counter in range(math.ceil(mask_len / h_len - 1)):
        C = i2osp(counter, 4)
        # T = T + hash(mgf_seed + C)            
        h = hashlib.sha1(bytearray(mgf_seed + C)) # may have to convert to oct()
        T = T + h.digest()

    return T >> ( len(T) - mask_len )