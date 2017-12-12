import hashlib
import math
import argparse
import binascii

h_len = 20 # length of hash output in octets


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
    # x_array = bytearray(x.to_bytes(x_len, byteorder="big", signed="False"))
    # print("i2osp x_array: {0}".format(x_array))

    # x_array.reverse()
    # X = x_array.copy()
    # print("return from i2osp: {0} / {1}".format(X, binascii.hexlify(X)))
    # return X
    return bytearray(x.to_bytes(x_len, byteorder="big", signed="False"))


def mgf1(mgf_seed, mask_len):
    """
    Take an input string of arbitrary length and output a string of 
    (almost) arbitrary length.

    Keyword arguments:
    mgf_seed -- seed from which mask is generated, an octet string
    mask_len -- intended length in octets of the mask, at most 2^32 hLen
    """

    if mask_len > ( pow(2, 32) * h_len ):
        return "mask too long"
    T = bytearray()

    for counter in range( math.ceil(mask_len / h_len) ):
        C = i2osp(counter, 4) 
        # print("C is: {0}".format(C))
        h = hashlib.sha1(mgf_seed + C)
        dig = bytearray(h.digest())
        T += dig
        # print("T is: {0}".format(T))

    return T[:mask_len]

def oaep_encode(message, seed):
    """
    Take an input message and ...

    Keyword arguments:
    message -- message to encode, an octet string of length m_len
    seed -- octet string seed of length hLen

    Returns:
    encoded_message -- the encoded message
    """
    k = 128
    L = ""
    h = hashlib.sha1(L.encode("utf-8"))
    l_hash = bytearray(h.digest())
    m_len = math.ceil(len(binascii.hexlify(message)) / 2)

    if m_len > (k - 2*h_len - 2):
        return "message too long"

    print(k - m_len - 2*h_len - 2)

    ps = 0
    ps = bytearray(ps.to_bytes(k - m_len - 2*h_len - 2, byteorder="big"))

    one = 1
    octet_of_one = bytearray(one.to_bytes(1, byteorder="big"))

    db = l_hash + ps + octet_of_one + message
    print("\nk - h_len - 1 = {0}".format(k-h_len-1))
    print("len(db) = {0}\n".format(math.ceil(len(binascii.hexlify(db))/2)))
    print("db = \t{0}".format(binascii.hexlify(db)))

    db_mask = mgf1(seed, k - h_len - 1)
    print("db_mask = \t{0}".format(binascii.hexlify(db_mask)))
    masked_db = bytearray(k - h_len - 1)
    for i in range(k - h_len - 1):
        # print("masked = {0}, db = {1}, db_mask = {2}".format(masked_db[i], db[i], db_mask[i]))
        masked_db[i] = db[i] ^ db_mask[i]
    print("masked_db: \t{0}\n".format(binascii.hexlify(masked_db)))

    seed_mask = mgf1(masked_db, h_len)

    print("\nseed_mask = \t{0}".format(binascii.hexlify(seed_mask)))
    print("seed = \t\t{0}".format(binascii.hexlify(seed)))
    masked_seed = bytearray(len(seed))
    for i in range(len(seed)-1):
        masked_seed[i] = seed[i] ^ seed_mask[i]
    print("masked_seed = \t{0}\n".format(binascii.hexlify(masked_seed)))

    encoded_message = bytearray(b'\00') + masked_seed + masked_db

    print("len(EM) = {0}\n".format(math.ceil(len(binascii.hexlify(encoded_message)) / 2)))
    return binascii.hexlify(encoded_message)

def oaep_decode(encoded_message):
    """
    Take an input message and ...

    Keyword arguments:
    encoded_message -- message to decode
 
    Returns:
    message -- the decoded message
    """
    L = bytearray(binascii.unhexlify("da39a3ee5e6b4b0d3255bfef95601890afd80709"))
    print(L)

    return ...

if __name__ == '__main__':
    print("------------------------------------------------------------------------")

    ex = {  'M': bytearray(binascii.unhexlify("fd5507e917ecbe833878")),
            'seed': bytearray(binascii.unhexlify("1e652ec152d0bfcd65190ffc604c0933d0423381")),
            'EM': bytearray(binascii.unhexlify("0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82")) }

    parser = argparse.ArgumentParser(description="Assignment B3")

    parser.add_argument("--mgfseed", help="mgfSeed", type=str)
    parser.add_argument("--masklen", help="maskLen", type=int)
    parser.add_argument("--m", help="Message to encode", type=int)
    parser.add_argument("--seed", help="Seed for encoding step", type=int)
    parser.add_argument("--em", help="Encoded message to decode", type=int)

    args = parser.parse_args()

    print(args)

    # mgf_seed = bytearray(binascii.unhexlify(args.mgfseed))
    # print("mgf_seed: {0}".format(mgf_seed))

    # output = mgf1(mgf_seed, args.masklen)
    # print("\nfinal output: {0}".format(binascii.hexlify(output)))
    # print("Should output: {0}".format(
        # " 18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a"))
    # print("Correct value? {0}".format("Yes!" 
        # if b"18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a" 
        # == binascii.hexlify(output) else "No.."))

    # output = oaep_encode(ex['M'], ex['seed'])
    # print("\nfinal output: \n{0}\n".format(output))
    # print(binascii.hexlify(ex['EM']))
    # print("Correct value? {0}".format("Yes!" 
    #     if output 
    #     == binascii.hexlify(ex['EM']) else "No.."))

    print(oaep_decode(ex['EM']))

'''
Test quiz values:
    mgf1:
        mgfSeed = 9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214
        maskLen = 21
    
    encoding:
        M = c107782954829b34dc531c14b40e9ea482578f988b719497aa0687
        seed = 1e652ec152d0bfcd65190ffc604c0933d0423381
    
    decoding:
        EM = 0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc 6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bf c51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f
'''
