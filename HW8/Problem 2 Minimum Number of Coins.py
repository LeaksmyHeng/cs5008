""""
To solve this issue here, we are using a dynamic programming bottom-up approach since the recursive approach
would give us an exponential runtime.
In this approach,
1. first we are checking for base case which is if the total_sum is 0. If it is 0 then we do not have to do
    anything but return 0 cause we don't have to add or check.
2. if it is not, we are going to create a variable result which is equal to the value of the 64bit (2^63). We use
    this to check whether there will be an overflow or not and this value will get updated once we loop through
    out coin list
3. after creating that variable, we are going to create a dp_table by looping through the total_sum + 1. In the 0
    element of that array, we are going to give its value 0 otherwise the result value (2^63). These values will
    get updated once we implement the bottom-up
4. last but not least, we implement bottom up here. In here, we are going to loop through the total_sum starting at
    1 all the way to total_sum + 1. In a sense, we are checking all of the amount starting at amount = 1.
    - Then we are going to loop through each of the coin so that we could check if the amount - coin is >=0
        because if is >= 0 then we can continue searching and find the solution to our
        dynamic programing and store it in the table we create in 3. Now if it is greater than 0,
        we will check if our temp table to see if the element in which amount - coin is different from the
        result and if it is smaller than the value in the dp table (table[amount]).
        If it is, we will update the table in that amount index, to the smallest value

    We will return the dp table at the amount index. But if we could not compute the total amount which mean the
    table at amount index is the same as the result (2^63) then we will return -1

With this approach we are taking O(m*V) where m is the length of the array and V is the total_sum.
This is because we have to loop through the total_sum first which take O(V) then we loop through the length of the
array later which take O(m). We do have the first for loop to generate the table and that is O(V).
So overall it should be O(V + m*V) -> hence, O(m*V)
"""

import sys


def find_minimum_number_of_coin(distinct_coin: list, total_sum: int) -> int:
    # base case cause if the total sum is 0, we don't have to do anything
    if total_sum == 0:
        return 0

    # fetch the largest 64-bit value -> 2^63
    result = sys.maxsize

    table = []
    for i in range(total_sum + 1):
        if i == 0:
            table.append(0)
        else:
            table.append(result)

    for amount in range(1, total_sum + 1):
        for coin in distinct_coin:
            if amount - coin >= 0:
                if (table[amount - coin] != result) and (table[amount - coin] < table[amount]):
                    table[amount] = table[amount - coin] + 1

    # if we could not compute the total sum
    if table[total_sum] == result:
        return -1

    return table[total_sum]


print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 9))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 0))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 17))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 7))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 15))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 3))
print(find_minimum_number_of_coin([9, 2, 4, 5, 1, 8], 50))