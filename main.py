import copy
import random


def my_func(x):
    return x ** 2


def create_odds(numsInList):
    # Creates a list of len(num) of random odd numbers between 1 and 1000
    num_list = []
    while numsInList > 0:
        new_num = random.randint(1, 1000)
        if new_num % 2 == 0:
            num_list.append(new_num)
            numsInList -= 1
    return num_list


def create_evens(numsInList):
    # Creates a list of len(num) of random even numbers between 1 and 1000
    num_list = []
    while numsInList > 0:
        new_num = random.randint(1, 1000)
        if new_num % 2 != 0:
            num_list.append(new_num)
            numsInList -= 1
    return num_list


class something:

    def __init__(self):
        self.values = [1, 2, 3, 4]

    # Pull request 3
    def check_for_val(self, val):

        # This member function checks to see if val exists in the class member
        # values and returns True if found
        for i in self.values:
            if i == val:
                return True
        return False


def get_val_index(nums, trg):
    # Searches arr for val and returns the index if found, otherwise -1
    for i in nums:
        if i == trg:
            return i
    return -1


# This is a global variable used by other functions, do not change
int_arr = [1, 2, 5, 2, 10, 45, 9, 100]


def print_sorted(nums):
    # Prints the items in the array after sorting
    nums_copy = copy.deepcopy(nums)
    nums_copy.sort()
    for num in nums_copy:
        print(num)


if __name__ == '__main__':
    g = something()
    arr = [1, 2, 6, 4, 5, 3]
    print_sorted(arr)
    print(arr)
