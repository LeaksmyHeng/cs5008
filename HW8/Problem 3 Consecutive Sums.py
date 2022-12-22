"""
a. The brute force algorithm to calculate max S has the runtime of O(n^3). The reason is because we loop through each
    element of the array, then in that start element, we loop from there to the end of the array. When looping, we
    create an array to keep track of the loop and to sum it up. So in this case we have nested loop and a sum of the
    array in that nested loop. Sum of that temp array in the nested loop take O(n) and the two nested loop is O(n^2).
    Hence it is O(n^3) in total.

    The algorithm:
    - we loop through the length of the array so that takes O(n) time.
    - Then we have a nested loop underneath it to loop through from the start to the length of the array
        so that we could do the sum on each of the loop to create the comparison. In that nested loop,
        we create another O(n) runtime.
    - In side that nested loop, like we mention before, we try to compare each sum to the best_sum to get the max sum.
        To do that, we create a temp array called arr. Then we sum every element in arr to get cur_sum and we use
        the cur_sum to compare with the best and update the best sum to cur_sum if cur_sum > best_sum.
        As we sum the arr, we call the sum(arr) and this is O(n) runtime.
    => Hence in total we have n*n*n time so the time complexity is O(n^3) for bruteforce.

b. The efficient algorithm for the above sum would be Kadane's algorithm. The algorithm would take O(n) time.
    To implement Kadane's algorithm, we have to keep track of the current sum and the best sum.
    - The current sum is the maximum number between the element in the array and the sum of current number and element in the array.
    - The best sum is the maximum number between the current sum and the best sum.
    - Then return the best sum at the end.

    So here is our algorithm:
    - first we need to initial like both of that variable and have it equal to 0
    - Then we loop through each element of the array, when looping:
        - we find the current sum by getting the maximum value between the element in the array and the current sum + the element
        - we find the best sum by checking what is the maximum number between the current sum and the best number
    - at the end, we will return the best sum.
    By doing this, we only loop the array one time which take O(n) time and the rest is only
    to initialize or to update the variable which take constant time. So in total, this algorithm take O(n) time.
"""


def array_max_consecutive_sum_brute_force(numbers: list):
    best_sum = 0
    for start in range(len(numbers)):               # this is loop through n time so O(n)
        for end in range(start, len(numbers)):      # this is loop through n time so O(n)
            arr = numbers[start:end+1]
            cur_sum = sum(arr)                      # this is O(n) time cause we have to loop through arr to sum
            best_sum = max(cur_sum, best_sum)
    return best_sum


def array_max_consecutive_sum_kadane(numbers: list):
    cur_sum = best_sum = 0
    for num in numbers:
        cur_sum = max(num, cur_sum + num)
        best_sum = max(best_sum, cur_sum)
    return best_sum


print(array_max_consecutive_sum_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(array_max_consecutive_sum_brute_force([4]))
print(array_max_consecutive_sum_brute_force([2, -9, 5, -4, 10]))
print(array_max_consecutive_sum_brute_force([-2, 3, 2, -1]))

print('\nStarting calling kudane algo'),
print(array_max_consecutive_sum_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(array_max_consecutive_sum_kadane([4]))
print(array_max_consecutive_sum_kadane([2, -9, 5, -4, 10]))
print(array_max_consecutive_sum_kadane([-2, 3, 2, -1]))

