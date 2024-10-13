function getNoteIdFromURL() {
    // Get the current URL
    const urlParams = new URLSearchParams(window.location.search);

    // Extract the note ID parameter from the URL
    const noteId = urlParams.get('noteId');

    // Return the extracted note ID
    return noteId;
}

document.addEventListener('DOMContentLoaded', function() {
    const noteDetailContainer = document.getElementById('note-detail-container');

    // Fetch note data from backend
    fetchNoteData();

    // Function to fetch note data from backend
    function fetchNoteData() {
        // Assuming the note ID is obtained from the URL query parameter
        const noteId = getNoteIdFromURL(); // Implement this function to extract note ID from URL
        console.log('Note ID:', noteId);
        // Fetch note data using the note ID
        fetch(`/api/note/${noteId}`)
            .then(response => response.json())
            .then(note => {
                renderNoteDetail(note);
            })
            .catch(error => console.error('Error fetching note data:', error));
    }

    // Function to render note detail on the page
    function renderNoteDetail(note) {
        const noteDetailElement = document.createElement('div');
        noteDetailElement.classList.add('note-detail');

        const titleElement = document.createElement('h2');
        titleElement.textContent = note.title;

        const subjectElement = document.createElement('p');
        subjectElement.textContent = note.subject;

        const topicElement = document.createElement('p');
        topicElement.textContent = note.topic;

        const sourceElement = document.createElement('p');
        sourceElement.textContent = note.source;

        const contentElement = document.createElement('p');
        contentElement.textContent = note.content;


        const timestampElement = document.createElement('p');
        timestampElement.textContent = `Timestamp: ${note.timestamp}`;

        noteDetailElement.appendChild(titleElement);
        noteDetailElement.appendChild(subjectElement);
        noteDetailElement.appendChild(topicElement);
        noteDetailElement.appendChild(sourceElement);
        noteDetailElement.appendChild(contentElement);
        //noteDetailElement.appendChild(timestampElement);

        noteDetailContainer.appendChild(noteDetailElement);
    }
});
