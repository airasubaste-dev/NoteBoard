from note import Note


class NoteOrganizer:
    def organize(self, note, category):
        print("Organizing note...")

        return {
            "note": note,
            "category": category
        }

    def create_note(self, content, category):
        return Note(content, category)