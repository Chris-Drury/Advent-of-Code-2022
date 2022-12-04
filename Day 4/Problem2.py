import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
assignment_pairs_list: list[str] = open(input_name, "r").readlines()

# Track total pairs where one fully contains the other
total_overlap: int = 0

for assignment_pair in assignment_pairs_list:
    assignment_pair = assignment_pair.strip()

    assignments: list[str] = assignment_pair.split(",")

    first_assignment_sections: str = assignments[0].split("-")
    first_assignment_start: int = int(first_assignment_sections[0])
    first_assignment_end: int = int(first_assignment_sections[-1])

    second_assignment_sections: str = assignments[1].split("-")
    second_assignment_start: int = int(second_assignment_sections[0])
    second_assignment_end: int = int(second_assignment_sections[-1])

    first_earlier_within_second: bool = second_assignment_start <= first_assignment_start <= second_assignment_end
    first_later_within_second: bool = second_assignment_start <= first_assignment_end <= second_assignment_end

    second_earlier_within_first: bool = first_assignment_start <= second_assignment_start <= first_assignment_end
    second_later_within_first: bool = first_assignment_start <= second_assignment_end <= first_assignment_end

    if first_earlier_within_second or first_later_within_second or second_earlier_within_first or second_later_within_first:
        total_overlap += 1

print("Total assignment pairs overlapping: ", total_overlap)