"""
The efficiency of the algorithm below is O(n). To find the maximum difference in the array,
- we started by getting the length of the array
- then we create a variable called min_element to store the element with the minimum value.
    By default, the element with the minimum value is the element with index 0
- after that we create another variable called max_element to store the element with the maximum value.
    By default, the element with the maximum value is the element with index 0
- Then we loop through every element in the array:
    - we then compare the element in the array to see if that element is smaller than the min_element.
        if it is, we update the min_element to that value
    - we also compare the element to the max_element. If it is, we update the max_element to that value
- at the end, our min_element and max_element should have the element with minimum value and element with the
    maximum value accordingly. Hence, we could substract the max_element to the min_element to get the
    max_difference.

From this algorithm, we only loop through our array 1 time so it is O(n) and within the loop, we create the
    comparison to search for max and min value and that operation is constant so O(1)
    => Hence, the overall runtime or efficiency of our algorithm is O(n)
"""


def finding_maximum_number_in_array(array: list) -> int:
    number_of_array = len(array)
    min_element = array[0]
    max_element = array[0]
    for i in range(number_of_array):
        min_element = min(min_element, array[i])
        max_element = max(max_element, array[i])
    return max_element - min_element


array = [5, 4, 3, 1, 9, 10]
print(finding_maximum_number_in_array(array))
