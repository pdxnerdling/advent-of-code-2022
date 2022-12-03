from sys import argv

def read_in_file(filename):
    f = open(filename, 'r')
    return f.read().splitlines()

def get_summed_elf_calories(data):
    elves_calories = []
    elf = 0
    data.append('')
    for row in data:
        if row == '':
            elves_calories.append(elf)
            elf = 0
        else:
            elf+=int(row)
    return elves_calories

if __name__ == "__main__":
    data = read_in_file(argv[1])
    elven_calories = get_summed_elf_calories(data)
    print(max(elven_calories))
