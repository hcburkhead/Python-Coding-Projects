numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # value range  

# Function to verify the linear search results  
def verify(index, function_type):  
    if index is not None:  
        print(f"{function_type} Target found at index:", index)  
    else:  
        print(f"{function_type} Target not found in list")  

# Function to verify recursive binary search results  
def verify_recursive_binary_search(result, target):  
    if result is not None:  
        print(f"RecBinary Search Target {target} found at index: {result}")  
    else:  
        print(f"RecBinary Search Target {target} not found in list")  

# Binary search function  
def verify_binary_search(index, function_type):  # Accept index and function type as parameters  
    if index is not None:  
        print(f"{function_type} Target found at index:", index)  
    else:  
        print(f"{function_type} Target not found in list")  

# Linear search function  
def linear_search(lst, target):  # Looking for position of value in the list  
    """  
    Returns the position of the target if found, else returns 'None'  
    """  
    for i in range(len(lst)):  
        if lst[i] == target:  
            return i  
    return None  

# Binary search function  
def binary_search(lst, target):  
    first = 0  
    last = len(lst) - 1  

    while first <= last:  
        middle = (first + last) // 2  
        if lst[middle] == target:  
            return middle  
        elif lst[middle] < target:  
            first = middle + 1  
        else:  
            last = middle - 1  

    return None  

# Recursive binary search function  
def recursive_binary_search(lst, target):  
    if len(lst) == 0:  
        return None  
    middle = len(lst) // 2  
    if lst[middle] == target:  
        return middle  
    elif lst[middle] < target:  
        result = recursive_binary_search(lst[middle + 1:], target)  
        return (middle + 1 + result) if result is not None else None  
    else:  
        return recursive_binary_search(lst[:middle], target)  

# Main loop for user input  
while True:  
    input_value = input("Enter a value (or press Enter to exit): ")  

    if input_value == "":    
        print("Exiting the program.")  
        break  # Exit the loop  
    
    try:  
        target = int(input_value)  # Convert input to int type  

        if target < 1 or target > 10:  
            print("Please enter an integer within the range of 1 to 10.")  
            continue  # Ask for input again if outside range  

        # Check linear search  
        result = linear_search(numbers, target)  
        verify(result, "Linear Search")  # Pass function type here  

        # Check binary search  
        result = binary_search(numbers, target)  
        verify_binary_search(result, "Binary Search")  # Pass function type here  

        # Check recursive_binary_search  
        result = recursive_binary_search(numbers, target)  
        verify_recursive_binary_search(result, target)    

    except BadValue:  # Catch from invalid input  
        print("Enter a valid integer please.")


