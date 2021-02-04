import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase): 
    def test_englishtofrench(self): 
        self.assertEqual(englishtofrench(""), "Input is empty")
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench("Hey"), "Bonjour")

class TestEnglishToGerman(unittest.TestCase): 
    def test_englishtogerman(self): 
        self.assertEqual(englishtogerman(""), "Input is empty")
        self.assertEqual(englishtogerman("Hello"), "Hallo")
        self.assertNotEqual(englishtogerman("Hey"), "Hallo")

unittest.main()
