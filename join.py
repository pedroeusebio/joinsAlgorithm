import datetime as dt
from BTrees.OOBTree import OOBTree
import sys

def merge_join(right, left, field_delimiter):
    matches = 0
    right_line = right.readline().split(field_delimiter)
    left_line = left.readline().split(field_delimiter)
    while len(left_line) != 1 and len(right_line) != 1:
        if left_line[0] == right_line[1]:
            matches += 1
            right_line = right.readline().split(field_delimiter)
            left_line = left.readline().split(field_delimiter)
        elif int(left_line[0]) < int(right_line[1]):
            left_line = left.readline().split(field_delimiter)
        else :
            right_line = right.readline().split(field_delimiter)
    print(matches)
    return matches

def nested_loop(right, left, field_delimiter):
    matches = 0;
    left_line = left.readline().split(field_delimiter)
    while len(left_line) > 1:
        right_line = right.readline().split(field_delimiter)
        while len(right_line) > 1:
            if(left_line[0] == right_line[1]):
                matches += 1
                if(matches%100 == 0):
                    print(matches)
                break
            right_line = right.readline().split(field_delimiter)
        right.seek(0)
        left_line = left.readline().split(field_delimiter)
    print(matches);
    return matches;

def hash_join(right, left, field_delimiter):
    matches = 0;
    hash_table = {}
    #build phase
    position = right.tell()
    right_line = right.readline().split(field_delimiter)
    while len(right_line) > 1:
        hash_table[right_line[1]] = position
        position = right.tell()
        right_line = right.readline().split(field_delimiter)
    right.seek(0)
    #probe phase
    left_line = left.readline().split(field_delimiter)
    while len(left_line) > 1:
        right.seek(int(hash_table[left_line[0]]))
        right_line = right.readline().split(field_delimiter)
        if(left_line[0] == right_line[1]):
            matches += 1
        left_line = left.readline().split(field_delimiter)
    print matches

def btree_join(right, left, field_delimiter):
    btree = OOBTree()
    matches = 0;
    #build phase
    position = right.tell()
    right_line = right.readline().split(field_delimiter)
    while len(right_line) > 1:
        btree.update({right_line[1]: position})
        position = right.tell()
        right_line = right.readline().split(field_delimiter)
    right.seek(0)
    #probe phase
    left_line = left.readline().split(field_delimiter)
    while len(left_line) > 1:
        right.seek(int(btree[left_line[0]]))
        right_line = right.readline().split(field_delimiter)
        if(left_line[0] == right_line[1]):
            matches += 1
        left_line = left.readline().split(field_delimiter)
    print(matches)
    return matches



def selectFile(size):
    obj = {}
    if(size == 1000):
        obj = {
            'right': {
                'ordered': "table2_1000_ordered.csv",
                'unordered': "table2_1000_unordered.csv"
            },
            'left': {
                'ordered': "table1_1000_ordered.csv",
                'unordered': "table1_1000_unordered.csv"
            }
        }
    elif(size == 10000):
        obj = {
            'right': {
                'ordered': "table2_10000_ordered.csv",
                'unordered': "table2_10000_unordered.csv"
            },
            'left': {
                'ordered': "table1_10000_ordered.csv",
                'unordered': "table1_10000_unordered.csv"
            }
        }
    elif(size == 100000):
        obj = {
            'right': {
                'ordered': "table2_100000_ordered.csv",
                'unordered': "table2_100000_unordered.csv"
            },
            'left': {
                'ordered': "table1_100000_ordered.csv",
                'unordered': "table1_100000_unordered.csv"
            }
        }
    return obj

def main():
    print('we are on !!')

    algorithms = {
        'merge-join': {
            'func': merge_join,
            'right': "ordered",
            'left': "ordered"
        },
        # 'nested_loop': {
        #     'func': nested_loop,
        #     'right': "unordered",
        #     'left': "ordered"
        # },
        'hash_join' : {
            'func': hash_join,
            'right': "unordered",
            'left': "unordered"
        },
        'btree_join' : {
            'func': btree_join,
            'right': "unordered",
            'left': "unordered"
        }
    }

    file_size = int(sys.argv[1]);
    field_delimiter = ";"

    for key, value in algorithms.iteritems():
        obj = selectFile(file_size)
        file1 = open(obj['right'][value['right']], "r")
        file2 = open(obj['left'][value['left']], "r")
        func = value['func']
        start = dt.datetime.now()
        func(file1, file2, field_delimiter)
        end = dt.datetime.now()
        file1.close()
        file2.close()
        print(key)
        print((end-start).total_seconds())





if __name__ == "__main__":
    main()
