"""
Example of median
median = [1,3,3,6,7,8,9] => n = 7 => mdn = (n + 1)/2 = (7+1)/2 = 4 => median[4] = 6
median = [1,2,3,4,5,6,8,9] => n = 8 => lower median = n/2 = 8/2 = 4 => median[4] = 4
                                  # => upper median = n/2 + 1 = 5   => median[5] = 5
We use lower median in this exercise.
Design and describe, in detail, a data structure Median - Heap to maintain a collectioin of numbers S that supports
Builds(S), Insert(x), Extract(), Peek operations.


--------------------------------------------------------Answer:------------------------------------------------------

Builds(S): we used 2 heaps to create the constructor or build which in my case is the __init__. The 2 heaps are
min_heap and max_heap that is stored as a list in the code below.

Insert(x):
if there is no elements in the max_heap and min_heap, we will insert x to the min_heap
if there is an element in min heap but there is no element in max heap,
    we check if x is greater than the element in min heap cause if x > element in min heap -> add x to max heap
    else we removed the element from min heap and store that value then insert the min heap value to max heap and
    store x in min heap
if there is (an) element(s) in both min_heap and max_heap,
    we check if x < the highest element in the min heap, if it is then we push x to min_heap
    however, if the x >= to the max value of the min heap, we push x to max heap
    after doing all the pushing, we will adjust the len of the min and max heap.
    If length of min_heap > length of max_heap, store the highest element of min_heap, then pop it
    from min_heap. With the element that we just store, we push or add it to the max_heap.
    If length of max_heap > length of min_heap, we store the min element of max_heap, then pop it from
    max_heap. The min element of max_heap that we just stored before pop is added to the min_heap.

peek(): if the length of min and max_heap is equal then return the smaller element from both min and max_heap, add it
and divide it by 2. if the length of min and max is not equal, return the top element of the heap that has the larger
size or length.

extract(): I assume extract here is remove the median element. If there are 2 median element, we remove 2 and if there
are 1 then we remove 1 element. Here is my logic:
remove the median element by checking if there is peek aka median. If there is peek, check the size of min and max heap.
if length of min_heap = length of max_heap, remove the top element form min heap and a top element from max heap. Hence
the size of min and max_heap is now n-1, n-1 respectively.
if length of max_heap < length of min_heap, remove top element of min_heap hence now there is n-1 elements for min_heap
if length of min_heap < length of max_heap, remove top element of max_heap hence now there is n-1 elements for max_heap
"""

import heapq as h


class median_heap(object):
    def __init__(self, S):
        """
        This __init__ function here is equivalent to the build function. I can't really change the constructor's name
        in python....

        Produces, in linear time, a data structure Median − Heap from an unordered input array S.
        For describing Build(S), you can assume access to the procedure Find_Median(S),
        which finds the median of S in linear time.
        :param S: unorder sorted array
        """
        self.max_heap = []
        self.min_heap = []

        for i in S:
            self.insert(i)
        h.heapify(self.max_heap)
        h.heapify(self.min_heap)

    def top_max_value_in_min_heap(self):
        return -1 * self.min_heap[0]

    def top_min_value_from_max_heap(self):
        return self.max_heap[0]

    def insert(self, x):
        """
        Insert(x): Insert element x into Median − Heap in O(log n) time.
        """
        # if both element is 0
        if not (len(self.min_heap) or len(self.max_heap)):
            h.heappush(self.min_heap, float(-1 * x))
        # if there is an element in min_heap but not max
        elif len(self.min_heap) == 1 and not len(self.max_heap):
            # if x is greater than the value in min_heap then push x to max-heap
            if x > self.top_max_value_in_min_heap():
                h.heappush(self.max_heap, float(x))
            # if x is smaller than the value in min_heap then:
            else:
                # pop a value from min heap and store it in pop_value
                # push that pop_value to max_heap
                # push x to min_heap
                pop_value = self.top_max_value_in_min_heap()
                h.heappop(self.min_heap)
                h.heappush(self.min_heap, float(-1 * x))
                h.heappush(self.max_heap, float(pop_value))
        # if there are element in both min and max_heap
        else:
            # if x is less than the max value in min_heap
            if x < self.top_max_value_in_min_heap():
                # push x to min_heap
                h.heappush(self.min_heap, float(-1 * x))
            # if x is greater or equal to max value in min_heap
            else:
                # push x to max_heap
                h.heappush(self.max_heap, float(x))

            # Adjusting the len between min and max heap after pushing
            if len(self.min_heap) > len(self.max_heap):
                pop_value = self.top_max_value_in_min_heap()
                h.heappop(self.min_heap)
                h.heappush(self.max_heap, float(pop_value))
            if len(self.max_heap) > len(self.min_heap):
                pop_value = self.top_min_value_from_max_heap()
                h.heappop(self.max_heap)
                h.heappush(self.min_heap, float(-1 * pop_value))

    def peek(self):
        '''
        Returns, in O(1) time, the value of the median of Median − Heap.
        '''

        if len(self.max_heap) == len(self.min_heap):
            return (self.top_max_value_in_min_heap() + self.top_min_value_from_max_heap()) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.top_max_value_in_min_heap()
        elif len(self.max_heap) > len(self.min_heap):
            return self.top_min_value_from_max_heap()
        return

    def extract(self):
        median = self.peek()
        if median:
            if len(self.max_heap) == len(self.min_heap):
                h.heappop(self.min_heap)
                h.heappop(self.max_heap)
            elif len(self.min_heap) > len(self.max_heap):
                h.heappop(self.min_heap)
            elif len(self.max_heap) > len(self.min_heap):
                return_val = self.top_min_value_from_max_heap()
                h.heappop(self.max_heap)
                return return_val
            return median


S = [1,3,5,6,7,8,9]

x = median_heap(S)
print(f'max heap is {x.max_heap}')
print(x.min_heap)
print(x.extract())
print(x.max_heap)
print(x.min_heap)
print(x.extract())
print(x.max_heap)
print(x.min_heap)
print(x.peek())






