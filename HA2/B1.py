import argparse
import binascii
import multiprocessing as mp
# from mp import Process, Queue

def dinner(q, dinner_input):
    q.put(dinner_input)

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
        dinner_input = ( ((int.from_bytes(sa, byteorder="big") >> i) & mask), ((int.from_bytes(sb, byteorder="big") >> i) & mask), ((int.from_bytes(da, byteorder="big") >> i) & mask), ((int.from_bytes(db, byteorder="big") >> i) & mask), ((int.from_bytes(m, byteorder="big") >> i) & mask), args.b )

        p = mp.Process(target=dinner, args=(q, dinner_input,), name="p{0}".format(i))
        processes.append(p)
        p.start()
        print(dinner_input)

    while True:
        # print(mp.cpu_count())
        1
        if not all(proc.is_alive() for proc in processes):
            break

    print()

    while not q.empty():
        print(q.get())

    # print(args.sa, args.sb, args.da, args.db, args.m, args.b)
    # print(sa, sb, da, db, m)
    # print(binascii.hexlify(sa).decode('utf-8').upper())
    # print(binascii.unhexlify(args.sb))

    # print('0C73')
    # test = str(bin(int('0C73', 16)))
    # print(test[:4])
    # print(int('0C73', 16))

    '''
        ta in argument
        dela upp i ihophörande bitar
            skicka in dessa tupler i varsin process
                if b == 1:
                    broadcast = SA ^ SB ^ M
                elif b == 0:
                    output = SA ^ SB ^ 0
                    randomise if Alice, Bob or None sends msg
                        do this..
                msg = broadcast ^ DA ^ DB
                return msg, broadcast
            samla returns från alla 16 processer
            ge alla returns, samlade

    python B1.py --sa 0C73 --sb 80C1 --da A2A9 --db 92F5 --m 9B57 --b 0 
    '''
