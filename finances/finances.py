"""
Analyze finances.

Usage:
  finances.py cal [--categories=<categories>] [--year=<year>] [--month=<month>] [--columns=<columns>] <csv>
  finances.py categories [--year=<year>] [--month=<month>] <csv>

Options:
  -h --help                    Print this menu.
  --categories <categories>    The categories to filter by.
  --year <year>                The year or comma-separated list of years to filter by. [default: 0]
  --month <month>              The month or comma-separated list of months to filter by. [default: 0]
  --columns <columns>          The number of columns to print per row. [default: 3]
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

def text_calendar_weekly_totals(entries, year, month):
    cal_text = calendar.TextCalendar().formatmonth(int(year), int(month))
    cal_array = cal_text.split('\n')
    weekly_totals = calc_weekly_totals(entries, int(year), int(month))
    monthly_total = sum(weekly_totals)
    highest = max(weekly_totals + [monthly_total])
    highest_len = len('{0:.2f}'.format(highest)) + 2 # Add 2 for the parentheses.
    cal_array[0] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[0], '({0:.2f})'.format(monthly_total))
    cal_array[1] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[1], '')
    cal_array[2] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[2], '({0:.2f})'.format(weekly_totals[0]))
    cal_array[3] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[3], '({0:.2f})'.format(weekly_totals[1]))
    cal_array[4] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[4], '({0:.2f})'.format(weekly_totals[2]))
    cal_array[5] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[5], '({0:.2f})'.format(weekly_totals[3]))
    cal_array[6] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[6], '({0:.2f})'.format(weekly_totals[4]))
    cal_array[7] = ('{0: <20}  {1: >' + str(highest_len) + '}').format(cal_array[7], '({0:.2f})'.format(weekly_totals[5]))
    cal_text = '\n'.join(cal_array)
    return cal_text

def mint_dot_com_find_all(csvpath, categories=None, start_date=None, end_date=None):
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

def mint_dot_com_find_all_dict_reader(reader, categories=None, start_date=None, end_date=None):
    def clean_mint_csv_row(row):
        row_date = re.split('\\/', row['Date'])
        # Mint exports dates formatted as Month/Day/Year
        date_obj = datetime.date(int(row_date[2]), int(row_date[0]), int(row_date[1]))
        row['Date'] = date_obj.strftime('%Y/%m/%d')
        return row
    rows = []
    for row in reader:
        cleaned_row = clean_mint_csv_row(row)
        is_within_date_range = True
        date_parts = re.split('\\/', cleaned_row['Date'])
        the_date = datetime.date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))

        if start_date is not None and end_date is not None:
            is_within_date_range = the_date >= start_date and the_date <= end_date
        elif start_date is not None:
            is_within_date_range = the_date >= start_date
        elif end_date is not None:
            is_within_date_range = the_date <= end_date

        if is_within_date_range:
            if isinstance(categories, list):
                for category in categories:
                    if row['Category'] == category:
                        rows.append(cleaned_row)
            else:
                if categories is None or row['Category'] == categories:
                    rows.append(cleaned_row)
    return rows

def mint_dot_com_list_years(entries):
    years = set()
    for entry in entries:
        if entry['Date']:
            date_parts = re.split('\\/', entry['Date'])
            years.add(date_parts[0])
    return sorted(list(years))

def calc_sum(entries):
    sum = 0.0
    for entry in entries:
        sum += float(entry['Amount'])
    return sum

def main():
    args = docopt.docopt(__doc__, help=True, version='v1.0')

    if args['cal']:
        categories = None
        if args['--categories']:
            args['--categories'].split(',')
        entries = mint_dot_com_find_all(args['<csv>'], categories)
        years = mint_dot_com_list_years(entries)
        if args['--year'] and args['--year'] != '0':
            years = args['--year'].split(',')
        months = list(range(1, 13))
        if args['--month'] and args['--month'] != '0':
            months = args['--month'].split(',')
        columns = int(args['--columns'])
        text_calendars = []
        for year in years:
            for month in months:
                text_calendars.append(text_calendar_weekly_totals(entries, year, month))
        row_text = ['' for _ in range(7)]
        i = 1
        for cal in text_calendars:
            cal_split = cal.split('\n')
            row_text[0] += '{0: <40}'.format(cal_split[0])
            row_text[1] += '{0: <40}'.format(cal_split[1])
            row_text[2] += '{0: <40}'.format(cal_split[2])
            row_text[3] += '{0: <40}'.format(cal_split[3])
            row_text[4] += '{0: <40}'.format(cal_split[4])
            row_text[5] += '{0: <40}'.format(cal_split[5])
            row_text[6] += '{0: <40}'.format(cal_split[6])
            if i % columns == 0:
                print(row_text[0])
                print(row_text[1])
                print(row_text[2])
                print(row_text[3])
                print(row_text[4])
                print(row_text[5])
                print(row_text[6])
                print()
                row_text = ['' for _ in range(7)]
            i += 1
        if row_text[0]:
            print(row_text[0])
            print(row_text[1])
            print(row_text[2])
            print(row_text[3])
            print(row_text[4])
            print(row_text[5])
            print(row_text[6])
    if args['categories']:
        entries = mint_dot_com_find_all(args['<csv>'])
        categories = mint_dot_com_list_categories_dict_reader(entries)
        for category in categories:
            print(category)

if __name__ == '__main__':
    main()
