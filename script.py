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

# Use Regex to remove $ signs in Income column
us_census['Income'] = us_census['Income'].replace('\$', '', regex = True)

# Split GenderPop in to a Men column and a Women column
us_census[['Men', 'Women']] = us_census['GenderPop'].str.split('_', expand=True)

# Remove M and F from Men and Women columns
# Convert each values to a number
us_census['Men'] = us_census['Men'].replace('M', '', regex = True)
us_census['Men'] = us_census['Men'].fillna(0)
pd.to_numeric(us_census['Men'])
us_census['Women'] = us_census['Women'].replace('F', '', regex = True)
us_census['Women'] = us_census['Women'].fillna(0)
pd.to_numeric(us_census['Women'])
