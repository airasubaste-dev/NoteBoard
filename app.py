import json
import os
from note import Note
from category import Category
from user import User
from note_scanner import NoteScanner
from text_extractor import TextExtractor
from note_organizer import NoteOrganizer
from search_manager import SearchManager

FILE_NAME = "notes.json"


def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


notes = load_notes()
organizer = NoteOrganizer()
search_manager = SearchManager()

print("===== NOTEBOARD =====")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")
    print("5. Search Notes")

    choice = input("Choose an option: ")

    if choice == "1":
        content = input("Enter your note: ")

        category_name = input("Enter category: ")
        category = Category(category_name)

        note = organizer.create_note(content,category.name)
        organized_note = organizer.organize(note.content, note.category)

        notes.append(organized_note)
        save_notes(notes)

        print("Note added and saved successfully!")

    elif choice == "2":
        print("\n===== YOUR NOTES =====")

        if len(notes) == 0:
            print("No notes yet.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "3":
        print("\n===== DELETE NOTE =====")

        if len(notes) == 0:
            print("No notes to delete.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

            try:
                number = int(input("Enter note number to delete: "))

                if 1 <= number <= len(notes):
                    deleted = notes.pop(number - 1)
                    save_notes(notes)
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid note number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using NoteBoard!")
        break
    elif choice == "5":
        keyword = input("Enter keyword to search: ")
        results = search_manager.search(notes, keyword)

        print("\n===== SEARCH RESULTS =====")

        if len(results) == 0:
            print("No notes found.")
        else:
            for i, note in enumerate(results, start=1):
                print(f"{i}. {note}")
    