

# this calculates the sum from i=1 to n of (xi - xbar)^2
def dist_xbar_sum(xbar, lst):
    total = 0
    # go thru each elem, subtract xbar and square for positive terms
    for elem in lst:
        total += (elem - xbar) ** 2
    return total

# get XBAR and YBAR based on listed data
def get_avg_from_lst(lst):
    # sum every element in list and divide by num of elems
    total = 0
    for elem in lst:
        total += elem
    return total / len(lst)