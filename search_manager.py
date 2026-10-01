class SearchManager:
    def search(self, notes, keyword):
        results = []

        for note in notes:
            if keyword.lower() in note["note"].lower():
                results.append(note)

        return results