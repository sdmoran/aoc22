# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

class File:
    # File has...
    # name: name of this file
    # size: size of this file
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # define getSize method identical to Directory to make things easier
    def getSize(self):
        return self.size

allNodes = []

class Directory:
    # Directory has...
    # name: name of this directory
    # parent: Directory object this is a parent of
    # contents: List of other Directory or File objects
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.contents = []
    
    def addElt(self, elt): # add file or dir 
        elt.parent = self
        self.contents.append(elt)
        if isinstance(elt, Directory):
            allNodes.append(elt)

    # Recursively get size of all contents
    def getSize(self):
        # empty dir
        if len(self.contents) < 1:
            return 0
        
        size = 0

        # Otherwise get sum of files and sum of size of subdirs
        for c in self.contents:
            size += c.getSize()

        return size


def getSize(contents):
    if contents == None:
        return 0
    
def part1(lines):
    root = Directory("/")

    lines = lines[1:] # strip first line, already created root dir

    i = 0

    # build dir structure
    activeDir = root
    while i < len(lines):
        # commands start with $
        if lines[i][0] == "$":
            cmd = lines[i][2:4]
            # we only care about changing dirs; ls we don't have to do anything
            if cmd == "cd":
                dirName = lines[i].split(" ")[2]
                print(f"Changing dir to: {dirName} ")
                if dirName == "/":
                    activeDir = root
                if dirName == "..":
                    activeDir = activeDir.parent
                else:
                    for c in activeDir.contents:
                        if c.name == dirName:
                            activeDir = c
                            break
                print("Changed to ", activeDir.name)
        # if not a command
        else: 
            # create dir
            if lines[i][:3] == "dir":
                # create dir with given name
                dirName = lines[i][4:]
                activeDir.addElt(Directory(dirName))
                print(f"Created dir {dirName}")
            # create file
            else:
                (size, fname) = lines[i].split(" ")
                print(f"Created file {fname}")
                activeDir.addElt(File(fname, int(size)))
        i += 1
    
    sizes = 0
    # once built, check file sizes
    for node in allNodes:
        s = node.getSize()
        print(f"Size of {node.name}: {s}")
        if s <= 100000:
            sizes += s

    print("TOTAL SIZES: ", sizes)
    return root

def part2(root):
    totalSpace = 70000000
    spaceUsed = root.getSize()
    spaceNeeded = 30000000
    spaceAvailable = totalSpace - spaceUsed
    print("Total size of root dir: ", spaceUsed)
    print("Total space available: ", spaceAvailable)

    bestSize = allNodes[0].getSize()

    for n in allNodes:
        dirSize = n.getSize()
        if spaceAvailable + dirSize > spaceNeeded:
            bestSize = min(bestSize, dirSize)
    
    print("Best size: ", bestSize)
    print("Free space after deleting best size: ", spaceAvailable + bestSize)


def main():
    lines = read_input("input.txt")
    root = part1(lines)
    part2(root)

if __name__ == "__main__":
    main()