import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
calories_list: list[str] = open(input_name, "r").readlines()

# Keep track of highest, and local calorie count
top_elf_calories: float = 0
elf_calories: float = 0

# For each calorie, add to local calories, if highest record.
for calorie in calories_list:
    calorie = calorie.strip()

    if calorie:
        elf_calories += float(calorie)
    else:
        # Elf count has ended, check if highest so far
        if top_elf_calories <= elf_calories:
            top_elf_calories = elf_calories
            print("highest so far: ", top_elf_calories)

        elf_calories = 0

# Give me my answer
print("Highest calories (fat elf): ", top_elf_calories)
