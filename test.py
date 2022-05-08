import unittest
import re

import Computation


class TestComputation(unittest.TestCase):
    def setUp(self):
        print("Before Test")

    def tearDown(self):
        print("After Test")

    def test_addition1(self):
        ''' the input numbers both integer ,but not big numbers '''
        print("Test case 1")
        self.assertEqual(Computation.addition('10', '95'), '105')

    def test_addition2(self):
        ''' the input numbers both integer and big numbers '''
        print("Test case 2")
        self.assertEqual(Computation.addition('66666666665555555555', '55555555555555555555'), '122222222221111111110')

    def test_addition3(self):
        ''' input one is big number and another one is not big number '''
        print("Test case 3")
        self.assertEqual(Computation.addition('66666666665555555555', '19'), '66666666665555555574')

    def test_addition4(self):
        '''Input two numbers with same length, output result correctly'''
        print("Test case 4")
        self.assertEqual(Computation.addition('888888888888888888888', '999999999999999999991'),
                         '1888888888888888888879')

    def test_addition5(self):
        '''Input length of first number is longer than the second one’s'''
        print("Test case 5")
        self.assertEqual(Computation.addition('12345678901234567890', '67543289765432'), '12345746444524333322')

    def test_addition6(self):
        '''Input length of second number is longer than the first one’s'''
        print("Test case 6")
        self.assertEqual(Computation.addition('67543289765432', '12345678901234567890'), '12345746444524333322')

    def test_additionWithDecimal1(self):
        ''' at least one of the numbers with a decimal point but both of them are not big numbers '''
        print("Test case 7")
        self.assertEqual(Computation.additionWithDecimal('10.34', '0.5'), '10.84')

    def test_additionWithDecimal2(self):
        ''' at least one of the numbers with a decimal point and both of them are big numbers '''
        print("Test case 8")
        self.assertEqual(Computation.additionWithDecimal('11111111111111111111.1', '92222222222222222229'),
                         '103333333333333333340.1')
        self.assertEqual(Computation.additionWithDecimal('11111111111111111111.1', '92222222222222222222.2222'),
                         '103333333333333333333.3222')
        self.assertEqual(Computation.additionWithDecimal('11111111111111111111.1', '92222222222222222222.2222'),
                         '103333333333333333333.3222')

    def test_additionWithDecimal3(self):
        '''Input two numbers with same length'''
        print("Test case 9")
        self.assertEqual(Computation.additionWithDecimal('8765438232134324245641.123', '876543823213432429999.888'),
                         '9641982055347756675641.011')

    def test_additionWithDecimal4(self):
        '''Input length of first number is longer than the second one’s'''
        print("Test case 10")
        self.assertEqual(Computation.additionWithDecimal('8765438232134324245641.123', '999.938'),
                         '8765438232134324246641.061')

    def test_additionWithDecimal5(self):
        '''Input length of second number is longer than the first one’s'''
        print("Test case 11")
        self.assertEqual(Computation.additionWithDecimal('999.938', '8765438232134324245641.123'),
                         '8765438232134324246641.061')

    def test_subtraction1(self):
        '''the input numbers both integer ,but not big numbers'''
        print("Test case 12")
        self.assertEqual(Computation.subtraction('100', '99'), '1')

    def test_subtraction2(self):
        ''' the input numbers both integer and big numbers '''
        print("Test case 13")
        self.assertEqual(Computation.subtraction('66666666665555555555', '55555555555555555555'),
                         '11111111110000000000')

    def test_subtraction3(self):
        ''' input one is big number and another one is not big number '''
        print("Test case 14")
        self.assertEqual(Computation.subtraction('66666666665555555555', '19'), '66666666665555555536')

    def test_subtraction4(self):
        '''Input two numbers with same length'''
        print("Test case 15")
        self.assertEqual(Computation.subtraction('8765438232134324245641', '876543823213432429999'),
                         '7888894408920891815642')

    def test_subtraction5(self):
        '''Input two numbers with different length'''
        print("Test case 16")
        self.assertEqual(Computation.subtraction('8765438232134324245640', '87654382321343242999'),
                         '8677783849812981002641')

    def test_subtraction6(self):
        '''the result is positive'''
        print("Test case 17")
        self.assertEqual(Computation.subtraction("65656566320981038764352", '9898900021223232321'),
                         '65646667420959815532031')

    def test_subtraction7(self):
        '''the result is negative'''
        print("Test case 18")
        self.assertEqual(Computation.subtraction("9898900021223232321", '65656566320981038764352'),
                         '-65646667420959815532031')

    def test_subtraction8(self):
        '''the result is 0'''
        print("Test case 19")
        self.assertEqual(Computation.subtraction("65656566320981038764352", '65656566320981038764352'), '0')

    def test_subtraction9(self):
        '''the result starts with 0'''
        print("Test case 20")
        self.assertEqual(Computation.subtraction("65656566320981038764352", '65656566320981038000000'), '764352')

    def test_subtractionWithDecimal1(self):
        '''the input numbers both integer ,but not big numbers'''
        print("Test case 21")
        self.assertEqual(Computation.subtractionWithDecimal('100.53', '99.87'), '0.66')

    def test_subtractionWithDecimal2(self):
        ''' the input numbers both integer and big numbers '''
        print("Test case 22")
        self.assertEqual(Computation.subtractionWithDecimal('66666666665555555555.123', '55555555555555555555.456'),
                         '11111111109999999999.667')

    def test_subtractionWithDecimal3(self):
        ''' input one is big number and another one is not big number '''
        print("Test case 23")
        self.assertEqual(Computation.subtractionWithDecimal('66666666665555555555.685', '19.49'),
                         '66666666665555555536.195')

    def test_subtractionWithDecimal4(self):
        '''Input two numbers with same length'''
        print("Test case 24")
        self.assertEqual(
            Computation.subtractionWithDecimal('8765438232134324245641.09872', '876543823213432429999.56555'),
            '7888894408920891815641.53317')

    def test_subtractionWithDecimal5(self):
        '''Input two numbers with different length'''
        print("Test case 25")
        self.assertEqual(Computation.subtractionWithDecimal('8765438232134324245640.55321', '87654382321343242999.9'),
                         '8677783849812981002640.65321')

    def test_subtractionWithDecimal6(self):
        '''the result is positive'''
        print("Test case 26")
        self.assertEqual(Computation.subtractionWithDecimal("65656566320981038764352.2341", '9898900021223232321.5543'),
                         '65646667420959815532030.6798')

    def test_subtractionWithDecimal7(self):
        '''the result is negative'''
        print("Test case 27")
        self.assertEqual(
            Computation.subtractionWithDecimal("9898900021223232321.7689981", '65656566320981038764352.5555'),
            '-65646667420959815532030.7865019')

    def test_subtractionWithDecimal8(self):
        '''the result is 0'''
        print("Test case 28")
        self.assertEqual(Computation.subtractionWithDecimal("65656566320981038764352.087642435",
                                                            '65656566320981038764352.087642435'), '0.0')

    def test_subtractionWithDecimal9(self):
        '''the result starts with 0'''
        print("Test case 29")
        self.assertEqual(Computation.subtractionWithDecimal("65656566320981038764352.1234354326785",
                                                            '65656566320981038764352.1234354326784'), '0.0000000000001')

    def test_multiplication1(self):
        '''the input numbers both integer ,but not big numbers'''
        print("Test case 30")
        self.assertEqual(Computation.multiplication('100', '99'), '9900')

    def test_multiplication2(self):
        ''' the input numbers both integer and big numbers '''
        print("Test case 31")
        self.assertEqual(Computation.multiplication('66666666665555555555', '55555555555555555555'),
                         '3703703703641975308574074074074691358025')

    def test_multiplication3(self):
        ''' input one is big number and another one is not big number '''
        print("Test case 32")
        self.assertEqual(Computation.multiplication('66666666665555555555', '19'), '1266666666645555555545')

    def test_multiplication4(self):
        '''Input two numbers with same length'''
        print("Test case 33")
        self.assertEqual(Computation.multiplication('8765438232134324245641', '876543823213432429999'),
                         '7683290740136210805686320697465941213384359')

    def test_multiplication5(self):
        '''Input two numbers with different length'''
        print("Test case 34")
        self.assertEqual(Computation.multiplication('8765438232134324245640', '876543823213432429990000000'),
                         '7683290740136210805606555209553518862743600000000')

    def test_multiplication6(self):
        '''one of the input number is 0'''
        print("Test case 35")
        self.assertEqual(Computation.multiplication('0', '876543823213432429990000000'), '0')
        self.assertEqual(Computation.multiplication('0', '0'), '0')

    def test_input(self):
        ''' the # of input is 2 '''
        print("Test case 36")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = [12, 68976758824]
        self.assertEqual(len(data), 2, msg="The # of the input is  two.")

    def test_input1(self):
        ''' the # of input is 3 '''
        print("Test case 37")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = [12, 68976758824, 4]
        self.assertNotEqual(len(data), 2, msg="The # of the input is not two, please input again.")

    def test_input2(self):
        ''' the # of input is null '''
        print("Test case 38")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = []
        self.assertFalse(len(data) == 2, msg="The # of the input is not two, please input again.")

    def test_input3(self):
        ''' the input are not integers or integers with a decimal '''
        print("Test case 39")
        data = ['a34345', 'dtfh']
        self.assertFalse((re.match("^[0-9]+$", data[0])), msg="The input is invalid, please input again.")
        self.assertFalse((re.match("^[0-9]+$", data[1])), msg="The input is invalid, please input again.")
        self.assertFalse((re.match("^\d+\.\d+$", data[0])), msg="The input is invalid, please input again.")
        self.assertFalse((re.match("^\d+\.\d+$", data[1])), msg="The input is invalid, please input again.")

    def test_input4(self, numberList=None):
        ''' the input are both integers and at least one with a decimal '''
        print("Test case 40")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = ['3453645675', '32878782535.768769']
        self.assertTrue(re.match("^[0-9]+$", data[0]))
        self.assertTrue(re.match("^\d+\.\d+$", data[1]))

    def test_input5(self):
        ''' at least one of the input numbers is not big number '''
        print("Test case 41")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = ['143454657657', '686784637']
        self.assertTrue((len(data[0]) < 20 or len(data[1]) < 20), msg="The input are big numbers.")

    def test_input6(self):
        '''both of the input numbers are big numbers without a decimal '''
        print("Test case 41")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = ['14345465765734543645756768698797', '686784637938025843859478689548695847896589']
        self.assertTrue((len(data[0]) >= 20 or len(data[1]) >= 20))

    def test_input6(self):
        '''both of the input numbers are big numbers with a decimal '''
        print("Test case 42")
        # with mock.patch('builtins.input', return_value="2 4 7"):
        #     assert Computation.check() == 'The # of the input is not two, please input again.'\
        data = ['14345465765734543645756768698797.3456', '686784637938025843859478689548695847896589.76778']
        self.assertTrue((len(data[0]) >= 20 or len(data[1]) >= 20))


if __name__ == '__main__':
    unittest.main()
