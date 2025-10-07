import numpy as np
import pandas as pd
import sklearn
import matplotlib as plt

print('numpy version:', np.__version__)
print('pandas version:', pd.__version__)
print('sklearn version:', sklearn.__version__)
print('matplotlib version:', plt.__version__)

path = "C:\\Users\\mason\\OneDrive\\Desktop\\Data Mining & Text Analytics\\InClassLab\\MATH3110_project_template\\data\\raw\\Auto.csv"
auto_df = pd.read_csv(path)
auto_df.head()

print(auto_df.isnull().sum())

print(auto_df.dtypes)

