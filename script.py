import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import codecademylib3_seaborn

# Combines all csv files to us_census df
census_files = glob.glob('states[0-9].csv')
li = []
for cf in census_files:
    df = pd.read_csv(cf)
    li.append(df)
us_census = pd.concat(li, axis=0)
#print(us_census.head())
