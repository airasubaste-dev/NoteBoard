# NoteBoard – Smart Note Scanning and Organization System

## Project Description

NoteBoard is a student-focused note management system designed to help students organize, save, and find their notes more easily.

The system provides a web interface for adding notes, assigning categories, scanning note images, extracting text using OCR, searching notes by keyword, and deleting notes.

### Main Workflow

*Scan → Extract → Organize → Save → Search*

## Problem Statement

Students often keep notes across notebooks and phone photos. Finding specific topics can take time, and important information can be difficult to locate.

## Proposed Solution

NoteBoard provides a single interface where users can add and categorize notes, scan images to extract text, save notes, and search for information using keywords.

## Current Features

- Add notes
- Assign categories to notes
- View saved notes
- Scan note images using Tesseract.js OCR
- Display extracted text
- Transfer extracted text to the note editor
- Search notes by keyword
- Delete notes
- Store notes in a JSON file through the Flask application
- Display the date and time for each saved note
- Responsive pastel-themed web interface
- Support scanning and text extraction through the web interface

## Object-Oriented Programming Classes

The project includes the following Python classes:

- User – represents a system user.
- Note – represents a note.
- Category – represents a note category.
- NoteScanner – provides a scanning component.
- TextExtractor – provides a text-extraction component.
- NoteOrganizer – organizes note content and categories.
- SearchManager – searches notes using keywords.

Note: The web interface currently performs OCR through Tesseract.js in the browser. The Python scanning and text-extraction classes are separate prototype components.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Tesseract.js
- JSON
- pytest

## Requirements

- Python installed
- Flask and the packages listed in requirements.txt
- A modern web browser
- Internet connection for loading the Tesseract.js library from its CDN

## How to Run

1. Open the NoteBoard project folder in VS Code.
2. Open the integrated terminal.
3. Install the dependencies:

   python -m pip install -r requirements.txt
4. Start the web application:


   python web_app.py

5. Open the local address shown in the terminal, usually:

   http://127.0.0.1:5000

Keep the terminal open while using the application.

## Testing

Run the automated tests using:

python -m pytest -v

The current test suite covers note creation, category creation, and note searching.

The previously recorded test run passed all three tests. Run the command again to verify the current version.

## Data Storage

Notes are stored in notes.json by the Flask application. Back up this file before making changes that could affect saved data.

## Current Development Status

The application currently provides a working web interface for note creation, image-based OCR, searching, deletion, and JSON-backed note storage.

The Python scanning and text-extraction classes are prototype components and are not the OCR engine used by the web interface.

## Future Improvements

- Improve error handling and input validation
- Expand automated tests for the web API and OCR workflow
- Add note editing and additional organization features
- Improve deployment and setup documentation
- Explore optional AI-assisted study features