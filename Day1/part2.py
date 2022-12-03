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

def total_top_3(elven_calories):
    elven_calories.sort(reverse=True)
    top_3 = 0
    for i in range(3):
        top_3+=elven_calories[i]
    return top_3

if __name__ == "__main__":
    data = read_in_file(argv[1])
    elven_calories = get_summed_elf_calories(data)
    print(total_top_3(elven_calories))
