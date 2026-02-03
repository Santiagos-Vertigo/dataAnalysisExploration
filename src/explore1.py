import os
import pandas as pd

#list them in a list format row by row


data_folder = os.path.join('..', 'data')
files = os.listdir(data_folder)

files_list = [[file] for file in files]
print(pd.DataFrame(files_list, columns=['Filename']))