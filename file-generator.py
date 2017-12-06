import random
import sys
import copy
from string import letters

def generateFile(size, register_size, delimiter):
    pk1 = range(0,size)
    pk2 = range(size, 2*size)
    pk2c = copy.deepcopy(pk2)
    print("generating table1")
    table1 = []
    for key in pk1:
        line = str(key) + delimiter
        line_size = len(line)
        for i in range(register_size - line_size):
            line += random.choice(letters)
        table1.append(line)
    print("generating table2")
    table2 = []
    for key in pk1:
        fk = random.choice(pk2c)
        pk2c.pop(pk2c.index(fk))
        line = str(fk) + delimiter
        line += str(key) + delimiter
        line_size = len(line)
        for i in range(register_size - line_size):
            line += random.choice(letters)
        table2.append(line)
    print("saving unordered files")
    savingFile('table1_' + str(size) + "_ordered.csv", table1)
    savingFile('table2_' + str(size) + "_ordered.csv", table2)
    random.shuffle(table1)
    random.shuffle(table2)
    print("saving ordered files")
    savingFile('table1_' + str(size) + "_unordered.csv", table1)
    savingFile('table2_' + str(size) + "_unordered.csv", table2)
    print("end")



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
