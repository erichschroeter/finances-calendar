import unittest
import csv

from finances import finances

class TestMintCSVData(unittest.TestCase):
    example_month = """Date,Description,Original Description,Amount,Transaction Type,Category,Account Name,Labels,Notes\n
    11/2/2018,Pick 'n Save,PICK N SAVE #000,5.89,debit,Groceries,testaccount,,\n
    11/2/2018,Pick 'n Save,PICK N SAVE #000,3.96,debit,Groceries,testaccount,,\n
    11/3/2018,Starbucks,STARBUCKS STORE 00000,15.01,debit,Fast Food,testaccount,,\n
    11/4/2018,Pick 'n Save,PICK N SAVE #000,25.61,debit,Groceries,testaccount,,\n
    11/5/2018,Whole Foods,WHOLEFDS #00000,16.58,debit,Groceries,testaccount,,\n
    11/7/2018,Pick 'n Save,PCK N SAVE #000,22.61,debit,Alcohol & Bars,testaccount,,\n
    11/7/2018,McDonald's,MCDONALD'S F00000,6.89,debit,Fast Food,testaccount,,\n
    11/8/2018,Chick-Fil-A,CHICK-FIL-A #00000,4.82,debit,Fast Food,testaccount,,\n
    11/10/2018,Starbucks,STARBUCKS STORE 00000,5.73,debit,Fast Food,testaccount,,\n
    11/11/2018,Starbucks,STARBUCKS STORE 00000,6.74,debit,Fast Food,testaccount,,\n
    11/11/2018,Pick 'n Save,PICK N SAVE #000,38.16,debit,Groceries,testaccount,,\n
    11/13/2018,PetSmart,PETSMART # 0000,8.39,debit,Pet Food & Supplies,testaccount,,\n
    11/14/2018,Health Insurance,HEALTH INSURANCE,480,debit,Business Services,testaccount,,\n
    11/14/2018,Pick 'n Save,PICK N SAVE #000,3.58,debit,Groceries,testaccount,,\n
    11/15/2018,Chick-Fil-A,CHICK-FIL-A #00000,3.46,debit,Fast Food,testaccount,,\n
    11/15/2018,Whole Foods,WHOLEFDS #00000,38.27,debit,Groceries,testaccount,,\n
    11/16/2018,Kwik Trip,KWIK TRIP  00000000000,32.76,debit,Gas & Fuel,testaccount,,\n
    11/17/2018,Pick 'n Save,PICK N SAVE #000,16,debit,Gas & Fuel,testaccount,,\n
    11/18/2018,Pick 'n Save,PICK N SAVE #000,22.86,debit,Groceries,testaccount,,\n
    11/19/2018,Pick 'n Save,PICK N SAVE #000,8.04,debit,Groceries,testaccount,,\n
    11/21/2018,Pick 'n Save,PCK N SAVE #000,18.49,debit,Alcohol & Bars,testaccount,,\n
    11/21/2018,Starbucks,STARBUCKS STORE 00000,83.87,debit,Restaurants,testaccount,,\n
    11/21/2018,Pick 'n Save,PICK N SAVE #000,78.36,debit,Alcohol & Bars,testaccount,,\n
    11/23/2018,Pick 'n Save,PICK N SAVE #000,34.31,debit,Groceries,testaccount,,\n
    11/23/2018,Automatic Received,AUTOMATIC PYMT RECEIVED,1692.6,credit,Credit Card Payment,testaccount,,\n
    11/26/2018,Car Insurance,CAR INS BILLING,121.05,debit,Auto Insurance,testaccount,,\n
    11/27/2018,Whole Foods,WHOLEFDS #00000,24.3,debit,Groceries,testaccount,,\n
    11/27/2018,Kwik Trip,KWIK TRIP  00000000000,30.15,debit,Gas & Fuel,testaccount,,\n
    11/27/2018,Pick 'n Save,PICK N SAVE #000,3.58,debit,Groceries,testaccount,,\n
    11/29/2018,Potbelly Sandwich Works,POTBELLY #000,7.36,debit,Fast Food,testaccount,,"""

    def test_calc_weekly_totals_for_single_category(self):
        data = csv.DictReader(self.example_month.splitlines())
        entries = finances.mint_dot_com_find_all_dict_reader(data, ['Fast Food'])
        weekly_totals = finances.calc_weekly_totals(entries, 2018, 11)
        self.assertAlmostEqual(weekly_totals[0], 15.01, places=2)
        self.assertAlmostEqual(weekly_totals[1], 24.18, places=2)
        self.assertAlmostEqual(weekly_totals[2], 3.46, places=2)
        self.assertAlmostEqual(weekly_totals[3], 0.0, places=2)
        self.assertAlmostEqual(weekly_totals[4], 7.36, places=2)
        self.assertAlmostEqual(weekly_totals[5], 0.0, places=2)

    def test_calc_weekly_totals_for_multiple_categories(self):
        data = csv.DictReader(self.example_month.splitlines())
        entries = finances.mint_dot_com_find_all_dict_reader(data, ['Fast Food', 'Groceries'])
        weekly_totals = finances.calc_weekly_totals(entries, 2018, 11)
        self.assertAlmostEqual(weekly_totals[0], 50.47, places=2)
        self.assertAlmostEqual(weekly_totals[1], 78.92, places=2)
        self.assertAlmostEqual(weekly_totals[2], 68.17, places=2)
        self.assertAlmostEqual(weekly_totals[3], 42.35, places=2)
        self.assertAlmostEqual(weekly_totals[4], 35.24, places=2)
        self.assertAlmostEqual(weekly_totals[5], 0.0, places=2)

if __name__ == '__main__':
    unittest.main()
