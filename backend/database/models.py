from datetime import datetime, timezone
import pytz
from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
local_timezone = pytz.timezone('Europe/Warsaw')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    topics = relationship('Topic', back_populates='subject')


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=True)
    subject = relationship('Subject', back_populates='topics')
    notes = relationship('Note', back_populates='topic')


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    notes = relationship('Note', back_populates='source')


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now(local_timezone))
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=True)
    topic = relationship('Topic', back_populates='notes')
    source_id = Column(Integer, ForeignKey('sources.id'), nullable=True)
    source = relationship('Source', back_populates='notes')
    note_reminders = relationship('Reminder', back_populates='note', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Note('{self.title}')"


class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True)
    reminder_date = Column(Date, nullable=False)
    note_id = Column(Integer, ForeignKey('notes.id'), nullable=False)
    note = relationship('Note', back_populates='note_reminders')

    def __repr__(self):
        return f"Reminder for note {self.note.title} on {self.reminder_date}"
