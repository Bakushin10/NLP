import pandas as pd
from openpyxl import Workbook

filepath_in = "/home/shin/Desktop/aaa.csv"
pd.read_csv(filepath_in, delimiter=",").to_excel("foo.xlsx", index=False)
