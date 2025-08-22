def print_color_map():
    result_dict = dict()
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            number_code = i*5+1+j
            major_color = major
            minor_color = minor
           
            print(f'{number_code} | {major_color} | {minor_color}')
            result_dict[number_code] = [major_color, minor_color]
    return result_dict
 
 
result = print_color_map()
assert(result[25] == ["Violet","Slate"])
print("All is well (maybe!)")
