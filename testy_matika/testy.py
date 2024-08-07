import unittest
from Number import Number


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.number1 = Number(0)
        self.number2 = Number(1)
        self.number3 = Number(20)
        self.number4 = Number(250)
        self.number5 = Number(-51)

    def tearDown(self):
        pass

    def test_octal(self):
        self.assertEqual(self.number1.to_octal(), '0')
        self.assertEqual(self.number2.to_octal(), '1')
        self.assertEqual(self.number3.to_octal(), '24')
        self.assertEqual(self.number4.to_octal(), '372')
        self.assertEqual(self.number5.to_octal(), '-63')

    def test_binary(self):
        self.assertEqual(self.number1.to_bin(), '0')
        self.assertEqual(self.number2.to_bin(), '1')
        self.assertEqual(self.number3.to_bin(), '10100')
        self.assertEqual(self.number4.to_bin(), '11111010')
        self.assertEqual(self.number5.to_bin(), '-110011')

    def test_hexadecimal(self):
        self.assertEqual(self.number1.to_hexadecimal(), '0')
        self.assertEqual(self.number2.to_hexadecimal(), '1')
        self.assertEqual(self.number3.to_hexadecimal(), '14')
        self.assertEqual(self.number4.to_hexadecimal(), 'FA')
        self.assertEqual(self.number5.to_hexadecimal(), '-33')

#if __name__ == '__testy__':
#    unittest.main()
