#!/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import xlsxwriter

cmd = "vmstat 1 5 | awk {now=strftime(\"%Y-%m-%d %T \"); print now $0}"
p = open(cmd, shell=True)
(ret,err) = p.communicate()

workbook = xlsxwriter.Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()
drows = ret.split("\n")

for row_idx, row in enumerate(rows):
    columns = row.split()
    for col_idx, col in enumerate(columns):
        worksheet.write(row_idx,col_idx,col)

workbook.close()