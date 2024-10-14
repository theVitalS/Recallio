from datetime import timedelta, datetime

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.database.models import Note, Reminder, local_timezone
from backend.database.db_operations import *
from config import DATABASE_URL

#from google.cloud import speech_v1p1beta1 as speech

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL  #'sqlite:////home/vital/LearNotik/LearNotik2/backend/database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Home route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reminders')
def reminders():
    return render_template('reminders.html')


@app.route('/note')
def note():
    return render_template('note.html')

@app.route('/tables')
def table():
    return render_template('sb/tables.html')


# API route to get all notes
@app.route('/api/notes')
def get_notes():
    try:
        notes = db.session.query(Note).all()
        notes_json = [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]
        return jsonify(notes_json), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/api/note/<int:note_id>', methods=['GET'])
def get_note(note_id):
    try:
        # Query the database for the note with the given ID
        note = db.session.query(Note).filter(Note.id == note_id).first()

        # Construct a dictionary containing the note information
        note_info = {
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'timestamp': note.timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Convert timestamp to string format
            'subject': note.topic.subject.name if note.topic else '',
            'topic': note.topic.name if note.topic else '',
            'source': note.source.name if note.source else ''
        }

        print(note_info)
        # Return the note information as JSON response
        return jsonify(note_info), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


# API route to add a new note
@app.route('/api/add-note', methods=['POST'])
def add_note():
    print(f"add_note request: {request.json}")
    data = request.json
    title = data.get('title')
    content = data.get('content')
    subject = data.get('subject')
    topic = data.get('topic')
    source = data.get('source')

    if title and content:
        topic_object = get_or_create_topic(db.session, topic, subject)
        source_object = get_or_create_source(db.session, source)

        new_note = Note(title=title, content=content, topic=topic_object, source=source_object)
        db.session.add(new_note)

        repetition_template = [1, 3, 7, 14, 28]  # Number of days after the note creation date
        for days in repetition_template:
            reminder_date = datetime.now(local_timezone) + timedelta(days=days)
            new_reminder = Reminder(note=new_note, reminder_date=reminder_date.date())
            db.session.add(new_reminder)

        db.session.commit()
        return jsonify({'message': 'Note added successfully'})
    else:
        return jsonify({'error': 'Title and content are required'}), 400


@app.route('/api/reminders')
def get_reminders():
    reminders = db.session.query(Reminder).all()
    reminders_data = [{
        'id': reminder.id,
        'reminder_date': reminder.reminder_date.strftime('%Y-%m-%d'),
        'note_id': reminder.note.id,
        'note_title': reminder.note.title,
        # Add other relevant reminder/note information here
    } for reminder in reminders]
    return jsonify(reminders_data)
