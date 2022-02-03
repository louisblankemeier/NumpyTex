import numpy as np
import sys
sys.path.append('../src')
from two_axis_table import gen_two_axis_table

vals = np.array([[0.6 , -0.2, 0.1], [0.4, -0.5, -0.9], [0.6, 0.9, -0.2]])
col_labels = ['HTN', 'DM', 'OP']
row_labels = ['HTN', 'DM', 'OP']
col_axis_label = 'Relative Performance On'
row_axis_label = 'Trained With'
table_name = "two_axis_example"

gen_two_axis_table(table_name, col_labels, row_labels, col_axis_label, row_axis_label, vals)