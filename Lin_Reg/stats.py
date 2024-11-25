import math
import helper as h
from scipy.stats import t

# B0 & B1 funcs to minimize RSS (residual sum of squares)
def get_B1(lst_x, lst_y, xbar, ybar):
    # increment num according to formula then divide by den func
    num = 0
    for i in range(len(lst_x)):
        num += (lst_x[i] - xbar) * (lst_y[i] - ybar)
    # now return finished num / den as RSS value
    return num / h.dist_xbar_sum(xbar, lst_x)


def get_B0(xbar, ybar, B1):
    return ybar - B1 * xbar

# calculate standard error of B0 and B1
def se_B0(xbar, lst, dist_xbar_sum_squared, rse):
    # according to se formula, dist_xbar_sum func to help
    return math.sqrt(rse * (1 / len(lst) +
                       xbar ** 2 / dist_xbar_sum_squared))

def se_B1(dist_xbar_sum_squared, rse):
    return math.sqrt(rse / dist_xbar_sum_squared)

# need to get RSE from RSS then use in SE equation
def rss(lst_y, lst_x, B0, B1):
    # sum how far each y actual is from y predicted (b0 + b1xi) then square it
    total = 0
    for i in range(len(lst_y)):
        total += lst_y[i] - B0 - B1 * lst_x[i]
    return total

def rse(n, rss):
    return math.sqrt(rss / (n - 2))

# create a confidence interval func so that user can choose which beta value
# have to intake se equation already completed
def ci_95(beta, se):
    return [beta - 2 * se, beta + 2 * se]

# t-statistic to test hypo test
def t_stat(beta, se):
    return beta / se

# p-value using t-distribution and t-statistic (df = n - 2)
def p_value(n, t_stat):
    return 2 * t.sf(t_stat, n - 2)

# get tss for r squared value
def tss(lst_y, avg_y):
    # sum of all actual y - avg y squared
    total = 0
    for y in lst_y:
        total += (y - avg_y) ** 2

def r_sq(rss, tss):
    return 1 - rss / tss
