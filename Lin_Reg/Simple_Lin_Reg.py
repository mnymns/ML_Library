import stats

class Regression:
    # create initializer
    def __init__(self, x, y):
        # x & y used for iteration purposes
        self.x = x
        self.y = y
        # B1 num & den used to calculate B1
        B1_num = 0
        B1_den = 0
        # avg x & y
        self.xbar = self.x.mean()
        self.ybar = self.y.mean()


        # loop through all x, y one time to get all data needed, optimized
        for i in range(len(self.x)):
            B1_num += stats.get_B1_num(self.x.iloc[i], self.y.iloc[i], self.xbar, self.ybar)
            B1_den += stats.get_B1_den(self.x.iloc[i], self.xbar)

        # B1 & B0
        self.B1 = B1_num / B1_den
        self.B0 = stats.get_B0(self.xbar, self.ybar, self.B1)

        # get rss (residual sum of squares), rse (residual standard error), and tss (total sum of squares)
        self.rss = 0
        self.tss = 0
        # have to iterate again since B0 & B1 must be known
        for i in range(len(self.x)):
            self.rss += stats.rss(self.y.iloc[i], self.x.iloc[i], self.B0, self.B1)
            self.tss += stats.tss(self.y.iloc[i], self.ybar)
        self.rse = stats.rse(len(self.x), self.rss)

        # standard errors of B1 & B0 (B1_den is the dist from xi to xbar squared total
        self.se_B1 = stats.se_B1(B1_den, self.rse)
        self.se_B0 = stats.se_B0(self.xbar, len(self.x), B1_den, self.rse)

        # rsquared value
        self.r_squared = stats.r_sq(self.rss, self.tss)


    # function that gives confidence interval
    def conf_interval(self, beta):
        # give user option of 'B0' or 'B1' before calculating
        if beta == 'B0':
            return stats.ci_95(self.B0, self.se_B0)
        else:
            return stats.ci_95(self.B1, self.se_B1)

    # function for t statistic
    def t_statistic(self, beta):
        # give user option
        if beta == 'B0':
            return stats.t_stat(self.B0, self.se_B0)
        else:
            return stats.t_stat(self.B1, self.se_B1)
    # p value func
    def p_value(self, t_stat):
        return stats.p_value(len(self.x), t_stat)


