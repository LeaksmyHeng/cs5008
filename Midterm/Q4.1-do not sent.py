# Python program for implementation of Selection
# Sort
import sys

A = [5,5,5,5,5]
B = [10,11,2,3,1,45]


def func(A):
    # Traverse through all array elements
    for i in range(len(A)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            print(f'This is j here {j} with i = {i}')
            if A[i] > A[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        A[i] = A[min_idx]
        A[min_idx] = A[i]

    return A

x = func(B)
print(x)
# Driver code to test above
print("Sorted array")
for i in range(len(x)):
    print("%d" % x[i], end=" ")