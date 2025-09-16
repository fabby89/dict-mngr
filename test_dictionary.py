import unittest
from dictionary_class import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dict = Dictionary()

    def test_newentry(self):
        self.dict.new_entry("gato", "es un felino")
        self.assertIn("gato", self.dict.myDict)
        self.assertEqual(self.dict.myDict["gato"], "es un felino")

    def test_lookup(self):
        self.dict.myDict["perro"] = "animal canino"
        result = self.dict.look_up("perro")
        self.assertEqual(result, "animal canino")

if __name__ == "__main__":
    unittest.main()
