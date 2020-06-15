import numpy as np
import pandas as pd


df =  pd.read_csv('all_connections.csv')
print('read csv!!!!!!!')
df.index = [np.arange(len(df.index)), df.index]
print('added indices?????')
df.to_csv('all_connections_i.csv')
print('saved csv!!!!!!!')