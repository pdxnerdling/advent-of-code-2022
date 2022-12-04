from sys import argv

def read_in_file(filename):
    f = open(filename, 'r')
    total_overlap_count = 0
    for line in f:
        line = line.strip().split(",")
        elf1 = line[0].split("-")
        elf1_a = int(elf1[0])
        elf1_b = int(elf1[1])
        elf2 = line[1].split("-")
        elf2_a = int(elf2[0])
        elf2_b = int(elf2[1])
        if elf1_b - elf1_a > elf2_b - elf2_a:
            if (elf1_a <= elf2_a and elf1_b >= elf2_a) or (elf1_b >= elf2_b and elf2_b >= elf1_a) or (elf1_a <= elf2_a and elf1_b >= elf2_b):
                total_overlap_count+=1
        else:
            if (elf2_a <= elf1_a and elf1_a <= elf2_b) or (elf2_b >= elf1_b and elf2_a <= elf1_b) or (elf2_a <= elf1_a and elf2_b >= elf1_b):
                total_overlap_count+=1
    print(total_overlap_count)

if __name__ == "__main__":
    filename = argv[1]
    read_in_file(filename)