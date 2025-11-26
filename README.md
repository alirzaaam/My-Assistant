# Flask Todo List with Weather API

🧠 **Overview**  
This is a web-based **Todo List application** built with Flask. Users can register, log in, add, and delete tasks. The app also integrates the **OpenWeatherMap API** to show real-time weather information for the user's city on the dashboard.  

💡 **Key Features**  
- **User Authentication:** Register, log in, and log out securely.  
- **Todo Management:** Add new tasks and delete completed tasks.  
- **Profile Management:** Change password and update your city.  
- **Weather Integration:** Displays current weather information for the user’s city (temperature, description, icon).  
- **Responsive Alerts:** Uses Flask’s `flash` messages for errors and confirmations.  

⚙️ **How to Run**  

1. **Clone the repository**  

```bash
git clone https://github.com/yourusername/flask-todo-weather.git
cd flask-todo-weather
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy code
pip install cs50 flask flask-session werkzeug requests
Run the application

bash
Copy code
python app.py
Open in browser
Visit http://127.0.0.1:5000

📁 File Structure

bash
Copy code
.
├── app.py             # Main Flask application
├── templates/         # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   └── done.html
├── todo.db            # SQLite database (auto-created)
└── README.md          # Project documentation
🌐 Features Summary

✅ Secure user registration and login
✅ Add and delete tasks dynamically
✅ Update profile and city information
✅ Displays real-time weather data for the user’s city
✅ Flash messages for validation and confirmations

🧰 Technologies Used

Backend: Python, Flask, CS50 SQL

Database: SQLite

Authentication: Werkzeug for password hashing

API Integration: OpenWeatherMap API

Frontend: HTML, CSS, Jinja2 templates

⚠️ Notes

You need a valid OpenWeatherMap API key to fetch weather data.

Make sure the database file todo.db is writable by your app.

Ensure proper handling of session and CS50 SQL queries.


