# Recalio

This is an early version of my pet project aimed at helping users in learning by providing efficient recalling of information. 

## Tech Stack

- **Current Prototype**
  - Backend: Flask (Python)
  - Database: SQLite (for early prototyping)

- **Upcoming Refactored Version**
  - Backend: FastAPI (Python)
  - Frontend: React.js
  - Database: PostgreSQL

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
