from statistics import variance as var

"""HELPER FUNCS"""
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





"""FORMULA FUNCS"""

# B0 & B1 funcs to minimize RSS (residual sum of squares)
def get_B1(lst_x, lst_y, xbar, ybar):
    # increment num according to formula then divide by den func
    num = 0
    for i in range(len(lst_x)):
        num += (lst_x[i] - xbar) * (lst_y[i] - ybar)
    # now return finished num / den as RSS value
    return num / dist_xbar_sum(xbar, lst_x)


def get_B0(xbar, ybar, B1):
    return ybar - B1 * xbar

# calculate standard error of B0 and B1
def se_B0(xbar, lst, dist_xbar_sum_squared):
    # according to se formula, dist_xbar_sum func to help
    return var(lst) * (1 / len(lst) +
                       xbar ** 2 / dist_xbar_sum_squared)

def se_B1(dist_xbar_sum_squared, lst):
    return var(lst) / dist_xbar_sum_squared

# need to get RSE from RSS then use in SE equation





