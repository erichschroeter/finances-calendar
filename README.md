The intent of this project is to provide answers to simple questions one may have about their financial data.

# Example

An example command to view your expenses on groceries and fast food in the year 2018 would be as follows:

    python finances/finances.py --categories "Groceries,Fast Food" --year 2018 my_data.csv

The command above would, for example, produce the following output:

        January 2018      (273.06)             February 2018      (666.62)               March 2018       (1212.00)
    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7    (0.00)                    1  2  3  4   (44.20)                    1  2  3  4    (69.24)
     8  9 10 11 12 13 14    (0.00)           5  6  7  8  9 10 11  (130.56)           5  6  7  8  9 10 11   (175.72)
    15 16 17 18 19 20 21   (99.26)          12 13 14 15 16 17 18  (246.16)          12 13 14 15 16 17 18   (144.18)
    22 23 24 25 26 27 28   (92.38)          19 20 21 22 23 24 25  (178.38)          19 20 21 22 23 24 25   (394.68)
    29 30 31               (81.42)          26 27 28               (67.32)          26 27 28 29 30 31      (428.18)
    
         April 2018       (463.40)                May 2018        (507.96)               June 2018        (555.28)
    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su
                       1    (0.00)              1  2  3  4  5  6   (64.81)                       1  2  3   (24.82)
     2  3  4  5  6  7  8  (132.14)           7  8  9 10 11 12 13   (97.48)           4  5  6  7  8  9 10  (379.58)
     9 10 11 12 13 14 15   (82.02)          14 15 16 17 18 19 20  (187.37)          11 12 13 14 15 16 17   (44.47)
    16 17 18 19 20 21 22  (101.91)          21 22 23 24 25 26 27  (147.82)          18 19 20 21 22 23 24   (48.80)
    23 24 25 26 27 28 29  (138.96)          28 29 30 31            (10.48)          25 26 27 28 29 30      (57.61)
    
         July 2018        (372.43)              August 2018       (280.80)             September 2018     (221.55)
    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su
                       1   (11.97)                 1  2  3  4  5   (34.93)                          1  2    (0.00)
     2  3  4  5  6  7  8  (166.98)           6  7  8  9 10 11 12   (69.93)           3  4  5  6  7  8  9   (67.82)
     9 10 11 12 13 14 15   (73.36)          13 14 15 16 17 18 19   (59.05)          10 11 12 13 14 15 16   (44.98)
    16 17 18 19 20 21 22   (41.89)          20 21 22 23 24 25 26   (56.73)          17 18 19 20 21 22 23   (84.53)
    23 24 25 26 27 28 29   (78.23)          27 28 29 30 31         (60.16)          24 25 26 27 28 29 30   (24.22)
    
        October 2018      (328.60)             November 2018      (478.48)             December 2018      (235.88)
    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su                    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7   (59.74)                    1  2  3  4   (50.47)                          1  2   (37.05)
     8  9 10 11 12 13 14   (88.02)           5  6  7  8  9 10 11  (101.53)           3  4  5  6  7  8  9   (47.11)
    15 16 17 18 19 20 21   (98.51)          12 13 14 15 16 17 18   (68.17)          10 11 12 13 14 15 16   (16.86)
    22 23 24 25 26 27 28   (48.40)          19 20 21 22 23 24 25  (223.07)          17 18 19 20 21 22 23   (27.80)
    29 30 31               (33.93)          26 27 28 29 30         (35.24)          24 25 26 27 28 29 30  (107.06)
