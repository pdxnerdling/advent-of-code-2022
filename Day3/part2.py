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
    while len(rucksacks) > 0:
        first = rucksacks.pop()
        second = rucksacks.pop()
        third = rucksacks.pop()
        matches = [item for item in first if second.count(item) > 0]
        for match in matches:
            if third.count(match) > 0:
                priority_sum+=get_priority_value(match)
                break
    return priority_sum

if __name__ == "__main__":
    rucksacks = read_in_file(argv[1])
    print(sum_item_priorities(rucksacks))