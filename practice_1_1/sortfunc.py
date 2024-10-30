from practice_1_1.decorator import check_time

nums = [5, 6, 2, 1, 3, 4]


@check_time
def bubble_sort(lst):
    """Cортировка пузырьковым методом"""
    b_lst = lst.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(b_lst) - 1):
            if b_lst[i] > b_lst[i + 1]:
                b_lst[i], b_lst[i + 1] = b_lst[i + 1], b_lst[i]
                swapped = True
    return b_lst


@check_time
def selection_sort(lst):
    """Cортировка выборкой"""
    s_lst = lst.copy()
    for i in range(len(s_lst)):
        lowest = i
        for j in range(i + 1, len(s_lst)):
            if s_lst[j] < s_lst[lowest]:
                lowest = j
        s_lst[i], s_lst[lowest] = s_lst[lowest], s_lst[i]
    return s_lst


@check_time
def insertion_sort(lst):
    """Сортировка вставкой"""
    i_lst = lst.copy()
    for i in range(1, len(i_lst)):
        key = i_lst[i]
        j = i - 1
        while i_lst[j] > key and j >= 0:
            i_lst[j + 1] = i_lst[j]
            j -= 1
        i_lst[j + 1] = key
    return i_lst



if __name__ == '__main__':
    print(nums)
    print()
    # print(bubble_sort(nums))
    # print(selection_sort(nums))
    # print(insertion_sort(nums))
    bubble_sort(nums)
    selection_sort(nums)
    insertion_sort(nums)
