"""
..code_author: Leaksmy Heng
Array A whose content is an integer values.
Given a particular threshold value t, an event between indices i<j is critical event if a[i] > t*a[j]
where t is the threshold value given as input from the user.

"""


def critical_event_detector(array, threshold):
    try:
        if isinstance(array, list) and (isinstance(threshold, int) or isinstance(threshold, float)):
            critical_event = 0
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    if array[i] > threshold * array[j]:
                        critical_event += 1
            return critical_event
        else:
            print('User input for array must be a list and threshold must be an int or a float.')

    except Exception as e:
        raise e


def execute(file_name):
    with open(file_name) as open_file:
        for line in open_file:
            if '[' in line:
                array = str(line).replace('\n', '').replace('[', '').replace(']', '').replace(' ', '')
                array_list = list()
                for i in array.split(','):
                    array_list.append(int(i))
                threshold = float(str(next(open_file)).replace('\n', ''))
                result = critical_event_detector(array_list, threshold)
                print(result)
        return


if __name__ == '__main__':
    execute('Problem4_input_file')
