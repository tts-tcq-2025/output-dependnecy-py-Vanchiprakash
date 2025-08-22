def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * len(minor_colors) + j
            color_map.append((pair_number, major, minor))

    return color_map

def format_color_map_entry(pair_number, major, minor):
    return f"{pair_number} | {major:<6} | {minor}"

def printOnconsole(lineItem):
    print(lineItem)

def print_color_map(output_func=printOnConsole):
    color_map = generate_color_map()
    for pair_number, major, minor in color_map:
        line = format_color_map_entry(pair_number, major, minor)
        output_func(line)  # Abstracted output
    return len(color_map)

#assert(result == 25)
def test_print_color_map_fail():

    # Record interaction   using Mock (Fake Dependency)
    def make_print_mock():
    #record
        calls = []

    def printmock(line):
        calls.append(line)

        printmock.calls = calls  # Attach calls list to function object
    return printmock

    mock_print = make_print_mock()
    count = print_color_map(mock_print)

    # assertions
    assert len(mock_print.calls) == 25  #value based testing
    assert mock_print.calls[0] == "0 | White  | Blue"  #interaction or Behavior Testing
    assert mock_print.calls[-1] == "24 | Violet | Slate"


