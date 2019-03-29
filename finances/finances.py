"""
Analyze finances.

Usage:
  finances.py cal [--categories=<categories>] [--year=<year>] [--month=<month>] <csv>
  finances.py categories [--year=<year>] [--month=<month>] <csv>

Options:
  -h --help                    Print this menu.
  --categories <categories>    The categories to filter by.
  --year <year>                The year to filter by. [default: 2018]
  --month <month>              The month to filter by. [default: 11]
"""

import docopt
import calendar
import csv
import datetime
import re

def calc_weekly_totals(entries, year, month):
    cal_text = calendar.TextCalendar().formatmonth(year, month)
    cal_array = cal_text.split('\n')
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
                        weekly_total += float(entry['Amount'])
        if index > 1: # Skip the Month and Weekday lines
            weekly_totals.append(weekly_total)
    return weekly_totals

def print_calendar_weekly_totals(entries, year, month):
    cal_text = calendar.TextCalendar().formatmonth(int(year), int(month))
    cal_array = cal_text.split('\n')
    weekly_totals = calc_weekly_totals(entries, int(year), int(month))
    monthly_total = sum(weekly_totals)
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

def mint_dot_com_find_all(csvpath, categories=None):
    rows = []
    with open(csvpath) as csvfile:
        r = csv.DictReader(csvfile)
        rows = mint_dot_com_find_all_dict_reader(r, categories)
    return rows

def mint_dot_com_list_categories_dict_reader(reader):
    categories = set()
    for row in reader:
        if row['Category']:
            categories.add(row['Category'])
    return sorted(list(categories))

def mint_dot_com_find_all_dict_reader(reader, categories=None):
    def clean_mint_csv_row(row):
        row_date = re.split('\\/', row['Date'])
        # Mint exports dates formatted as Month/Day/Year
        date_obj = datetime.date(int(row_date[2]), int(row_date[0]), int(row_date[1]))
        row['Date'] = date_obj.strftime('%Y/%m/%d')
        return row
    rows = []
    for row in reader:
        if isinstance(categories, list):
            for category in categories:
                if row['Category'] == category:
                    cleaned_row = clean_mint_csv_row(row)
                    rows.append(cleaned_row)
        else:
            if categories is None or row['Category'] == categories:
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

    if args['cal']:
        entries = mint_dot_com_find_all(args['<csv>'], args['--categories'].split(','))
        print_calendar_weekly_totals(entries, args['--year'], args['--month'])
    if args['categories']:
        entries = mint_dot_com_find_all(args['<csv>'])
        categories = mint_dot_com_list_categories_dict_reader(entries)
        for category in categories:
            print(category)

if __name__ == '__main__':
    main()
