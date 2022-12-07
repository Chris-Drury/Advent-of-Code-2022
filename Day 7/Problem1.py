import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" +  "exampleInput.txt"

# Read each line into an element
command_input = open(input_name, "r")

size_threshold: int = 100000

total_smaller_directories: int = 0

# Recursive strategy for entering directories
def get_directory_size():
    global total_smaller_directories
    directory_size = 0

    command = command_input.readline()
    while command:
        while not "$ " in command and not "dir " in command and command:
            command_split = command.split()

            for piece in command_split:
                if piece.isdigit():
                    directory_size += int(piece)
                    break
        
            command = command_input.readline()

        if "cd " in command:
            if ".." in command:
                if directory_size < size_threshold:
                    total_smaller_directories += directory_size

                return directory_size
            
            directory_size += get_directory_size()

        command = command_input.readline()

    if directory_size < size_threshold:
        total_smaller_directories += directory_size

    return directory_size

command: str = command_input.readline()

get_directory_size()

print(total_smaller_directories)