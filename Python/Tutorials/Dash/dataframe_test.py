import pandas as pd
import numpy as np

def isfloat(string):
    if string=='inf':
        return False
    try:
        float(string)
        return True
    except ValueError:
        return False

test_report_df = pd.read_excel('datalog_file.xlsx', sheetname=1)
test_report_df = test_report_df.drop(test_report_df.columns[[0,1,3,4]], axis=1)
# test_report_df.set_index('Test#')
print(test_report_df.head())

datalog_df = pd.read_excel('datalog_file.xlsx', sheetname=0)
datalog_df = datalog_df.drop(datalog_df.columns[[2,3,6,8]], axis=1)

test_dict = {}
bin_dict = {}
for test in set(datalog_df['Test#']):
    temp_df = datalog_df[datalog_df['Test#']==test]
    temp_rp = test_report_df[test_report_df['Test#']==test]

    if all(map(isfloat, list(temp_df['Value']))) and all(map(isfloat,list(temp_rp['Sdev']))):
        test_dict[test]=list(map(float,list(temp_df['Value'])))
        bin_dict[test] = [el/10 for el in list(map(float,temp_rp['Sdev']))]

bins, hist_data, group_labels = [], [], []
for k in test_dict.keys():
    if bin_dict[k][0]!=0:
        bins.append(bin_dict[k][0])
        hist_data.append(test_dict[k])
        group_labels.append("Test# {}".format(k))

test_N, Cpk_list = [], []
for v, c in zip(test_report_df['Test#'], test_report_df['Cpk']):
    if isfloat(c) and not pd.isnull(c):
        test_N.append(v)
        Cpk_list.append(c)


# print(test_report_df[['Test#', 'Cpk']])
