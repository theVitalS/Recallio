import { NoteItem } from './note-item.js';

document.addEventListener('DOMContentLoaded', function() {
    const remindersContainer = document.getElementById('reminders-container');

    // Function to fetch reminders from the backend
    function fetchReminders() {
        fetch('/api/reminders')
            .then(response => response.json())
            .then(reminders => {
                // Clear previous reminders
                remindersContainer.innerHTML = '';

                // Sort reminders by reminder_date
                reminders.sort((a, b) => new Date(a.reminder_date) - new Date(b.reminder_date));

                // Group reminders by day
                const groupedReminders = {};
                reminders.forEach(reminder => {
                    const day = reminder.reminder_date;
                    groupedReminders[day] = groupedReminders[day] || [];
                    groupedReminders[day].push(reminder);
                });

                // Render grouped reminders on the page
                Object.keys(groupedReminders).forEach(day => {
                    const remindersForDay = groupedReminders[day];

                    // Create a box for each day's reminders
                    const reminderBox = document.createElement('div');
                    reminderBox.classList.add('reminder-box');

                    // Create a header for the day
                    const dayHeader = document.createElement('div');
                    dayHeader.classList.add('day-header');
                    dayHeader.textContent = day;
                    reminderBox.appendChild(dayHeader);

                    // Create list for reminders of this day
                    const remindersList = document.createElement('ul');
                    remindersForDay.forEach(reminder => {
                        const reminderItem = NoteItem(reminder.note_title, reminder.note_id);
                        remindersList.appendChild(reminderItem);
                    });
                    reminderBox.appendChild(remindersList);

                    // Append the reminder box to the container
                    remindersContainer.appendChild(reminderBox);
                });
            })
            .catch(error => console.error('Error fetching reminders:', error));
    }

    // Fetch reminders when the page loads
    fetchReminders();
});
