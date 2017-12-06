import random
import sys
import time
import copy
from string import letters

def generateFile(size, register_size, delimiter):
    pk1 = range(0,size)
    pk2 = range(size, 2*size)
    pk1c = copy.deepcopy(pk1)
    table1 = []
    for key in pk1:
        line = ""
        line += str(key) + delimiter
        line_size = len(line)
        for i in range(register_size - line_size):
            line += random.choice(letters)
        print line
        table1.append(line)
    table2 = []
    for key in pk2:
        line = ""
        line += str(key) + delimiter
        fk = random.choice(pk1c)
        line += str(fk) + delimiter
        pk1c.pop(pk1c.index(fk))
        line_size = len(line)
        for i in range(register_size - line_size):
            line += random.choice(letters)
        print line
        table2.append(line)
    savingFile('table1_' + str(size) + "_ordered.csv", table1)
    savingFile('table2_' + str(size) + "_ordered.csv", table2)
    random.shuffle(table1)
    random.shuffle(table2)
    savingFile('table1_' + str(size) + "_unordered.csv", table1)
    savingFile('table2_' + str(size) + "_unordered.csv", table2)



def savingFile(filename, data):
    file = open( filename, "w")
    for line in data:
        file.write(line + "\n")
    file.close()


def main():
    field_delimiter = ";"
    size = int(sys.argv[1]);
    register_size = int(sys.argv[2])
    generateFile(size, register_size, field_delimiter)


if __name__ == "__main__":
    main()
