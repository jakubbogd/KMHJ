import unittest
from KMHJ-main.GUI import files
class TestFiles(unittest.TestCase):
    def test_read_cities_false_1(self):
        file="1.1.csv"
        self.assertFalse(files.read_cities(file))
    def test_read_cities_false_2(self):
        file="1.2.csv"
        self.assertFalse(files.read_cities(file))
    def test_read_cities_false_3(self):
        file="1.3.csv"
        self.assertFalse(files.read_cities(file))
    def test_read_cities_false_4(self):
        file="1.4.csv"
        self.assertFalse(files.read_cities(file))
    def test_read_cities_true(self):
        file="1.csv"
        self.assertTrue(files.read_cities(file))
    def test_read_prod_false_1(self):
        file="2.1.csv"
        self.assertFalse(files.read_prod(file))
    def test_read_prod_false_2(self):
        file="2.2.csv"
        self.assertFalse(files.read_prod(file))
    def test_read_prod_false_3(self):
        file="2.3.csv"
        self.assertFalse(files.read_prod(file))
    def test_read_prod_false_4(self):
        file="2.4.csv"
        self.assertFalse(files.read_prod(file))
    def test_read_prod_true(self):
        file="2.csv"
        self.assertTrue(files.read_prod(file))
    def test_read_worker_time_false_1(self):
        file="3.1.csv"
        self.assertFalse(files.read_worker_time(file))
    def test_read_worker_time_false_2(self):
        file="3.2.csv"
        self.assertFalse(files.read_worker_time(file))
    def test_read_worker_time_false_3(self):
        file="3.3.csv"
        self.assertFalse(files.read_worker_time(file))
    def test_read_worker_time_true(self):
        file="3.csv"
        self.assertTrue(files.read_worker_time(file))
    def test_read_solution_false_1(self):
        file="4.1.csv"
        file1="1.csv"
        file2="2.csv"
        self.assertFalse(files.read_solution(file,file1,file2))
    def test_read_solution_false_2(self):
        file="4.2.csv"
        file1="1.csv"
        file2="2.csv"
        self.assertFalse(files.read_solution(file,file1,file2))
    def test_read_solution_false_3(self):
        file="4.3.csv"
        file1="1.csv"
        file2="2.csv"
        self.assertFalse(files.read_solution(file,file1,file2))
    def test_read_solution_true(self):
        file="4.csv"
        file1="1.csv"
        file2="2.csv"
        self.assertTrue(files.read_solution(file,file1,file2))
        
    
if __name__ == '__main__':
    unittest.main()
