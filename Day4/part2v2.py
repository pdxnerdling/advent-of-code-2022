from operator import itemgetter
from sys import argv

START = 0 
END = 1

def get_assignments_sorted_by_start(line):
    line = line.strip().split(",")
    # Split element into list of ints
    line = [list(map(int, elf.split("-"))) for elf in line]
    # Sorts list of lists based on smallest first elemet
    # If first element is the same then sorts on largest second element
    line = sorted(line, key=lambda x: (x[0], -x[1]))
    return line[0], line[1]

def get_num_overlaps(filename):
    f = open(filename, 'r')
    total_overlap_count = 0
    for line in f:
        assignment1, assignment2 = get_assignments_sorted_by_start(line)
        if assignment1[END] >= assignment2[START]:
            total_overlap_count+=1
    print(total_overlap_count)

if __name__ == "__main__":
    filename = argv[1]
    get_num_overlaps(filename)