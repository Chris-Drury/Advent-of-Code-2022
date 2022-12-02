import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
calories_list: list[str] = open(input_name, "r").readlines()
calories_list.append("") # do this to give a chance to calculate for last set further below


# Keep track of highest calories, and local calorie count
all_elf_calories: list[float] = [0]
elf_calories: float = 0

# For each calorie, add to local calories, if highest record.
for calorie in calories_list:

    calorie = calorie.strip()

    if calorie:
        elf_calories += float(calorie)
    else:
        # Elf count has ended, apppend the total to a list
        all_elf_calories.append(elf_calories)

        elf_calories = 0

# Sort in ascending order
all_elf_calories.sort()

# Get the top three values
top_elf_calories: list[float] = all_elf_calories[-3:]

# Give me my answer
print("Highest 3 calorie counts (fat elves): ", top_elf_calories[-3:])
print("Highest 3 calorie counts aggregated: ", sum(top_elf_calories[-3:]))

