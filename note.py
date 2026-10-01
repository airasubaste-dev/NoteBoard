class Note:
    def __init__(self, content, category):
        self.content = content
        self.category = category

    def display(self):
        return f"{self.content} [{self.category}]"