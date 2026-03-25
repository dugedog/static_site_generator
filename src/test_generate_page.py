import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title_hello(self):
        md = "# hello"

        title = extract_title(md)

        self.assertEqual(title, "hello")

    def test_extract_title_raises_exception(self):
        md = """ 
hello there was
            oncee a man with three pies
"""
        with self.assertRaises(Exception):
            title = extract_title(md)
            print(title)

    def test_extract_title_raises_exception_with_message(self):
        md = """ 
hello there was
            oncee a man with three pies
"""
        with self.assertRaises(Exception) as context:
            title = extract_title(md)
            print(title)

        self.assertEqual(str(context.exception), "Header not found in markdown")

class TestGeneratePage(unittest.TestCase):
    def test_extract_title_late_title(self):
        md = """
Once I went to the shop and 

found a bunch of stuff

in the house

the biggest thing i found

was a 

# Heading
"""



        title = extract_title(md)

        self.assertEqual(title, "Heading")


