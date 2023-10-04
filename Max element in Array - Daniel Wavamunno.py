

def find_max(arr) :

    max_element = array[0]
    for element in array:
        if element > max_element:
            max_element = element
    return max_element

array = (10, 20, 24, 48, 91, 405, 231)
max_value = find_max (array)
print (f"The maximum element:", max_value)