
import unittest

def is_leap_year(year):

    if year%4==0 and year%100!= 0 or year%400==0:
        return True
    else:
        return False
    

def check_year(y):

    if y > 0 and y < 10000:
        return True
    else:
        return False
    

def check_month(m):

    if  m > 0 and m < 13:      
        return True
        
    else:
        return False
    

def check_day(d, m, y):

    if m in long_months and d > 0 and d < 32:
        return True
    elif m in short_months and d > 0 and d < 31:
        return True
    elif m == feb:
        if is_leap_year(y) == True and d > 0 and d < 30:
            return True
        if is_leap_year(y) == False and d > 0 and d < 29:
            return True
        else:
            return False

    else:
        return False



date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
d, m, y = (int(i) for i in date)
long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
feb = 2



class TestTaskForTesting(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2024), True)

    def test_month(self):
        self.assertFalse(check_month(13), False)

    def test_year(self):
        self.assertEqual(check_year(10000), False)

    def test_day(self):
        self.assertTrue(check_day(31, 1, 2023), True)
        


if __name__ == "__main__":
    unittest.main(verbosity=4)
        
        
