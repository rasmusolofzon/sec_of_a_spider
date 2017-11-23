import hashlib
import math

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

        return root.hex()

    def show_example(self):
        with open('merkle_path.txt', 'r') as f:
            result = self.lookup(f).hex()
            print("resulting merkle root: \t{0}".format(result))
            facit = "6f51120bc17e224de27d3d27b32f05d0a5ffb376"
            print("Should be \t\t{0}".format(facit))
            print("Correct? {0}".format(True if result == facit else False))

class Full_Node:
    def get_root_and_path(self, input_file):
        file_lines = input_file.readlines()

        leaf = int(file_lines[0])
        # print(leaf)
        j = int(file_lines[1])
        log = math.log2(len(file_lines)-2)
        # log = 3.75
        depth = int(log) if log % 2 == 0 else math.floor(log)+1
        # print(depth)
        tree = {}
        i = 0

        print()
        for line in file_lines[2:]:
            if line[-1:] == '\n':
                tree[(i, depth)] = bytearray.fromhex(line[:-1])
            else:
                tree[(i, depth)] = bytearray.fromhex(line)
                if i % 2 == 0:
                    tree[(i+1, depth)] = bytearray.fromhex(line)
            i += 1
        
        print("pre recursion:")
        for item in tree.items():
            print(item)

        print("\npost recursion:")
        tree = self.construct_tree_at_depth(tree, depth-1)
        for item in tree.items():
            print("({0}, {1}), {2}".format(item[0][0], item[0][1], item[1].hex()))

        root = tree[(0, 0)].hex()

        path = ""
        path_index = leaf*2
        path_node = ("", "")

        for d in range(depth, 0, -1):
            path_index = math.floor(path_index/2)
            if path_index % 2 == 0: 
                sibling = path_index+1 
            else:
                sibling = path_index-1 
            path += 'R' if path_index % 2 == 0 else 'L'
            path += str(tree[(sibling, d)].hex())
            path += '\n'

            if d == j:
                path_node = ('L' if path_index % 2 == 1 else 'R', tree[(sibling, d)].hex())
                print("\npath_node: {0}\n".format(path_node))
                for item in tree.items():
                    if item[1].hex() == path_node[1]:
                        print("({0}, {1})".format(item[0], item[1].hex()))

        path = path[:-1]
        # print(path)

        return root, path, path_node

    def construct_tree_at_depth(self, tree, depth):
        for i in range(int((max([index[0] for index in tree.keys() if index[1] == depth+1]) + 1)/2)):
            sub0 = tree[(i*2, depth+1)]
            sub1 = tree[(i*2+1, depth+1)]
            
            h = hashlib.sha1(bytearray(sub0))
            h.update(bytearray(sub1))
            tree[(i, depth)] = h.digest()
            if i % 2 == 0 and i > 0:
                tree[(i+1, depth)] = h.digest()
        if depth > 0:
            tree = self.construct_tree_at_depth(tree, depth-1)

        return tree

    def show_example(self):
        print()
        with open('full_node_example.txt', 'r') as f:
            i = -2
            print("{0} \t{1}\t\t{2}".format("i", "sibling", "hash"))
            for line in f:
                print("{0} \t{1}\t\t{2}".format(i, 'R' if i % 2 == 1 else 'L', line), end='')
                i += 1
        print()

if __name__ == "__main__":
    full_n = Full_Node()
    # full_n.show_example()
    # file_name = "test_full_node.txt"
    file_name = "valid_B3_full.txt"
    # file_name = "full_node_example.txt"
    with open(file_name, 'r') as f:
        root, path, path_node = full_n.get_root_and_path(f)
        print("\nroot: {0}".format(root))
        print("path_node: {0}{1}".format(path_node[0], path_node[1]))
        print("path: ", end="")
        for line in path.splitlines():
            print("\t{0}".format(line))

        print("\n{0}{1}{2}".format(path_node[0], path_node[1], root))
        # print(len("Rd6000578ba17ea5935dc4f2ba5fcea2416ff0ecef4f4cd35f5a3c801fb7e701c834bff87d2b3adaa"))
    
    spv_n = SPV_Node()
    # spv_n.show_example()
    print()
    with open("valid_B3_node.txt", 'r') as f2:
        result = spv_n.lookup(f2)
        print(result)
    #     print("57252a732982c12a13cc88c66d286acee68b676e")
