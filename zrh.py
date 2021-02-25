import pandas as pd

class Row(object):
    index = ''
    count_2017 = 0
    count_2018 = 0
    count_2019 = 0
    def __init__(self, index):
        self.index = index
    def change_index(self, index):
        self.index = index
    def count_2017_add(self):
        self.count_2017 += 1
    def count_2018_add(self):
        self.count_2018 += 1
    def count_2019_add(self):
        self.count_2019 += 1
    def clear_data(self):
        self.index = ''
        self.count_2017 = 0
        self.count_2018 = 0
        self.count_2019 = 0

excel_file_path = "data.xlsx"
sheet = pd.read_excel(io=excel_file_path, converters={'股票代码':str, '会计年度':str, '关键审计事项类型':str})
result_sheet = pd.DataFrame(columns=('股票代码','会计年度','关键审计事项个数'))

df = sheet.set_index('股票代码')
temp_index = '0'
temp_row = Row(temp_index)
for index, row in df.iterrows():
    if temp_index != index:
        #保存上一条数据
        result_sheet = result_sheet.append(pd.DataFrame({'股票代码':[temp_row.index], '会计年度':['2017'], '关键审计事项个数':[temp_row.count_2017]}), ignore_index=True)
        result_sheet = result_sheet.append(pd.DataFrame({'股票代码':[temp_row.index], '会计年度':['2018'], '关键审计事项个数':[temp_row.count_2018]}), ignore_index=True)
        result_sheet = result_sheet.append(pd.DataFrame({'股票代码':[temp_row.index], '会计年度':['2019'], '关键审计事项个数':[temp_row.count_2019]}), ignore_index=True)
        #清除对象数据
        temp_row.clear_data()
        #重新填充对象
        temp_index = index
        temp_row.change_index(index)
    if row['会计年度'] == '2017':
        temp_row.count_2017_add()
    elif row['会计年度'] == '2018':
        temp_row.count_2018_add()
    else:
        temp_row.count_2019_add()

# result_sheet.drop(labels=[1,3], inplace=True)#删除无用的前三行

result_sheet.to_excel('result.xlsx', index=False)