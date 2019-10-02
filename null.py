
import pandas as pd
import numpy as np


class Null_checker():

    def __init__(self, df):
        self.df = pd.DataFrame()

    def null(self):

        if df.isnull().values.any():
            return True, df.isnull().sum()
        else:
            return False, df.isnull().sum()
