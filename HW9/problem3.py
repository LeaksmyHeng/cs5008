"""
Conducting the analysis/research on the longest increasing subsequence problem, I found that we could actually convert
this problem to a longest common subsequence problem. In order to do that, we need to create another string array.
The new string array will be equal to the sorted of the input string array
(example: new_arr = ''.join(sorted(set(list(string_arr)))). This is due to the fact that we want to use
that sorted string array as a row to check against every column which is the input_string_array.

For example: If we have string 'efzabgh' -> we have to convert it to a sorted array: 'abefghz'. Now we will check
'abefghz' against 'efzabgh' for any common subsequence. The longest subsequence will be equal to the longest increasing
subsequence.

Time complexity analysis:
- Since we have to create a sorted string arr, this cost O(nlogn) time (python use Timsort with the worst case time
complexity of O(nlogn))
- After that we implement longest common subsequence:
    - First we create a 2D array which has n+1 row and m+1 column. But since n and m are the same length. The total time
    complexity is O(n^2). (m is the length of the input array and n is the length of the sorted input array)
    - We then loop through the 2D array by checking each row against each column and update the element in the 2D array
    using bottom up approach accordingly. Hence we create a nested for loop. This creates O(n*n) or O(n^2) time
    (length of row is the same as length of column as row is the sorted column array).

In total we have O(nlogn + n^2 + n^2); hence O(n^2) time complexity.
"""

from HW9.problem1and2 import longest_common_subsequence


def longest_increasing_subsequence(string_arr: str) -> int:
    # convert string to an array
    arr_column = list(string_arr)
    # create a sorted array based on string_list. Assuming each element are different, hence we do not have to
    # create a set of string_list then sorted it later (sorted(set(string_list)))
    sorted_arr_column = sorted(arr_column)
    arr_row = ''.join(sorted_arr_column)

    # the longest increasing subsequence here would become the longest common subsequence between
    # the sorted array (column array) and the string arr
    result = longest_common_subsequence(arr_row, string_arr)

    """
    Code for longest_common_subsequence along with comment:
    
    def longest_common_subsequence(first_string: str, second_string: str) -> int:
        first_list = list(first_string)
        second_list = list(second_string)
        len_of_first_list = len(first_list)
        len_of_second_list = len(second_list)
    
        # create a 2D array based on first_list and second_list
        # add 1 because we want the first row and column because we want the initial value to be field with 0
        # and help algorithm to start -> The total space complexity here is O(n*m)
        # and time complexity of O(n*m)
        dp_array = []
        for i in range(len_of_first_list + 1):
            dp_array.append([])
            for j in range(len_of_second_list + 1):
                dp_array[i].append(0)
    
        # Using bottom up approach in this problem.
        # loop through the element in the first_list (row) starting from the last to the first and compare it with the
        # element in the second list (column) starting from the last element as well
        # -> This nested loop generate the time complexity of O(n*m) -> The cumulative time complexity now is
        # O(n*m + n*m) = O(n*m)
        # -> Under this loop, we check the condition and update the 2D array at position (i,j). Hence does not cost any
        # additional space complexity. Therefore, the cumulative space complexity is still O(n*m)
        for i in range(len_of_first_list - 1, -1, -1):
            for j in range(len_of_second_list - 1, -1, -1):
    
                # if the element is the same, update the element in that position (i,j) to be equal to the diagonal value+1
                # otherwise get the maximum value of the value on its left and value on its bottom
                if first_list[i] == second_list[j]:
                    dp_array[i][j] = dp_array[i + 1][j + 1] + 1
                else:
                    dp_array[i][j] = max(dp_array[i + 1][j], dp_array[i][j + 1])
    
        return dp_array[0][0]

    """
    return result


if __name__ == '__main__':
    print(longest_increasing_subsequence('efzabgh'))
    print(longest_increasing_subsequence('water'))
