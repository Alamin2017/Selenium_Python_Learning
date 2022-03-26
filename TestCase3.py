import unittest
class Apptesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is Login Test")
    @classmethod
    def tearDown(self):
        print("This is Logout Test")

    def test_search(self):
        print("This is search test")

    def test_Advancedsearch(self):
        print("This is Advancedsearch test")

    def test_PrepaidRecharge(self):
        print("This is PrepaidRecharge test")

    def test_PostpaidRecharge(self):
        print("This is PostpaidRecharge test")


if __name__ == "__main__":
    unittest.main()
