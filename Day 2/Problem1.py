import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" + "input.txt"

# Read each line into an element
round_list: list[str] = open(input_name, "r").readlines()

# Define the 'encrypted' values
# [Rock, Paper, Scissors]
opponent_choices: list[str] = ["A", "B", "C"]
my_choices: list[str] = ["X", "Y", "Z"]

# Define the point values for winning with index corresponding index
index_key: list[int] = [1, 2, 3]

opponent_total_score: int = 0
my_total_score: int = 0

for round in round_list:
    round.strip()
    
    opponent_choice: str = round.split()[0]
    my_choice: str = round.split()[-1]

    opponent_choice_index = opponent_choices.index(opponent_choice)
    my_choice_index = my_choices.index(my_choice)

    index_difference = opponent_choice_index - my_choice_index

    if index_difference == 1 or index_difference == -2:
        opponent_total_score += (6 + index_key[opponent_choice_index])
        my_total_score += index_key[my_choice_index]

    elif index_difference == -1 or index_difference == 2:
        opponent_total_score += index_key[opponent_choice_index]
        my_total_score += (6 + index_key[my_choice_index])

    else:
        opponent_total_score += (3 + index_key[my_choice_index])
        my_total_score += (3 + index_key[my_choice_index])

print("Opponent's final score:", opponent_total_score, ". My final score: ", my_total_score)