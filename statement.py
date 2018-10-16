#!/bin/python
import fileinput
from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

dates = ''
for line in fileinput.input():
  dates += line
startDate = dates.split('\n')[0]
endDate = dates.split('\n')[1]
startDateSplit = startDate.split('/')
endDateSplit = endDate.split('/')
startDate = date(int(startDateSplit[2]), int(startDateSplit[1]),
  int(startDateSplit[0]))
endDate = date(int(endDateSplit[2]), int(endDateSplit[1]), int(endDateSplit[0]))
weeks = diff_dates(startDate, endDate) / 7.0
print(f'{weeks:.2f}')
