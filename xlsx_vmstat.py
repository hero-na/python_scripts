#!/bin/env python
#-*- coding: utf-8 -*-

from xlsxWriter import *
from subprocess import *

cmd "vmstat 1 5 | awk {now=strftime(\"%Y-%m-%d %T \"); print now $0}"
p = Popen(cmd, shell=True, stdout= PIPE)
(ret,err) = p.communicate()

workbook = Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()
drows = ret.split("\n")

for row_idx, row in enumerate(rows):
    columns = row.split()
    for col_idx, col in enumerate(columns):
        worksheet.write(row_idx,col_idx,col)

workbook.close()