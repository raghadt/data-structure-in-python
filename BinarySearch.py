def binary_search(input_array, value):
    """Your code goes here."""
    left=0
    right = len(input_array)
    while left<=right:
        print(left)
        print(right)
        mid = (left+right)//2
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            right = mid - 1
        else:
            left=mid + 1
    return -1

binary_search(test_list, test_val1)