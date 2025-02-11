# Flask Form Application

## Overview
This is a basic web application built using Flask for the backend, HTML, CSS, and JavaScript for the frontend, and SQL for data storage. The application allows users to submit a form, which is then stored in a database.

## Features
- User-friendly form interface
- Backend validation using Flask
- Data storage using SQL
- Frontend styling with CSS
- Dynamic behavior with JavaScript

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQL (SQLite/MySQL/PostgreSQL, as per configuration)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sanskarkesari/Basic-Form-Application.git
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Set up the database (for SQLite, create a `.db` file; for MySQL/PostgreSQL, configure database credentials in `config.py`).

4. Run the application:
   ```bash
   python app.py
   ```
5. Open the browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure
```
├── templates/
│   ├── form.html
├── app.py
├── README.md
```

## Usage
1. Open the web application.
2. Fill in the form with the required details.
3. Submit the form.
4. The submitted data is stored in the database.

## Future Improvements
- Implement user authentication
- Add form validation on both frontend and backend
- Enhance UI with better styling
- Support multiple database options

## License
This project is licensed under the MIT License.

