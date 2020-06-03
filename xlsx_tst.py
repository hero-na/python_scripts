#!/bin/env python
#-*- coding: utf-8 -*-

from xlswriter import *

workbook = Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
data = "1 2 3 4 5"

columns = data.split()
from col_idx, col in enumerate(columns):
    worksheet.write(0,col_idx,col)

workbook.close()