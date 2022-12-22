"""
Problem1:
To achieve the time complexity of O(n*m), we are using dynamic programming bottom up approach.
    First we create an array (n+1)*(m+1) called dp and populate all elements in the array to 0.
    Then we loop through the array starting from the last element in the row. Then check the element of that row against
        every elements in the column (hence, create nested for loop). For example: the word 'HELO' and 'HEL'.
        First, we will check O against L, then E, then H.
    If the element is the same (first_list[i] == second_list[j]), we will update the dp array in position i and j to the
        diagonal value of (i, j) + 1 (dp[i][j] = dp[i + 1][j + 1] + 1).
    However, if the element is not the same (first_list[i] != second_list[j]), we will check its
        left value (dp[i + 1][j]) and its bottom value (dp[i][j + 1]) then grab the maximum out of those two and
        update the dp position i and j to that max value.
    At the end we will return the top element with is dp[0][0].
    Since we have to create an array first, it costs O(n*m)
    Then we loop through every row in the array and compare each row to every element, it costs O(n*m)
    The total cost is O(n*m + n*m); hence O(n*m) time complexity.

Problem2:
As elaborating in the first problem, we first created a 2D array that has (n+1)*(m*1). Hence the space complexity is
O(n*m). Then we loop through the element in the array, and update the row,col of that array according to our
condition. Hence, we do not actually create any additional space.
Therefore, the total space complexity for this algorithm is O(n*m).

Please see the code/comment for more elaboration.
"""


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


if __name__ == '__main__':
    print(longest_common_subsequence('hello', 'hallow'))
