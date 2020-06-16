import numpy as np
import pandas as pd

# create example csv without index column
lst = [[100, 'ab', 1],[200,'bc','1',],[300,'cd',1],[400, 'de',2]]
print('lst created')
df = pd.DataFrame(lst, columns=['bodyids', 'rois','weights'])
print('df made')
df.to_csv('stump.csv', index = False)
print('made to csv!')


# add index column to csv
print('starting to read csv')
df =  pd.read_csv('stump.csv')
print('read csv!!!!!!!')
df.index = np.arange(len(df.index))
print('added indices?????')
df.to_csv('stump_i.csv')
print('saved csv!!!!!!!')


# code that reads csv file and prints first 10 lines to see that we have added index column
import csv
with open('stump_i.csv', newline='') as f:
    reader = csv.reader(f)
    count  = 10
    for row in reader:
        if count >0:
            print(row)
            count -= 1
        else:
            break
