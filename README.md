# 💰 Expense Tracker

A professional web-based expense tracking application built with **Flask** and **MongoDB**. Users can register, login, and manage their personal income and expense transactions securely.

---

## 🚀 Features

- 🔐 User Authentication (Register / Login / Logout)
- 🔒 Passwords stored securely using hashing (Werkzeug)
- 📊 Dashboard with Balance, Total Income & Total Expense summary
- ➕ Add income and expense transactions
- 🗑️ Delete transactions
- 💾 All data persisted in MongoDB
- 🎨 Modern dark UI with glassmorphism design
- 📱 Responsive layout (mobile friendly)

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | Python, Flask     |
| Database   | MongoDB (pymongo) |
| Frontend   | HTML, CSS         |
| Auth       | Flask Sessions, Werkzeug |
| Config     | python-dotenv     |

---

## 📁 Project Structure

```
Expence_tracker/
│
├── static/
│   └── style.css          # All styles (dark theme, auth, navbar)
│
├── templates/
│   ├── index.html         # Main dashboard
│   ├── login.html         # Login page
│   └── register.html      # Register page
│
├── app.py                 # Flask app, routes, MongoDB logic
├── .env                   # Environment variables (not committed)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Edit the `.env` file:
```env
MONGO_URI=mongodb://localhost:27017/
SECRET_KEY=your_super_secret_key_change_this
```

> 💡 For MongoDB Atlas (cloud), replace `MONGO_URI` with your Atlas connection string:
> ```
> MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
> ```

### 4. Start MongoDB locally
```bash
mongod
```

### 5. Run the application
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 🗄️ MongoDB Collections

Database: `expense_tracker`

| Collection     | Description                          |
|----------------|--------------------------------------|
| `users`        | Stores user name, email, hashed password |
| `transactions` | Stores transactions linked to user_id |

---

## 🔐 Authentication Flow

```
Visit any page
     ↓
Not logged in? → Redirect to /login
     ↓
/register → Create account → Redirect to /login
     ↓
/login → Enter credentials → Dashboard
     ↓
Dashboard → Logout → Back to /login
```

---

## 📸 Pages

- `/register` — Create a new account
- `/login` — Login to your account
- `/` — Main dashboard (protected)
- `/add` — Add a transaction (POST)
- `/delete/<id>` — Delete a transaction
- `/logout` — Logout and clear session

---

## 📦 Dependencies

```
flask
pymongo
python-dotenv
werkzeug
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Made with ❤️ using Flask & MongoDB
