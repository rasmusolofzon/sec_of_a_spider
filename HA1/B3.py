import hashlib

class SPV_Node:
    def lookup(self, input_file):
        path = {}
        i = 0

        for line in input_file:
            if i == 0:
                path[i] = bytearray.fromhex(line[:-1])
            else:
                if line[-1:] == '\n':
                    path[i] = (line[:1], bytearray.fromhex(line[1:-1]))
                else:
                    path[i] = (line[:1], bytearray.fromhex(line[1:]))
            i += 1

        root = path[0]
        for i in range(1, len(path.keys())):
            # print("root: \t\t\t{0}".format(bytearray(root)))
            # print("path[{0}][1]:\t{1} \t{2}".format(i, path[i][0], bytearray(path[i][1])))
            if path[i][0] == 'L':
                h = hashlib.sha1(bytearray(path[i][1]))
                h.update(bytearray(root))
            else:
                h = hashlib.sha1(bytearray(root))
                h.update(bytearray(path[i][1]))
            root = h.digest()

        return root

    def show_example(self):
        with open('merkle_path.txt', 'r') as f:
            result = self.lookup(f).hex()
            print("resulting merkle root: \t{0}".format(result))
            facit = "6f51120bc17e224de27d3d27b32f05d0a5ffb376"
            print("Should be \t\t{0}".format(facit))
            print("Correct? {0}".format(True if result == facit else False))

class Full_Node:
    def __init__(self):
        pass    

if __name__ == "__main__":
    spv_n = SPV_Node()
    spv_n.show_example()