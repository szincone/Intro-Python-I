"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
  - If the user doesn't specify any input, your program should
    print the calendar for the current month. The 'datetime'
    module may be helpful for this.
  - If the user specifies one argument, assume they passed in a
    month and render the calendar for that month of the current year.
  - If the user specifies two arguments, assume they passed in
    both the month and the year. Render the calendar for that
    month and year.
  - Otherwise, print a usage statement to the terminal indicating
    the format that your program expects arguments to be given.
    Then exit the program.
"""

import sys
import calendar
from datetime import datetime

year = datetime.now().year
month = datetime.now().month
cal = calendar.Calendar().itermonthdates(year, month)


def get_cal(month=month, year=year):
    months_dict = dict((v, k) for k, v in enumerate(calendar.month_abbr))
    user_input = input(
        "Enter: month [year] ").split()
    if len(user_input) > 2:
        print("Try input again..")
    elif len(user_input) == 2:
        [month, year] = [user_input[0][:3].lower(), int(user_input[1])]
        for x in months_dict:
            if type(x) != int:
                if x.lower() == month:
                    month = months_dict[x]
                    print(calendar.TextCalendar(
                        0).formatmonth(year, month))
    elif len(user_input) == 1:
        month = user_input[0][:3].lower()
        for x in months_dict:
            if type(x) != int:
                if x.lower() == month:
                    month = months_dict[x]
                    print(calendar.TextCalendar(
                        0).formatmonth(year, month))
    else:
        print(calendar.TextCalendar(0).formatmonth(year, month))


get_cal()
