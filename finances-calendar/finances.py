"""
Analyze finances.

Usage:
  finances.py ls [--categories=<categories>] <csv>

Options:
  -h --help                    Print this menu.
  --categories <categories>    The categories to filter by.
"""

import docopt
import calendar
import csv
import datetime
import re

# '   November 2018\nMo Tu We Th Fr Sa Su\n          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30\n'
def print_calendar_weekly_totals(entries, year, month):
    cal = calendar.calendar(year, month)
    # Find the first week day of the month
    # firstweekday = calendar.monthcalendar(year, month)[0].index(1)
    cal_text = calendar.TextCalendar().formatmonth(year, month)
    cal_array = cal_text.split('\n')
    monthly_total = 0.0
    weekly_totals = []
    for index, week_string in enumerate(cal_array):
        dates = re.findall(r'([0-9]+)', week_string)
        weekly_total = 0.0
        for date in dates:
            day = int(date)
            if day < 32:
                expected_date = '{0}/{1:02d}/{2:02d}'.format(year, month, day)
                for entry in entries:
                    if entry['Date'] == expected_date:
                        # print(entry['Amount'])
                        weekly_total += float(entry['Amount'])
        if index > 1: # and cal_array[index]:
            # Skip the Month and Weekday lines
            weekly_totals.append(weekly_total)
            monthly_total += weekly_total
    highest = max(weekly_totals + [monthly_total])
    highest_len = len('{0:.2f}'.format(highest)) + 2 # Add 2 for the parentheses.
    cal_array[0] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[0], '({0:.2f})'.format(monthly_total))
    cal_array[2] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[2], '({0:.2f})'.format(weekly_totals[0]))
    cal_array[3] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[3], '({0:.2f})'.format(weekly_totals[1]))
    cal_array[4] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[4], '({0:.2f})'.format(weekly_totals[2]))
    cal_array[5] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[5], '({0:.2f})'.format(weekly_totals[3]))
    cal_array[6] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[6], '({0:.2f})'.format(weekly_totals[4]))
    cal_array[7] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[7], '({0:.2f})'.format(weekly_totals[5]))
    cal_text = '\n'.join(cal_array)
    print(cal_text)

def find_all(csvpath, categories):
    def clean_mint_csv_row(row):
        row_date = re.split('\\/', row['Date'])
        # Mint exports dates formatted as Month/Day/Year
        date_obj = datetime.date(int(row_date[2]), int(row_date[0]), int(row_date[1]))
        row['Date'] = date_obj.strftime('%Y/%m/%d')
        return row
    rows = []
    with open(csvpath) as csvfile:
        r = csv.DictReader(csvfile)
        for row in r:
            if isinstance(categories, list):
                for category in categories:
                    if row['Category'] == category:
                        cleaned_row = clean_mint_csv_row(row)
                        rows.append(cleaned_row)
            else:
                if row['Category'] == categories:
                    cleaned_row = clean_mint_csv_row(row)
                    rows.append(cleaned_row)
    return rows

def calc_sum(entries):
    sum = 0.0
    for entry in entries:
        sum += float(entry['Amount'])
    return sum

def main():
    args = docopt.docopt(__doc__, help=True, version='v1.0')

    if args['ls']:
        entries = find_all(args['<csv>'], args['--categories'].split(','))
        print_calendar_weekly_totals(entries, 2018, 11)
        # print(len(entries))
        sum = calc_sum(entries)
        print('{0:.2f}'.format(sum))

if __name__ == '__main__':
    main()
