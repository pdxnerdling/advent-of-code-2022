from sys import argv

def read_in_file(filename):
    f = open(filename, 'r')
    return f.read().splitlines()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def get_priority_value(letter):
    letter_val = ord(letter)
    priority_value = letter_val-96
    if letter.isupper():
        priority_value = letter_val - 38
    return priority_value

def sum_item_priorities(rucksacks):
    priority_sum = 0
    for sack in rucksacks:
        items_per_compartment = int(len(sack) / 2)
        first_half = sack[:items_per_compartment]
        second_half = sack[items_per_compartment:]
        letter = [item for item in first_half if second_half.count(item) > 0] 
        priority_sum+=get_priority_value(letter.pop())
    return priority_sum

if __name__ == "__main__":
    rucksacks = read_in_file(argv[1])
    print(sum_item_priorities(rucksacks))