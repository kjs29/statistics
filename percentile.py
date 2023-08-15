import math
def stats(lst):
    # takes a list of numbers, calculates mean, standard dev, median

    # mean
    mean = sum(lst)/len(lst)

    print(f"mean : {mean}")

    # standard deviation
    empty = []
    for each_num in lst:
        empty.append((each_num - mean) ** 2)

    print(f"Stdev : {math.sqrt(sum(empty)/(len(lst)-1))}")

    # median

    lst = sorted(lst)
    if (len(lst)%2 ==0):
        print((lst[int(len(lst)/2)]+ lst[int(len(lst)/2)-1])/2)
    else:
        print(lst[int(len(lst)/2)])

    percentile = 0.9
    
    print(lst[int(percentile * len(lst) - 1)])

    for i,each in enumerate(lst):
        lst[i]=[each,f"{i+1}th"]

    for each in lst[::-1]:
        print(each)
