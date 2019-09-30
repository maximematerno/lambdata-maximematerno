
import pandas as pd
import numpy as np


def null(df):
    
	if df.isnull().values.any():
		return True, df.isnull().sum()
	else:
        return False, df.isnull().sum()