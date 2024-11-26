import math
from scipy.stats import t

# B0 & B1 funcs to minimize RSS (residual sum of squares)
def get_B1_num(xvalue, yvalue, xbar, ybar):
    # return each value, class will iterate and sum
    return (xvalue - xbar) * (yvalue - ybar)

def get_B1_den(xvalue, xbar):
    # return each value, class will iterate and sum
    return (xvalue - xbar) ** 2


def get_B0(xbar, ybar, B1):
    return ybar - B1 * xbar

# calculate standard error of B0 and B1
def se_B0(xbar, n, dist_xbar_sum_squared, rse):
    # according to se formula, dist_xbar_sum func to help
    return math.sqrt((rse ** 2) * (1 / n +
                       xbar ** 2 / dist_xbar_sum_squared))

def se_B1(dist_xbar_sum_squared, rse):
    return math.sqrt(rse ** 2 / dist_xbar_sum_squared)

# need to get RSE from RSS then use in SE equation
def rss(y, x, B0, B1):
    # sum how far each y actual is from y predicted (b0 + b1xi) then square it
    return (y - B0 - B1 * x) ** 2

def rse(n, rss):
    return math.sqrt(rss / (n - 2))

# create a confidence interval func
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
def tss(y, ybar):
    # sum of all actual y - avg y squared
    return (y - ybar) ** 2

def r_sq(rss, tss):
    return 1 - rss / tss
