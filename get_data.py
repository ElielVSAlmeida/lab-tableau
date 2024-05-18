import pandas as pd

analysis = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/we_fn_use_c_marketing_customer_value_analysis.csv')

analysis.isna().sum()

analysis.duplicated().sum()

analysis['Effective To Date'] = pd.to_datetime(analysis['Effective To Date'])

analysis.to_csv('value_analysis.csv')