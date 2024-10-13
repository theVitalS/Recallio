import { NoteItem } from './note-item.js';

document.addEventListener('DOMContentLoaded', function() {
    const noteForm = document.getElementById('note-form');
    const noteList = document.getElementById('note-list');

    // Function to fetch notes from the backend
    function fetchNotes() {
        fetch('/api/notes')
            .then(response => response.json())
            .then(notes => {
                noteList.innerHTML = ''; // Clear previous notes
                notes.forEach(note => {
                    const noteItem = NoteItem(note.title, note.id);
                    noteList.appendChild(noteItem);
                });
            })
            .catch(error => console.error('Error fetching notes:', error));
    }

    // Fetch notes when the page loads
    fetchNotes();

   // Handle form submission
noteForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const subject = document.getElementById('subject').value;
    const topic = document.getElementById('topic').value;
    const source = document.getElementById('source').value;

    // Validate title and content
    if (!title.trim() || !content.trim()) {
        console.error('Title and content are required');
        return;
    }

    //console.log('Adding note:', title, content);

    // Send POST request to add a new note
    fetch('/api/add-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, content, subject, topic, source})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Fetch notes again to update the list
        fetchNotes();

        const titleField = document.getElementById('title');
        titleField.value= '';

        const contentField = document.getElementById('content');
        contentField.value= '';
    })
    .catch(error => console.error('Error adding note:', error));
});
});
