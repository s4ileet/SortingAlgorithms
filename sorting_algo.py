# Sorting algorithms

array = [5, 6, 4, 88, 33, 22, 3, 4, 2, 4, 5, 1]


# Bubble sort
def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


print(f'Bubble sort {bubble_sort(array)}')


# Insertion sort
def insertion_sort(ins_list):
    for i in range(1, len(ins_list)):
        j = i - 1
        key = ins_list[i]
        while (ins_list[j] > key) and (j >= 0):
            ins_list[j + 1] = ins_list[j]
            j -= 1
            ins_list[j + 1] = key
    return ins_list


print(f'Insertion sort {insertion_sort(array)}')


# Selection sort
def selection_sort(sel_list):
    for index in range(0, len(sel_list)):
        iSmall = index
        for i in range(index, len(sel_list)):
            if sel_list[iSmall] > sel_list[i]:
                iSmall = i
                sel_list[index], sel_list[iSmall] = sel_list[iSmall], sel_list[index]
    return sel_list


print(f'Selection sort {selection_sort(array)}')
