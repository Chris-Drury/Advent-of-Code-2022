import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" +  "input.txt"

# Read each line into an element
command_input = open(input_name, "r")

size_threshold: int = 100000
filesystem_size: int = 70000000
unused_space_size: int = 30000000

total_filesystem_size: int = 0
total_smaller_directories: int = 0

directory_sizes: list[int] = []

# Recursive strategy for entering directories
def get_directory_size():
    global total_filesystem_size
    global total_smaller_directories
    global directory_sizes
    directory_size = 0

    command = command_input.readline()
    while command:
        while not "$ " in command and not "dir " in command and command:
            command_split = command.split()

            for piece in command_split:
                if piece.isdigit():
                    total_filesystem_size += int(piece)
                    directory_size += int(piece)
                    break
        
            command = command_input.readline()

        if "cd " in command:
            if ".." in command:
                if directory_size < size_threshold:
                    total_smaller_directories += directory_size

                directory_sizes.append(directory_size)
                return directory_size
            
            directory_size += get_directory_size()

        command = command_input.readline()

    if directory_size < size_threshold:
        total_smaller_directories += directory_size

    directory_sizes.append(directory_size)
    return directory_size

command: str = command_input.readline()

get_directory_size()

print("Total Filesystem Size: ", total_filesystem_size, 
" Aggregation of smaller filesystem sizes: ", total_smaller_directories)

optimal_directory_size: int = filesystem_size

for size in directory_sizes:
    resulting_directory: int = total_filesystem_size - size

    if resulting_directory <= (filesystem_size - unused_space_size):
        if size < optimal_directory_size:
            optimal_directory_size = size

print ("optimal directory to delete size: ", optimal_directory_size)