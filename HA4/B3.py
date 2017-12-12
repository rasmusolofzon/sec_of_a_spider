import hashlib
import math
import argparse
import binascii

def i2osp(x, x_len):
    """Convert a nonnegative integer to an octet string of a
    specified length. (Integer-to-Octet-String primitive)

    Keyword arguments:
    x -- nonnegative integer to be converted
    xLen -- intended length of the resulting octet string

    Returns:
    X -- corresponding octet string of length xLen, a bytearray
    """
    if x >= pow(256, x_len):
        return "integer too large"

    # print("i2osp x: {0}".format(x))
    x_array = bytearray(x.to_bytes(x_len, byteorder="big", signed="False"))
    # print("i2osp x_array: {0}".format(x_array))

    # x_array.reverse()
    X = x_array.copy()
    # print("return from i2osp: {0} / {1}".format(X, binascii.hexlify(X)))
    return X


def mgf1(mgf_seed, mask_len):
    """
    Take an input string of arbitrary length and output a string of 
    (almost) arbitrary length.

    Keyword arguments:
    mgf_seed -- seed from which mask is generated, an octet string
    mask_len -- intended length in octets of the mask, at most 2^32 hLen
    """
    h_len = 20 # length of hash output in octets

    if mask_len > ( pow(2, 32) * h_len ):
        return "mask too long"
    T = bytearray(b'')

    for counter in range( math.ceil(mask_len / h_len) ):
        C = i2osp(counter, 4) 
        # print("C is: {0}".format(C))
        h = hashlib.sha1(mgf_seed + C)
        dig = bytearray(h.digest())
        T += dig
        # print("T is: {0}".format(T))

    return T[:mask_len]

if __name__ == '__main__':
    print("------------------------------------------------------------------------")
    # print("return from i2osp: {0}\n".format(i2osp(int("11111111111111111111111111111111", 2), 8)))

    parser = argparse.ArgumentParser(description="Assignment B3")

    parser.add_argument("--mgfseed", help="mgfSeed", type=str)
    parser.add_argument("--masklen", help="maskLen", type=int)

    args = parser.parse_args()

    print(args)

    mgf_seed = bytearray(binascii.unhexlify(args.mgfseed))
    print("mgf_seed: {0}".format(mgf_seed))

    output = mgf1(mgf_seed, args.masklen)
    print("\nfinal output: {0}".format(binascii.hexlify(output)))
    print("Should output: {0}".format(
        " 18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a"))
    print("Correct value? {0}".format("Yes!" 
        if b"18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a" 
        == binascii.hexlify(output) else "No.."))
