import unittest
from test import cal
# all entries within <> are placeholders


def add(a,b):
    return int(a) + int(b)


def cal(a,b,opp):
    a = int(a)
    b = int(b)
    d = opp

    if d == '*':
        return (a * b)
    if d == '+':
        return (a + b)
    if d == '/':
        return (a / b)
    if d == '-':
        return (a / b)



class TestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,cal(1, 2,'+'))
        self.assertEqual(1, cal(2, 1, '-'))
        self.assertEqual(.5, cal(1, 2, '/'))


if __name__=='__main__':
    unittest.main()

