import unittest

class TestFiles(unittest.TestCase):
    def test_read_cities1(self):
        file="1.1.csv"
        self.assertFalse(file)
    def test_read_cities2(self):
        file="1.2.csv"
        self.assertFalse(file)
    def test_read_cities3(self):
        file="1.3.csv"
        self.assertFalse(file)
    def test_read_cities4(self):
        file="1.4.csv"
        self.assertFalse(file)
    def test_read_cities_path(self):
        file="123456.csv"
        self.assertFalse(file)
    def test_read_cities(self):
        file="1.csv"
        self.assertTrue(file)
    def test_read_prod1(self):
        file="2.1.csv"
        self.assertFalse(file)
    def test_read_prod2(self):
        file="2.2.csv"
        self.assertFalse(file)
    def test_read_prod3(self):
        file="2.3.csv"
        self.assertFalse(file)
    def test_read_prod4(self):
        file="2.4.csv"
        self.assertFalse(file)
    def test_read_prod_path(self):
        file="123456.csv"
        self.assertFalse(file)
    def test_read_prod(self):
        file="2.csv"
        self.assertTrue(file)
    def test_read_worker_time1(self):
        file="3.1.csv"
        self.assertFalse(file)
    def test_read_worker_time2(self):
        file="3.2.csv"
        self.assertFalse(file)
    def test_read_worker_time3(self):
        file="3.3.csv"
        self.assertFalse(file)
    def test_read_worker_time_path(self):
        file="123456.csv"
        self.assertFalse(file)
    def test_read_worker_time(self):
        file="3.csv"
        self.assertTrue(file)
    def test_read_solution1(self):
        file="4.1.csv"
        self.assertFalse(file)
    def test_read_solution2(self):
        file="4.2.csv"
        self.assertFalse(file)
    def test_read_solution3(self):
        file="4.3.csv"
        self.assertFalse(file)
    def test_read_solution_path(self):
        file="123456.csv"
        self.assertFalse(file)
    def test_read_solution(self):
        file="4.csv"
        self.assertTrue(file)
        
    
if __name__ == '__main__':
    unittest.main()