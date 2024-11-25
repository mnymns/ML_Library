import pandas as pd

class Simple_Lin_Reg:
    # create initializer (data is a df)
    def __init__(self, data):
        self.x = data.iloc[0]
        self.y = data.iloc[1]

    

