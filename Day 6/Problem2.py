import os

# Open file
__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_name: str = __location__ + "\\" +  "input.txt"

# Read each line into an element
input: str = open(input_name, "r").readline()

marker: str

# Initialize to cover initial 4 chars
packet_index: int = 14
while packet_index < len(input):
    marker = input[(packet_index - 14):packet_index]

    unique_marker = True
    for char in marker:
        if marker.count(char) > 1:
            unique_marker = False
            break

    if unique_marker:
        print("unique marker: ", marker, " at index: ", packet_index)
        break
    packet_index += 1