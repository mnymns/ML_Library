import pandas as pd
from Simple_Lin_Reg import Regression


# read file into df
file = open('Advertising.csv')
df = pd.read_csv(file, usecols=[1, 4])
file.close()

model = Regression(df)
B1 = model.B1
B0 = model.B0
t_stat = model.t_statistic(B0)

print('r^2: ', model.r_squared)
print('t_stat (B0): ', model.t_statistic('B0'))
print('t_stat (B1): ', model.t_statistic('B1'))
print('se for B0', model.se_B0)
print('se for B1', model.se_B1)
print(f'conf int for B0 & B1: \n {model.conf_interval('B0')}\n {model.conf_interval('B1')}')

