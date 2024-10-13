// note-item.js
export function NoteItem(title, noteId) {
    const noteItem = document.createElement('li');
    noteItem.classList.add('note-item');

    // Create an anchor element
    const link = document.createElement('a');
    link.textContent = `${title}`; // Set the link text to the note title
    link.href = `/note?noteId=${noteId}`; // Set the link URL to the desired page URL, replace "/note/" with your actual route

    // Append the link to the list item
    noteItem.appendChild(link);

    return noteItem
}
