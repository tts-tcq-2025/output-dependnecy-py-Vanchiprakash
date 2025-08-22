major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

# New function: Generates the *strings* for the color map, but still contains the original bug
def get_color_map_strings():
    map_strings = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * 5 + j 
            # This is the line from the original code that causes the misalignment
            map_strings.append(f'{pair_number} | {major} | {minor}')
    return map_strings

def print_color_map():
    # This function now uses the new 'get_color_map_strings' and only prints
    strings_to_print = get_color_map_strings()
    for s in strings_to_print:
        print(s)
    return len(strings_to_print) # Returns count of lines printed


result = print_color_map()
assert(result == 25)
actual_map_strings = get_color_map_strings()
assert(actual_map_strings[9] == "10 | Red | Slate") # This will fail if get_color_map_strings()[9] is "10 | Red | Slate"

print("All is well (maybe!)")


