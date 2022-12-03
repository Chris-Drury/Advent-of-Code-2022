import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
rucksack_list: list[str] = open(input_name, "r").readlines()

# Start creating the elve's groups of three
elf_group_list: list[list[str]] = []
elf_group: list[str] = []

# Build the 1d input array to the 2d array of elf groups
rucksack_tracker: int = 0
for rucksack in rucksack_list:
    rucksack.strip()
    elf_group.append(rucksack)

    rucksack_tracker += 1
    if rucksack_tracker == 3:
        rucksack_tracker = 0
        elf_group_list.append(elf_group)
        elf_group = []

# Sum of priorities
sum_of_group_priorities: int = 0

for elf_group in elf_group_list:
    for item in elf_group[0]:
        if (elf_group[1].count(item)) and (elf_group[2].count(item)):
            is_lowercase: bool = item.islower()

            item_ascii: int = ord(item) - 38

            priority: int = (item_ascii - 58) if item.islower() else (item_ascii)
            sum_of_group_priorities += priority

            break

print ("The sum of group priorities is: ", sum_of_group_priorities)