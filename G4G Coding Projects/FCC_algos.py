
numbers = [1,2,3,4,5,6,7,8,9,10] #value range

def verify(index): #function for linear_search
    if index is not None: #IF statement if number in range and print result
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

def verify_recursive_binary_search(result):
    print("target_rec_check1 found: ", result), ("target_rec_check2 found: ", result)
    


#linear search examples
def linear_search(list, target): #Looking for position of value in the list by index (-1, exception, 1)
    """
    Returns the position of the target if found, else Returns 'None'
    
    """
    for i in range(0, len(list)): #loop through specific range to see if value is in target list [0-end of range]
        if list[i] == target: #if i(value) is in range then return a value, otherwise list as None
            return i
    return None


#binary search examples
def binary_search(list, target): #looking for a position of value by comparison to midpoint of a range
    first = 0 #assigns values to f/l
    last = len(list) - 1 

   #comparison operation between middle and target
    while first <= last: #within loop we have a value assignment operation for middle (midpoint of value range)
        middle = (first + last)//2
        
        if list[middle] == target: #compares middle to target through loop
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None
    
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        middle = (len(list))//2
        
        if list[middle] == target:
            return True
        else:
            if list[middle] < target:
                return recursive_binary_search(list[middle+1:], target)
            else:
                return recursive_binary_search(list[:middle], target)
    
#get user input: check if valid
while True: #loops until True
    try:
        target = int(input("Enter a value: "))  # Convert input to int type
        target_rec_check1 = int(input("Enter a value for 1: "))  # Convert input to int type
        target_rec_check2 = int(input("Enter a value for 2: "))  # Convert input to int type
        
        # Check linear search
        result = linear_search(numbers, target)  
        verify(result)

        # Check binary search
        result = binary_search(numbers, target)  
        verify(result)
        
        # Check recursive_binary_search
        result = recursive_binary_search(numbers, target_rec_check1)
        verify_recursive_binary_search(result)
        result = result = recursive_binary_search(numbers, target_rec_check2)
        verify_recursive_binary_search(result)

        break  # Exit loop if input is valid
    
    except badvalue:
        print("enter a valid integer please.")


