import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
rucksack_list: list[str] = open(input_name, "r").readlines()

# Sum of priorities
sum_of_priorities: int = 0

for rucksack in rucksack_list:
    rucksack.strip()

    first_compartment: str = rucksack[:len(rucksack) // 2]
    second_compartment: str = rucksack[len(rucksack) // 2:]

    for item in first_compartment:
        item_count: int = second_compartment.count(item)

        if item_count:
            is_lowercase: bool = item.islower()

            item_ascii: int = ord(item) - 38

            priority: int = (item_ascii - 58) if item.islower() else (item_ascii)
            sum_of_priorities += priority

            break

print ("The sum of priorities is: ", sum_of_priorities)