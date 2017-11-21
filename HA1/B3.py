import hashlib

# hexstring = "2354cf006ef4eeefeddf29b9e68d5cb1918ed589"
# b_array = bytearray.fromhex(hexstring)
# print(b_array)

class Node:
    def lookup(self, input_file):
        path = {}
        i = 0

        for line in input_file:
            print(line, end="")
            if i == 0:
                path[i] = bytearray.fromhex(line[:-1])
            else:
                if line[-1:] == '\n':
                    path[i] = (line[:1], bytearray.fromhex(line[1:-1]))
                else:
                    path[i] = (line[:1], bytearray.fromhex(line[1:]))
            i += 1
        print()
        print()
        for item in path.items():
            print(item)
            print(bytearray(item[1][1]).hex())
        print()
        print()
        
        root = path[0]
        for i in range(1, len(path.keys())):
            print()
            print("root: \t\t\t{0}".format(bytearray(root)))
            print("path[{0}][1]:\t{1} \t{2}".format(i, path[i][0], bytearray(path[i][1])))
            if path[i][0] == 'L':
                h = hashlib.sha1(bytearray(path[i][1]))
                h.update(bytearray(root))
            else:
                h = hashlib.sha1(bytearray(root))
                h.update(bytearray(path[i][1]))
            root = h.digest()

        return root

if __name__ == "__main__":
    n = Node()
    with open('merkle_path.txt', 'r') as f:
        result = n.lookup(f).hex()
        print("\nresulting merkle root: \t{0}".format(result))
        facit = "6f51120bc17e224de27d3d27b32f05d0a5ffb376"
        print("Should be \t\t{0}".format(facit))
        print("Correct? {0}".format(True if result == facit else False))