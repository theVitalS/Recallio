# Recalio

Recalio is a Python-based app designed to enhance the learning process by generating "smart notes" and automating a personalized schedule for spaced repetition. With Recalio, users can retain knowledge more effectively by creating, organizing, and reviewing notes optimized for long-term retention. The project is currently in the early stages of development, with a working prototype written in Flask and ongoing refactoring to a FastAPI and React.js stack for improved performance and scalability.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Overview

Recalio's core purpose is to support efficient, sustained learning through the creation of smart notes and a structured review schedule. Leveraging concepts from cognitive psychology, such as spaced repetition and active recall, Recalio automates reminders to review notes at optimized intervals, ensuring that information is refreshed in memory before it begins to fade. 

Currently, Recalio is in an early development stage, with a Flask-based prototype in use, and is actively being refactored to a FastAPI backend and a React.js frontend to provide a more scalable and responsive experience.

## Key Features

- **Smart Note Creation**: Create notes optimized for active recall and easy review.
- **Automated Spaced Repetition**: Review schedules are generated automatically based on each note's age, difficulty, and previous review history.
- **User-Friendly Interface**: A React.js interface (coming soon) to enhance note management and review scheduling.
- **Personalized Review Reminders**: Set customized reminders based on individual learning progress.
- **Data Analysis and Insights** (planned): Track learning trends, retention rates, and usage patterns to optimize study strategies.

## Tech Stack

- **Current Prototype**
  - Backend: Flask (Python)
  - Database: SQLite (for early prototyping)

- **Upcoming Refactored Version**
  - Backend: FastAPI (Python)
  - Frontend: React.js
  - Database: PostgreSQL or MongoDB (to be decided based on scalability needs)

## Installation

### Prerequisites
- Python 3.8+
- Node.js and npm (for frontend development)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/theVitalS/Recallio.git
   cd Recallio
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Development Server** (Flask prototype)
   ```bash
   FLASK_APP=app.app.py FLASK_ENV=development flask run
   ```


## Roadmap

- **Refactor Backend**: Transition from Flask to FastAPI for a more robust and scalable backend.
- **React Frontend**: Develop a responsive React.js interface.


## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make changes and commit.
4. Submit a pull request for review.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---
