import argparse
import binascii
import multiprocessing as mp

def dinner(q, dinner_input):
    if dinner_input[6] == 1:
        own_broadcast = dinner_input[1] ^ dinner_input[2] ^ dinner_input[5]
        msg = own_broadcast ^ dinner_input[3] ^ dinner_input[4]
    else:
        own_broadcast = dinner_input[1] ^ dinner_input[2] ^ 0
        msg = ( own_broadcast ^ dinner_input[3] ^ dinner_input[4] ) << dinner_input[0]

    q.put((dinner_input[0], own_broadcast, msg))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A 16 bit Dining Cryptographers net.", epilog="Please specify all parameters (except -h, of course).")

    parser.add_argument("--sa", help="Your shared 16-bit secret with Alice")
    parser.add_argument("--sb", help="Your shared 16-bit secret with Bob", type=str)
    parser.add_argument("--da", help="The data broadcasted by Alice", type=str)
    parser.add_argument("--db", help="The data broadcasted by Bob", type=str)
    parser.add_argument("--m", help="The message you may want to send", type=str)
    parser.add_argument("--b", help="1 for sending message m, 0 for not sending it", type=int)

    args = parser.parse_args()

    sa = binascii.unhexlify(args.sa)
    sb = binascii.unhexlify(args.sb)
    da = binascii.unhexlify(args.da)
    db = binascii.unhexlify(args.db)
    m = binascii.unhexlify(args.m)

    mask = 0b1
    q = mp.Queue()
    processes = []

    for i in range(16):
        # (0,     1,  2,  3,  4,  5, 6)
        # (index, SA, SB, DA, DB, M, b)
        dinner_input = ( i, ((int.from_bytes(sa, byteorder="big") >> i) & mask), ((int.from_bytes(sb, byteorder="big") >> i) & mask), ((int.from_bytes(da, byteorder="big") >> i) & mask), ((int.from_bytes(db, byteorder="big") >> i) & mask), ((int.from_bytes(m, byteorder="big") >> i) & mask), args.b )

        p = mp.Process(target=dinner, args=(q, dinner_input,), name="p{0}".format(i))
        processes.append(p)
        p.start()
        print(dinner_input)

    print()

    dinner_output = []
    while len(dinner_output) < 16:
        dinner_output.append(q.get())
    
    result = 0
    for output in dinner_output:
        print(output)
        if args.b == 0:
            result = result | (output[1] << ( 16 + output[0]) )
            result =  result | output[2]
        elif args.b == 1:
            result = result | (output[1] << output[0] )
    
    print("\n\nProgram output is: {0}".format(hex(result)).upper())

    # print(args.sa, args.sb, args.da, args.db, args.m, args.b)
    # print(sa, sb, da, db, m)
    # print(binascii.hexlify(sa).decode('utf-8').upper())
    # print(binascii.unhexlify(args.sb))

    '''
    assignment test string #1
        python B1.py --sa 0C73 --sb 80C1 --da A2A9 --db 92F5 --m 9B57 --b 0 
            result 0x8CB2BCEE

    assignment test string #2
        python B1.py --sa 27C2 --sb 0879 --da 35F6 --db 1A4D --m 27BC --b 1 
            result 0807
    
    testquiz #1
        python B1.py --sa bf0d --sb 3c99 --da 186f --db 2ead --m 62ab --b 0
            result 0x8394B556
     testquiz #2
        python B1.py --sa d75c --sb ee87 --da c568 --db fcb3 --m 4674 --b 1
            result 0x7FAF
    '''
