def binary_search(lst, item):
    # low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(lst) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = lst[mid]
        # Found the item.
        if guess == item:
            return mid
        # The guess was too high.
        if guess > item:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1
    return None  # Item doesn't exist


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))  # => 0

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1))  # => None
