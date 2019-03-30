import unittest
import csv
import datetime

from finances import finances

class TestMintCSVData(unittest.TestCase):
    example_data_header = "Date,Description,Original Description,Amount,Transaction Type,Category,Account Name,Labels,Notes\n"
    example_data_january = """1/15/2018,McDonald's,MCDONALD'S F00000,6.66,debit,Fast Food,testaccount,,
    1/15/2018,Potbelly Sandwich Works,POTBELLY #000,7.25,debit,Fast Food,testaccount,,
    1/17/2018,Pick 'n Save,PICK N SAVE #000,4.78,debit,Groceries,testaccount,,
    1/17/2018,Auto Mechanic,AUTO MECHANIC,194.44,debit,Service & Parts,testaccount,,
    1/18/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
    1/19/2018,Pick 'n Save,PICK N SAVE #000,16.62,debit,Groceries,testaccount,,
    1/22/2018,McDonald's,MCDONALD'S F00000,4.24,debit,Fast Food,testaccount,,
    1/22/2018,PetSmart,PETSMART # 0000 C_5995,30.98,debit,Pet Food & Supplies,testaccount,,
    1/22/2018,Pick 'n Save,PICK N SAVE #000,0.79,debit,Groceries,testaccount,,
    1/22/2018,Pick 'n Save,PICK N SAVE #000,12.09,debit,Groceries,testaccount,,
    1/22/2018,McDonald's,MCDONALD'S F00000,4.24,debit,Fast Food,testaccount,,
    1/22/2018,PetSmart,PETSMART # 0000 C_5995,30.98,debit,Pet Food & Supplies,testaccount,,
    1/22/2018,Pick 'n Save,PICK N SAVE #000,0.79,debit,Groceries,testaccount,,
    1/22/2018,Pick 'n Save,PICK N SAVE #000,12.09,debit,Groceries,testaccount,,
    1/23/2018,Pick 'n Save,PICK N SAVE #000,6.98,debit,Groceries,testaccount,,
    1/25/2018,Animal Hospital,ANIMAL HOSPITAL,403.7,debit,Business Services,testaccount,,
    1/25/2018,Automatic Received,AUTOMATIC PYMT RECEIVED C_0000,444.03,credit,Credit Card Payment,testaccount,,
    1/25/2018,Pick 'n Save,PICK N SAVE #000,22.09,debit,Groceries,testaccount,,
    1/29/2018,Car Insurance,CAR INS BILLING,115.41,debit,Auto Insurance,testaccount,,
    1/29/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
    1/29/2018,Pick 'n Save,PICK N SAVE #000,25.07,debit,Groceries,testaccount,,
    1/31/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,"""
    example_data_february = """2/2/2018,Pick 'n Save,PICK N SAVE #000,11.12,debit,Groceries,testaccount,,
    2/2/2018,Potbelly Sandwich Works,POTBELLY #000,10.98,debit,Fast Food,testaccount,,
    2/5/2018,Mexican Rest,MEXICAN REST,8.12,debit,Restaurants,testaccount,,
    2/5/2018,Kwik Trip,KWIK TRIP  00000000000,32.68,debit,Gas & Fuel,testaccount,,
    2/5/2018,Some Bar,Some Bar,8,debit,Alcohol & Bars,testaccount,,
    2/5/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
    2/6/2018,Pick 'n Save,PICK N SAVE #000,7.28,debit,Groceries,testaccount,,
    2/8/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
    2/8/2018,Pick 'n Save,PICK N SAVE #000,26.24,debit,Groceries,testaccount,,
    2/12/2018,Ale House,ALE HOUSE,15.19,debit,Restaurants,testaccount,,
    2/12/2018,Save More Food,SAVE MORE FOOD MARKE,89.56,debit,Groceries,testaccount,,
    2/12/2018,BP,BP#000000,16.57,debit,Gas & Fuel,testaccount,,
    2/12/2018,The Store 55,THE STORE 55,24.27,debit,Gas & Fuel,testaccount,,
    2/12/2018,Pick 'n Save,PICK N SAVE #000,2.79,debit,Groceries,testaccount,,
    2/12/2018,Arby's,ARBYS,8.18,debit,Fast Food,testaccount,,
    2/14/2018,BP,BP#000000,19.44,debit,Gas & Fuel,testaccount,,
    2/15/2018,Pick 'n Save,PICK N SAVE #000,2.79,debit,Groceries,testaccount,,
    2/16/2018,Chick-Fil-A,CHICK-FIL-A #00000,4.57,debit,Fast Food,testaccount,,
    2/19/2018,Pick 'n Save,PICK N SAVE #000,33.9,debit,Groceries,testaccount,,
    2/19/2018,Pick 'n Save,PICK N SAVE #000,2.79,debit,Groceries,testaccount,,
    2/21/2018,Pick 'n Save,PICK N SAVE #000,6.38,debit,Groceries,testaccount,,
    2/21/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
    2/22/2018,McDonald's,MCDONALD'S F00000,4.66,debit,Fast Food,testaccount,,
    2/23/2018,Kwik Trip,KWIK TRIP  00000000000,30.08,debit,Gas & Fuel,testaccount,,
    2/23/2018,Pick 'n Save,PICK N SAVE #000,33.64,debit,Groceries,testaccount,,
    2/23/2018,Automatic Received,AUTOMATIC PYMT RECEIVED C_0000,953.07,credit,Credit Card Payment,testaccount,,
    2/26/2018,AMC,AMC #0000,5.38,debit,Movies & DVDs,testaccount,,
    2/27/2018,Car Insurance,CAR INS BILLING,115.41,debit,Auto Insurance,testaccount,,
    2/27/2018,Pick 'n Save,PICK N SAVE #000,22.68,debit,Groceries,testaccount,,
    2/27/2018,Potbelly Sandwich Works,POTBELLY #000,10.98,debit,Fast Food,testaccount,,"""
    example_data_november = """11/2/2018,Pick 'n Save,PICK N SAVE #000,5.89,debit,Groceries,testaccount,,
    11/2/2018,Pick 'n Save,PICK N SAVE #000,3.96,debit,Groceries,testaccount,,
    11/3/2018,Starbucks,STARBUCKS STORE 00000,15.01,debit,Fast Food,testaccount,,
    11/4/2018,Pick 'n Save,PICK N SAVE #000,25.61,debit,Groceries,testaccount,,
    11/5/2018,Whole Foods,WHOLEFDS #00000,16.58,debit,Groceries,testaccount,,
    11/7/2018,Pick 'n Save,PCK N SAVE #000,22.61,debit,Alcohol & Bars,testaccount,,
    11/7/2018,McDonald's,MCDONALD'S F00000,6.89,debit,Fast Food,testaccount,,
    11/8/2018,Chick-Fil-A,CHICK-FIL-A #00000,4.82,debit,Fast Food,testaccount,,
    11/10/2018,Starbucks,STARBUCKS STORE 00000,5.73,debit,Fast Food,testaccount,,
    11/11/2018,Starbucks,STARBUCKS STORE 00000,6.74,debit,Fast Food,testaccount,,
    11/11/2018,Pick 'n Save,PICK N SAVE #000,38.16,debit,Groceries,testaccount,,
    11/13/2018,PetSmart,PETSMART # 0000,8.39,debit,Pet Food & Supplies,testaccount,,
    11/14/2018,Health Insurance,HEALTH INSURANCE,480,debit,Business Services,testaccount,,
    11/14/2018,Pick 'n Save,PICK N SAVE #000,3.58,debit,Groceries,testaccount,,
    11/15/2018,Chick-Fil-A,CHICK-FIL-A #00000,3.46,debit,Fast Food,testaccount,,
    11/15/2018,Whole Foods,WHOLEFDS #00000,38.27,debit,Groceries,testaccount,,
    11/16/2018,Kwik Trip,KWIK TRIP  00000000000,32.76,debit,Gas & Fuel,testaccount,,
    11/17/2018,Pick 'n Save,PICK N SAVE #000,16,debit,Gas & Fuel,testaccount,,
    11/18/2018,Pick 'n Save,PICK N SAVE #000,22.86,debit,Groceries,testaccount,,
    11/19/2018,Pick 'n Save,PICK N SAVE #000,8.04,debit,Groceries,testaccount,,
    11/21/2018,Pick 'n Save,PCK N SAVE #000,18.49,debit,Alcohol & Bars,testaccount,,
    11/21/2018,Starbucks,STARBUCKS STORE 00000,83.87,debit,Restaurants,testaccount,,
    11/21/2018,Pick 'n Save,PICK N SAVE #000,78.36,debit,Alcohol & Bars,testaccount,,
    11/23/2018,Pick 'n Save,PICK N SAVE #000,34.31,debit,Groceries,testaccount,,
    11/23/2018,Automatic Received,AUTOMATIC PYMT RECEIVED,1692.6,credit,Credit Card Payment,testaccount,,
    11/26/2018,Car Insurance,CAR INS BILLING,121.05,debit,Auto Insurance,testaccount,,
    11/27/2018,Whole Foods,WHOLEFDS #00000,24.3,debit,Groceries,testaccount,,
    11/27/2018,Kwik Trip,KWIK TRIP  00000000000,30.15,debit,Gas & Fuel,testaccount,,
    11/27/2018,Pick 'n Save,PICK N SAVE #000,3.58,debit,Groceries,testaccount,,
    11/29/2018,Potbelly Sandwich Works,POTBELLY #000,7.36,debit,Fast Food,testaccount,,"""
    example_data_year_2018 = example_data_header + example_data_january + example_data_february + example_data_november

    def test_calc_weekly_totals_for_single_category(self):
        example_data = self.example_data_header + self.example_data_november
        data = csv.DictReader(example_data.splitlines())
        entries = finances.mint_dot_com_find_all_dict_reader(data, ['Fast Food'])
        weekly_totals = finances.calc_weekly_totals(entries, 2018, 11)
        self.assertAlmostEqual(weekly_totals[0], 15.01, places=2)
        self.assertAlmostEqual(weekly_totals[1], 24.18, places=2)
        self.assertAlmostEqual(weekly_totals[2], 3.46, places=2)
        self.assertAlmostEqual(weekly_totals[3], 0.0, places=2)
        self.assertAlmostEqual(weekly_totals[4], 7.36, places=2)
        self.assertAlmostEqual(weekly_totals[5], 0.0, places=2)

    def test_calc_weekly_totals_for_multiple_categories(self):
        example_data = self.example_data_header + self.example_data_november
        data = csv.DictReader(example_data.splitlines())
        entries = finances.mint_dot_com_find_all_dict_reader(data, ['Fast Food', 'Groceries'])
        weekly_totals = finances.calc_weekly_totals(entries, 2018, 11)
        self.assertAlmostEqual(weekly_totals[0], 50.47, places=2)
        self.assertAlmostEqual(weekly_totals[1], 78.92, places=2)
        self.assertAlmostEqual(weekly_totals[2], 68.17, places=2)
        self.assertAlmostEqual(weekly_totals[3], 42.35, places=2)
        self.assertAlmostEqual(weekly_totals[4], 35.24, places=2)
        self.assertAlmostEqual(weekly_totals[5], 0.0, places=2)

    def test_list_categories_with_no_filter(self):
        expected_categories = [
            'Alcohol & Bars',
            'Auto Insurance',
            'Business Services',
            'Credit Card Payment',
            'Fast Food',
            'Gas & Fuel',
            'Groceries',
            'Movies & DVDs',
            'Pet Food & Supplies',
            'Restaurants',
            'Service & Parts'
        ]
        data = csv.DictReader(self.example_data_year_2018.splitlines())
        actual_categories = finances.mint_dot_com_list_categories_dict_reader(data)
        self.assertListEqual(actual_categories, expected_categories)

    def test_find_all_with_filter_between_2018_02_15_and_2018_02_26(self):
        range_data = self.example_data_header + """2/15/2018,Pick 'n Save,PICK N SAVE #000,2.79,debit,Groceries,testaccount,,
        2/16/2018,Chick-Fil-A,CHICK-FIL-A #00000,4.57,debit,Fast Food,testaccount,,
        2/19/2018,Pick 'n Save,PICK N SAVE #000,33.9,debit,Groceries,testaccount,,
        2/19/2018,Pick 'n Save,PICK N SAVE #000,2.79,debit,Groceries,testaccount,,
        2/21/2018,Pick 'n Save,PICK N SAVE #000,6.38,debit,Groceries,testaccount,,
        2/21/2018,Chick-Fil-A,CHICK-FIL-A #00000,7.82,debit,Fast Food,testaccount,,
        2/22/2018,McDonald's,MCDONALD'S F00000,4.66,debit,Fast Food,testaccount,,
        2/23/2018,Kwik Trip,KWIK TRIP  00000000000,30.08,debit,Gas & Fuel,testaccount,,
        2/23/2018,Pick 'n Save,PICK N SAVE #000,33.64,debit,Groceries,testaccount,,
        2/23/2018,Automatic Received,AUTOMATIC PYMT RECEIVED C_0000,953.07,credit,Credit Card Payment,testaccount,,
        2/26/2018,AMC,AMC #0000,5.38,debit,Movies & DVDs,testaccount,,"""
        expected_data = csv.DictReader(range_data.splitlines())
        data = csv.DictReader(self.example_data_year_2018.splitlines())
        expected_entries = finances.mint_dot_com_find_all_dict_reader(expected_data)
        actual_entries = finances.mint_dot_com_find_all_dict_reader(data, start_date=datetime.date(2018, 2, 15), end_date=datetime.date(2018, 2, 26))
        self.assertListEqual(actual_entries, expected_entries)

if __name__ == '__main__':
    unittest.main()
