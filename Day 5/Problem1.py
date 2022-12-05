import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" +  "input.txt"

# Read each line into an element
lines: list[str] = open(input_name, "r").readlines()

stack_rows: list[list[str]] = []
number_of_stacks: int = 0

at_commands: bool = False
commands: list[int] = []

# Read in: stack rows, number of stacks, and then commands
for line in lines:
    line = line.rstrip()

    if not at_commands and (line.count("[") > 0):
        while len(line) % 4 > 0:
            line += " "

        stack_rows.append(list(map(''.join, zip(*[iter(line)]*4))))

    elif not at_commands and not line:
        at_commands = True

    elif not at_commands:
        number_of_stacks = len(line) - line.count(" ")

    elif at_commands:
        line = line.strip().replace(" from ", "-").replace(" to ", "-").replace("move ", "")
        commands.append(line.split("-"))

# Prepare stacks properly to allow for transpose
for row in stack_rows:
    while len(row) < number_of_stacks:
        row.append("    ")

    for crate in row:
        if crate:
            row[row.index(crate)] = crate[1]
    
# Transpose rows to stacks for operations
stack_rows: list[list[str]] = list(zip(*stack_rows))
stacks: list[list[str]] = []

# remove empty crates from stacks
for stack in stack_rows:
    stack = list(stack)
    while " " in stack:
        stack.remove(" ")
    
    stack.reverse()
    stacks.append(list(stack))

for command in commands:
    amount: int = int(command[0])
    origin: int = int(command[1]) - 1
    destination: int = int(command[2]) - 1

    while (len(stacks[origin]) >= amount) and (amount > 0):
        crate = stacks[origin].pop()
        stacks[destination].append(crate)
        amount -= 1

print("Crate stacks: ")
for stack in stacks:
    print(stack)