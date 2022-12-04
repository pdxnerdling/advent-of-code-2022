from sys import argv

def get_elf_assigment_ends_in_lowest_start_order(line):
    line = line.strip().split(",")
    # Split element into list of ints
    line = [list(map(int, elf.split("-"))) for elf in line]
    # Sorts list of lists based on smallest first elemet
    # If first element is the same then sorts on largest second element
    line = sorted(line, key=lambda x: (x[0], -x[1]))
    return line[0][1], line[1][1] # return end of each assignment

def get_num_overlaps(filename):
    f = open(filename, 'r')
    total_overlap_count = 0
    for line in f:
        assignment1_end, assignment2_end = get_elf_assigment_ends_in_lowest_start_order(line)
        if assignment1_end >= assignment2_end:
            total_overlap_count+=1
    print(total_overlap_count)

if __name__ == "__main__":
    filename = argv[1]
    get_num_overlaps(filename)