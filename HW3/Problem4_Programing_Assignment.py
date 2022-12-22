"""
Given an integer array nums, find a contiguous non-empty subarray within the array that ahs the largest product
and return the product.
"""


def find_largest_product(nums):
    # Check if the user uses list as an array, if not then throw/raise Value Error
    if not isinstance(nums, list):
        raise ValueError

    else:
        result = 0
        # constraint 1: 1 <= nums.length <= 2 * 10^4
        if 1 <= len(nums) <= 20000:
            for i in range(len(nums)-1):
                next_element = nums[i+1]
                prev_element = nums[i]

                # checking if the element is integer or not, if not raise ValueError
                if isinstance(next_element, int) and isinstance(prev_element, int):
                    # Check if it is a contiguous number_array
                    if abs(next_element - prev_element) == 1:
                        # constraint 2: -10 <= nums[i] <= 10
                        if -10 <= next_element <= 10 and -10 <= prev_element <= 10:
                            new_result = next_element * prev_element
                            # constraint 3: The product is guaranteed to fit in a 32-bit integer which is
                            # in between -2147483648 to 2147483647.
                            if -2147483648 <= new_result <= 2147483647:
                                # If the new result is higher than the previous result, update that
                                if new_result > result:
                                    result = new_result
                else:
                    # if not satisfy constraint 1, raise Value Error
                    raise ValueError
                i += 1
        else:
            # If the len of the list is not in between 1 and 2000 raise value error
            raise ValueError

        return result


if __name__ == '__main__':
    array1 = [2, 3, -2, 4]
    array2 = [-2, 0, -1]
    array3 = [-5, -4, 3, 2, 5, 9, 8]
    array4 = [-12, -11, -10, -9, 5, 3, 9, 8, 10, 11, 1, 0, 9, 10]
    print(find_largest_product(array1))
    print(find_largest_product(array2))
    print(find_largest_product(array3))
    print(find_largest_product(array4))

