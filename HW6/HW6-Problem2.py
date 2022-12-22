# Problem 2
# For our algorithm, we will sort
#       the height of the skiers in ascending order -> Example = [4.9, 5, 5.2, 5.5, 6]
#       the height of the pair of skis in ascending order too -> Example = [5, 5.2, 5.5, 6.2]
# After the height of the skiers and the pair of skis are sorted, we will assigned the 1st skier to the 1st ski,
# the 2nd skier to the 2nd ski and so on

# As for the time complexity:
#   sorting the height of the skiers take O(nlogn) where n is the number of skiers (quick sort)
#   sorting the height of the skis take O(mlogm) where m is the number of skis (quick sort)
#   at the end we do another for loop to pair skiers to the skis and it takes O(n)
# Hence, it sort it takes O(nlogn) time where n is the number of skis and skiers

# Proof by contracted: Our algo gives the minimum absolute sum of the dif between ski height and skier height = False
# Assume number of skis and skiers are the same
# Height of skier = [4.5, 5.0, 6.1]
# Height of skis = [5.1, 5.5, 6.0]
# All cases:    |4.5 - 5.1| + |5.0 - 5.5| + |6.1 - 6.0| = 0.6 + 0.5 + 0.1 = 1.2 (This is the algorithm)
#               |4.5 - 5.5| + |5.0 - 6.0| + |6.1 - 5.1| = 1.0 + 1.0 + 1.0 = 3   (if we don't sum by sorting)
#               |4.5 - 6.0| + |5.0 - 5.1| + |6.1 - 5.5| = 1.5 + 0.1 + 0.6 = 2.2 (if we don't sum by sorting)
# From here we are able to see, if we don't map the first skier to the first pair of skis in ascending order,
# we won't be able to get the min absolute different of 1.2. Hence our algorithm is optimal


def pair_ski(list_of_skier: list, list_of_skis: list) -> dict:
    """
    This code would be to pair skier to the pair of skis.
    We assume that the number of skies and the number of skiers are the same
    so that no one would be left without ski.

    :param list_of_skier: list of the height of the skiers
    :param list_of_skis: list of the height of the pair of skis
    :return: dictionary that map the height of skiers to skis
    """
    sorted_skier = sorted(list_of_skier)
    sorted_skis = sorted(list_of_skis)
    dict_ski_skiers = {}
    if len(sorted_skier) == len(sorted_skis):
        for i in range(len(sorted_skier)):
            if i not in dict_ski_skiers:
                dict_ski_skiers[i] = {'skier_height': sorted_skier[i],
                                      'skis_height': sorted_skis[i]}
        return dict_ski_skiers
    print('Number of skis and skiers are not the same')
    return dict_ski_skiers


print(pair_ski([7, 6.5, 4.9, 5, 5.2, 5.5, 6], [6.5, 5, 5.2, 7.5, 5.5, 6.2, 4.9]))



