import hashlib
import math
import argparse
import binascii

h_len = 8 # length of hash output in octets

def i2osp(x, x_len):
    """Convert a nonnegative integer to an octet string of a
    specified length. (Integer-to-Octet-String primitive)

    Keyword arguments:
    x -- nonnegative integer to be converted
    xLen -- intended length of the resulting octet string

    Returns:
    X -- corresponding octet string of length xLen
    """
    if x >= pow(256, x_len):
        return "integer too large"

    x_new = 0
    for i in range(256):
        x_new += ( ( x >> i ) | 0 ) * pow(256, i)

    X = 0
    for i in range(1,x_len+1):
        X += ( ( x_new >> ( x_len - i ) ) | 0 ) << ( x_len - i )

    return X


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
    T = 0

    for counter in range(math.ceil(mask_len / h_len - 1)):
        C = i2osp(counter, 4)
        # T = T + hash(mgf_seed + C)            
        h = hashlib.sha1(bytearray(mgf_seed) + bytearray(C)) # may have to convert to oct()
        dig = h.digest()
        # print(type(dig))
        T +=  int.from_bytes(dig, byteorder="big")

    output = 0
    for i in range(mask_len):
        output += 0

    return hex(T >> ( len(T) - mask_len ))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Assignment B3")

    parser.add_argument("--mgfseed", help="mgfSeed", type=str)
    parser.add_argument("--masklen", help="maskLen", type=int)

    args = parser.parse_args()

    print(hex(int(args.mgfseed, 16)))
    mgf_seed = binascii.unhexlify(args.mgfseed)
    print(mgf_seed)
    print(type(mgf_seed))
    print(len(mgf_seed))

    print(mgf1(mgf_seed, args.masklen))
