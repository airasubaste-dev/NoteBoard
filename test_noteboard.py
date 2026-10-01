import unittest
from note import Note
from category import Category
from search_manager import SearchManager

class TestNote(unittest.TestCase):

    def test_note_creation(self):
        note = Note("Python OOP", "Programming")
        self.assertEqual(note.content, "Python OOP")

    def test_category_creation(self):
        category = Category("Programming")
        self.assertEqual(category.name, "Programming")

    def test_search_notes(self):
        manager = SearchManager()

        notes = [
            {"note": "Python OOP", "category": "Programming"},
            {"note": "Database Basics", "category": "Database"}
        ]

        results = manager.search(notes, "Python")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["note"], "Python OOP")


if __name__ == "__main__":
    unittest.main()