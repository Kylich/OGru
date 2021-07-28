import pandas
import openpyxl
import xlsxwriter
import xlrd

prodList = pandas.read_excel('Service-2021-07-28.xlsx', index_col='Id')
print(prodList)

# for prod in prodList:
#     print(prod)