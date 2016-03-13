import time


def timed_sort(list, key, algorithm='insertion'):
    sort_func = globals()[algorithm]
    start_time = time.time()
    sorted_list = sort_func(list, key=key)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (sorted_list, elapsed_time)


def insertion(list, key=lambda item: item):
    size = len(list)
    for i in range(1, size):
        for j in range(i, 0, -1):
            compare = list[j - 1]
            current = list[j]
            if key(current) < key(compare):
                list[j] = compare
                list[j - 1] = current

    return list


def selection_sort(array):
    """
    Find the lowest value O(n)
    Put it in a new array O(1)
    Find the next highest value O(n)
    Put it in front of the previous sorted card O(1)
    Repeat 3 and 4 until you have all the values sorted
    O(n^2)
    """
    copy = array[:]
    sorted = []
    size = len(array)
    for _ in range(size):
        smallest_index = 0
        for i in range(len(copy)):
            if copy[i] < copy[smallest_index]:
                smallest_index = i
        sorted.append(copy[smallest_index])
        del copy[smallest_index]
    return sorted


def insertion_sort(array):
    """A bit faster insertion sort

    This variation decides where the index should be before inserting.
    O(n^2)
    """
    if not array:
        return []
    end = start = array[0]
    sort = [start]  # The returned array; TODO optimize to be in-place
    for val in array[1:]:
        # print(sort, start, end, val)  # Debug
        # insert at beginning if < min
        if val < start or val == start:
            sort.insert(0, val)
            start = val
        # insert at end if > max
        elif val > end or val == end:
            sort.append(val)
            end = val
        else:
            # Figure out what the index should be
            num = len(sort) * (val - start) / (end - start)
            # print(num)  # Debug
            idx = int(num)
            # print("pre idx:", idx)  # Debug
            # Insertion sort from the index
            if val < sort[idx]:
                while val < sort[idx - 1]:
                    idx -= 1
                # print("< idx:", idx)  # Debug
                # O(N) time to insert :(
                sort.insert(idx, val)
            elif val > sort[idx]:
                while val > sort[idx + 1]:
                    idx += 1
                # print("> idx:", idx)  # Debug
                sort.insert(idx + 1, val)
            else:
                sort.insert(idx, val)
    return sort
