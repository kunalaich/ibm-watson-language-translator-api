import unittest

from translator import englishtofrench

class TestEnglishToFrench(unittest.TestCase): 
    def test_englishtofrench(self): 
        self.assertEqual(englishtofrench(""), "Input is empty")
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench("Hey"), "Bonjour")

unittest.main()
