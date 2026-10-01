# NoteBoard – Smart Note Scanning and Organization System

## Project Description

NoteBoard is a student-focused note management system designed to help students organize and find their notes more easily.

The proposed system follows this process:

*Scan → Extract → Organize → Save → Search*

## Problem

Students often have notes scattered across notebooks and phone photos. Finding specific topics can take time, and important information can become difficult to locate.

## Proposed Solution

NoteBoard provides one place where notes can be added, organized by category, saved, and searched using keywords.

## OOP Classes

The system uses the following classes:

- User – represents a system user.
- Note – represents a note and its category.
- Category – represents a note category.
- NoteScanner – handles the scanning process.
- TextExtractor – handles text extraction.
- NoteOrganizer – organizes note content and categories.
- SearchManager – searches notes using keywords.

## Current Features

- Add Note
- View Notes
- Delete Note
- Search Notes
- Categorize Notes
- JSON Data Persistence
- Object-Oriented Classes
- Unit Testing

## Testing

Unit tests are implemented using Python unittest.

Current tests cover:

- Note creation
- Category creation
- Note searching

Current result:

*3 tests passed successfully.*

## Current Development Status

The current prototype has the core OOP structure, note management functions, search, persistence, and unit tests implemented.

The scanning and text extraction components currently serve as the prototype structure for the planned image-to-text workflow.

## Future Development

- Actual image scanning
- OCR/text extraction
- AI-assisted note processing
- Web/PWA interface
- Improved organization
- Export functionality
- Additional testing
## How to Run

1. Open the NoteBoard project folder in VS Code.
2. Open the Terminal.
3. Run the application:

```bash
python app.py