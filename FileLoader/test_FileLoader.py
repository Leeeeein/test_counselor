import unittest
from FileLoader import *
import os


file_path = os.path.join(os.path.dirname(__file__), '../', 'gghh.pdf')
class MyTestCase(unittest.TestCase):
    def test_read_pdf_with_pypdf2(self):
        text = read_pdf_with_pypdf2(file_path)
        assert text != None

    def test_index_2_pages(self):
        pages = read_pdf_with_pypdf2(file_path)
        dic = index_2_pages(pages)
        print(dic)
        assert dic != None

if __name__ == '__main__':
    unittest.main()
