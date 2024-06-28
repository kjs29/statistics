import math
def stats(lst):
    # takes a list of numbers, calculates mean, standard dev, and median

    # mean
    mean = sum(lst)/len(lst)

    print(f"Mean : {mean}")

    # standard deviation
    empty = []
    for each_num in lst:
        empty.append((each_num - mean) ** 2)

    print(f"Stdev : {math.sqrt(sum(empty)/(len(lst)-1))}")

    # median
    lst = sorted(lst)
    
    # two middle numbers
    mid_left = lst[int(len(lst) / 2)]
    mid_right = lst[int(len(lst) / 2) - 1]
    
    if (len(lst) % 2 == 0):
        print(f"Median : {(mid_left + mid_right) / 2}")
    else:
        print(f"Median: {mid_left}")

stats([3, 7, 8, 12, 13, 14, 18, 21, 23, 24, 29, 32, 35])