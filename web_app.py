from flask import Flask, render_template, request, jsonify
import json
import os
from note import Note

app = Flask(__name__)

FILE_NAME = "notes.json"


def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/notes", methods=["GET"])
def get_notes():
    notes = load_notes()

    keyword = request.args.get("search", "").lower()

    if keyword:
        notes = [
            note for note in notes
            if keyword in note["note"].lower()
        ]

    return jsonify(notes)

@app.route("/api/scan", methods=["POST"])
def scan_note():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "No image selected"}), 400

    return jsonify({
        "message": "Image received successfully",
        "filename": image.filename
    }), 200

@app.route("/api/notes", methods=["POST"])
def add_note():
    data = request.get_json()

    content = data.get("note", "").strip()
    category = data.get("category", "General").strip()

    if not content:
        return jsonify({"error": "Note content is required"}), 400

    notes = load_notes()

    note_obj = Note(content, category)

    new_note = {
        "note": note_obj.content,
        "category": note_obj.category
    }

    notes.append(new_note)
    save_notes(notes)

    return jsonify(new_note), 201


@app.route("/api/notes/<int:index>", methods=["DELETE"])
def delete_note(index):
    notes = load_notes()

    if index < 0 or index >= len(notes):
        return jsonify({"error": "Note not found"}), 404

    deleted = notes.pop(index)
    save_notes(notes)

    return jsonify(deleted)


if __name__ == "__main__":
    app.run(host="0.0.0.0", 
    port=5000, debug=True)