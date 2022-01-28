# Sorting algorithms

array = [5, 6, 4, 88, 33, 22, 3, 4, 2, 4, 5, 1]


# Bubble sort
def bubble_sort(seq):
    for rep in range(len(seq)-1):
        for i in range(len(seq) - 1 - rep):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq


print(f'Bubble sort {bubble_sort(array)}')


# Insertion sort
def insertion_sort(ins_list):
    for rep in range(1, len(ins_list)):
        for i in range(rep, 0, -1):
            if ins_list[i] < ins_list[i-1]:
                ins_list[i], ins_list[i - 1] = ins_list[i - 1], ins_list[i]
            else:
                break
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
