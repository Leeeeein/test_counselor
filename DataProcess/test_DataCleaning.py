import unittest
from DataCleaning import *

class MyTestCase(unittest.TestCase):
    def test_remove_special_characters(self):
        text = 'Hello, 你好！This is an example text, it contains some special characters like #, $, and %.这是一段中文文本，包含一些特殊字符，如#、$和%。'
        cleaned_text = remove_special_characters(text)
        self.assertTrue(all(c.isalnum() or c.isspace() for c in cleaned_text), "字符串中包含非字母数字和空格的特殊字符")


    def test_split_string(self):
        text = 'Hello, world\n How are you today?'
        expected_split_text = ['Hello, world',' How are you today?']
        split_text = split_string(text, '\n')
        self.assertEqual(split_text, expected_split_text)


if __name__ == '__main__':
    unittest.main()
