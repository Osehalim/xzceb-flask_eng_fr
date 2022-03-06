import unittest
from translator import french_to_english
class Testfrench_to_english(unittest.TestCase):
    def test1(self)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
unittest.main()

import unittest
from translator import french_to_english
class Testfrench_to_english(unittest.TestCase):
    def test2(self)
        self.assertNotEqual(french_to_english('Bonjour'), 'Beautiful')
unittest.main()

import unittest
from translator import english_to_french
class Testenglish_to_french(unittest.TestCase):
    def test3(self)
        self.assertNotEqual(english_to_french('Hello'), 'Oui')
unittest.main()

import unittest
from translator import english_to_french
class Testenglish_to_french(unittest.TestCase):
    def test4(self)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
unittest.main()